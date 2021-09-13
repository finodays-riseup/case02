#include <atomic>
#include <future>
#include <iostream>
#include <tuple>

#include "csv.h"
#include "distance.h"

struct TCoord {
    long double Lat;
    long double Lon;
};

inline std::tuple<std::size_t, long double> FindNearestCity(const std::vector<TCoord> &cities, const TCoord &p) {
    long double minDistance = Distance(cities[0].Lat, cities[0].Lon, p.Lat, p.Lon);
    std::size_t idx = 0;

    for (std::size_t i = 1; i < cities.size(); i++) {
        const auto &d = Distance(cities[i].Lat, cities[i].Lon, p.Lat, p.Lon);
        if (minDistance > d) {
            minDistance = d;
            idx = i;
        }
    }

    return std::make_tuple(idx, minDistance);
}

std::vector<TCoord>
ReadCoords(
        const std::string &filepath,
        const std::string &latHeader = "geo_lat",
        const std::string &lonHeader = "geo_lon"
) {
    io::CSVReader<2, io::trim_chars<' ', '\t'>, io::double_quote_escape<',', '"'>> reader(filepath);
    reader.read_header(io::ignore_extra_column, latHeader, lonHeader);

    std::vector<TCoord> coords;
    TCoord tmp{};
    while (reader.read_row(tmp.Lat, tmp.Lon)) {
        coords.push_back(tmp);
    }

    return coords;
}

int main() {
    auto cities = ReadCoords("city.csv");
    std::clog << "City table read done.\n";
    auto ads = ReadCoords("all_v2.csv");
    std::clog << "Ad table read done.\n";

    std::vector<std::size_t> cityIdxByAd(ads.size());
    std::vector<long double> ccdByAd(ads.size()); // CCD - city center distance
    std::atomic<std::size_t> progress(0);

    auto fn = [&cities, &ads, &cityIdxByAd, &ccdByAd, &progress](const std::size_t &left, const std::size_t &right) {
        for (std::size_t i = left; i != right; i++, progress++) {
            std::tie(cityIdxByAd[i], ccdByAd[i]) = FindNearestCity(cities, ads[i]);
        }
    };

    const std::size_t JOB_COUNT = 4;
    const auto &startTime = std::chrono::system_clock::now();
    const auto &totalSize = ads.size();
    const auto &baseJobSize = totalSize / JOB_COUNT;
    const auto &remainder = totalSize % JOB_COUNT;

    std::vector<std::future<void>> futures;
    for (std::size_t i = 0, offset = 0; i < JOB_COUNT; i++) {
        const auto &left = offset;
        const auto &right = offset + baseJobSize + (i < remainder);

        futures.push_back(std::async(std::launch::async, fn, left, right));
        std::clog << "Job #" + std::to_string(i) +
                     " [" + std::to_string(left) + "-" + std::to_string(right) + "] created.\n";

        offset = right;
    }
    while (!futures.empty()) {
        auto fs = futures.back().wait_for(std::chrono::seconds(10));
        if (fs == std::future_status::ready) {
            futures.pop_back();
        } else {
            auto now = std::chrono::system_clock::now();
            auto diff = std::chrono::duration_cast<std::chrono::seconds>(now - startTime).count();
            std::clog << "[" + std::to_string(diff) + "] Progress: " +
                         std::to_string(progress.load()) + "/" + std::to_string(totalSize) + ".\n";
        }
    }
    std::clog << "All jobs are done " + std::to_string(progress.load()) + "/" + std::to_string(totalSize) + ".\n";

    std::clog << "Writing output file.\n";
    std::freopen("ccd.csv", "w+", stdout);
    std::cout << "city_idx,city_center_distance\n";
    for (std::size_t i = 0; i < ads.size(); i++) {
        std::cout << cityIdxByAd[i] << ',' << ccdByAd[i] << '\n';
    }

    return 0;
}
