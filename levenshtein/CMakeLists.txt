cmake_minimum_required(VERSION 3.5)
project(levenshtein C)

set(CMAKE_C_STANDARD 99)

add_library(levenshtein SHARED library.c)