cmake_minimum_required(VERSION 3.14)

# Set the top-level project name
project(raspberry-surveillance)

add_executable(${CMAKE_PROJECT_NAME})
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

set(SOURCES
	src/main.cpp
	src/logger.cpp
)

set(HEADERS
	include/logger.h
)

target_sources(${CMAKE_PROJECT_NAME} PRIVATE ${SOURCES})
target_sources(${CMAKE_PROJECT_NAME} PRIVATE ${HEADERS})
