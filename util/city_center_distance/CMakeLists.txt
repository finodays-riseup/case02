cmake_minimum_required(VERSION 3.20)
project(cpp_sandbox)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS_RELEASE "-Ofast")

add_executable(cpp_sandbox main.cpp)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(cpp_sandbox PRIVATE Threads::Threads)
