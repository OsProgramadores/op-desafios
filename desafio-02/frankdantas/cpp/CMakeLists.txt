cmake_minimum_required (VERSION 3.16)

set(CMAKE_GENERATOR "MinGW Makefiles")

project(numero_primos VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED on)



add_executable(numero_primos main.cpp)