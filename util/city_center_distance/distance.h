#ifndef DISTANCE_H
#define DISTANCE_H

#include <cmath>

const long double ONE_DEG = (M_PI) / 180.0;

inline long double DegToRadians(const long double &degrees) {
    return degrees * ONE_DEG;
}

long double
Distance(const long double &lat1, const long double &lon1, const long double &lat2, const long double &lon2) {
    auto lat1R = DegToRadians(lat1);
    auto lon1R = DegToRadians(lon1);
    auto lat2R = DegToRadians(lat2);
    auto lon2R = DegToRadians(lon2);

    // Haversine Formula
    auto dLonR = lon2R - lon1R;
    auto dLatR = lat2R - lat1R;

    return 6378137.0L * 2 * std::asin(std::sqrt(std::pow(std::sin(dLatR / 2), 2) +
                                                std::cos(lat1R) * std::cos(lat2R) *
                                                std::pow(std::sin(dLonR / 2), 2)));

}

#endif
