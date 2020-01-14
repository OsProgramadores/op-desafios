cmake_minimum_required(VERSION 3.10)

# set the project name
project(Desafio-02)

# add the executable
add_executable(primes primes.c)

# specify the C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)

# configure needed libraries
target_link_libraries(primes m)

