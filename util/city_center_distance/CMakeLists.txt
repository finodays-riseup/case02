cmake_minimum_required(VERSION 3.20)
project(city_center_distance)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS_RELEASE "-Ofast")

add_executable(city_center_distance main.cpp)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(city_center_distance PRIVATE Threads::Threads)
