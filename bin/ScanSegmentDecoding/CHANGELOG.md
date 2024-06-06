# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.4] - 2023-10-10

### Removed

* Removed notice about .bat file inside SICK network

## [2.0.3] - 2023-05-15

### Changed

* Update license information table

## [2.0.2] - 2023-05-05

### Changed

* Simplified pipeline

## [2.0.0] - 2023-04-19

### Added

* Added license information

### Changed

* Renamed package to `scansegmentdecoding`

## [1.0.0] - 2023-03-17

### Added

* Added unit tests for msgpack util
* Added documentation for classes and functions

### Removed

* Removed the class `RestAPI_Handler`
* Removed the function `UDP_Handler.sendData`
* The following was removed in this project and will be moved to the `StandaloneDataRecorder` project:
    * Properties and rssi related functionality from `decodeUtil`.
    * The `msgpackFrameGenerator` class
    * The `sdrHandler` class
    * The `tcpStreamer` class
* Removed linting from the dev-dependencies because of licensing reasons

### Changed

* Renamed `UDP_Handler` to `UDPHandler`
* Renamed `UDP_Handler.waitOnNewScan` to `UDPHandler.receiveNewScanSegment`

## [0.4.0] - 2022-12-12

### Added

* Added gitlab ci support

### Changed

* Renamed project and package to segmentrecording

