# Mastery Less-than-load (LTL) Challenge

- [Mastery Less-than-load (LTL) Challenge](#mastery-less-than-load-ltl-challenge)
  - [Requirements](#requirements)
  - [Dependencies](#dependencies)
    - [Local Dependencies](#local-dependencies)
    - [Docker Images](#docker-images)
    - [Python Dependencies](#python-dependencies)
  - [Getting Started](#getting-started)

## Requirements
  - [x] Must expose some kind of API (REST/GraphQL or other) to create trucks and shipments
    - [x] Must be able to create trucks and shipments
    - [x] Trucks and shipments are immutable, will not change once created
    - [x] Trucks and shipments must be created even if a match is not currently available, only deny creation if validation fails
  - [ ] Trucks must be loaded with shipments without exceeding capacity
  - [ ] Shipments must fit on one truck, **cannot** be divided among multiple trucks
  - [ ] Must include report endpoint for:
    - [ ] All successful matches
    - [ ] Trucks without shipments
    - [ ] Shipments without a truck

## Dependencies
Versions are what are were used in development and may not be actual requirements.
### Local Dependencies
  | Name | Version |
  |----|----|
  | docker | 20.10.5, build 55c4c88 |
  | docker-compose | 1.28.5, build c4eb3a1f |

### Docker Images
Images can be pulled with the pattern `Name:Version` from the table below.
  | Name | Version |
  |----|----|
  | mongo | 4.1 |
  | python | 3.8 |

### Python Dependencies
Packages used in the `flask_app` docker container.
  | Name | Version | Reason |
  | ---- | ---- | ---- |
  | bs4 | 0.0.1 | Beautiful Soup. An HTML parser. |
  | Flask | 0.12.2 | Creates REST API for creating Trucks, Shipments, and generating reports. |
  | pandas | 1.2.4  | Used in creating reports and finding which shipments to put into which trucks. |
  | pymongo | 3.7.2 | Connecting with MongoDB. |
  | requests | 2.21.0 | Performs http calls to fetch data. |

## Getting Started



