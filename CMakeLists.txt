#  Set minimum version of cmake that is able to compile this project
cmake_minimum_required(VERSION 3.31)

#  Set up language-specific variables, run compiler and linker checks
project(cmake_conan_qt LANGUAGES CXX)

#  Set the C++ standard to 17 or later
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

#  Install packages for both Debug and Release configuration
execute_process(COMMAND conan install --settings=build_type=Debug --update --build=missing ${CMAKE_SOURCE_DIR})
execute_process(COMMAND conan install --settings=build_type=Release --update --build=missing ${CMAKE_SOURCE_DIR})

# Include the file generated after 'conan install' commands
include(${CMAKE_BINARY_DIR}/generators/conan_toolchain.cmake)

#  Start processing "CMakeLists.txt" in "src" directory
add_subdirectory(src)