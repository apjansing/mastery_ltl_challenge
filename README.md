# [Mastery Less-than-load (LTL) Challenge](https://github.com/apjansing/mastery_ltl_challenge)

- [Mastery Less-than-load (LTL) Challenge](#mastery-less-than-load-ltl-challenge)
  - [Requirements](#requirements)
  - [Dependencies](#dependencies)
    - [Local Dependencies](#local-dependencies)
    - [Docker Images](#docker-images)
    - [Python Dependencies](#python-dependencies)
  - [Getting Started](#getting-started)
    - [Installing Dependencies](#installing-dependencies)
    - [Starting the application](#starting-the-application)
    - [Confirm the application is running](#confirm-the-application-is-running)
    - [API Endpoints](#api-endpoints)
      - [make_truck](#make_truck)
      - [make_shipment](#make_shipment)
      - [get_shipments and get_trucks](#get_shipments-and-get_trucks)
      - [generate_report](#generate_report)
  - [Further Work](#further-work)

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
### Installing Dependencies
To start, you must have docker and docker-compose installed. Please follow from the following sites:
 - [docker](https://docs.docker.com/get-docker/)
 - [docker-compose](https://docs.docker.com/compose/install/)

### Starting the application
Once docker-compose is installed, all you need to do is clone this repository and run the `docker-compose up` command (include `-d` if you wish to suppress the logs of the containers).

```bash
git clone git@github.com:apjansing/mastery_ltl_challenge.git
cd mastery_ltl_challenge
docker-compose up -d
```

### Confirm the application is running
Now you can visit http://localhost:5000/ to confirm the application is running. You should see a version of [this project's homepage](https://apjansing.github.io/mastery_ltl_challenge/) without the theme applied to it.

### API Endpoints
#### make_truck
To enter a truck, with a unique ID, into the database run a POST command like the following. Trucks with the same ID will be rejected.
```bash
curl -X POST -H "Content-Type: application/json" -d '{"ID": "truck_123", "Capacity": 48000, "Origin_Latitude": 123.4, "Origin_Longitude": 123.4, "Destination_Latitude": 123.4, "Destination_Longitude": 123.4}' http://localhost:5000/make_truck
```
Trucks must follow the schema:
```bash
{
  'ID': str,
  'Capacity': int,
  'Origin_Latitude': float,
  'Origin_Longitude': float,
  'Destination_Latitude': float,
  'Destination_Longitude': float
}
```

#### make_shipment
To enter a shipment, with a unique ID, into the database run a POST command like the following. Shipments with the same ID will be rejected.
```bash
curl -X POST -H "Content-Type: application/json" -d '{"ID": "shipment_456", "Weight": 200, "Origin_Latitude": 123.4, "Origin_Longitude": 123.4, "Destination_Latitude": 123.4, "Destination_Longitude": 123.4}' http://localhost:5000/make_shipment
```
Shipments must follow the schema:
```bash
{
  'ID': str,
  'Weight': int,
  'Origin_Latitude': float,
  'Origin_Longitude': float,
  'Destination_Latitude': float,
  'Destination_Longitude': float
}
```

#### get_shipments and get_trucks
Either visit `http://localhost:5000/get_shipments` or `http://localhost:5000/get_trucks` to get a list of shipments or trucks, respectively, in JSON form.
```bash
curl -X GET http://localhost:5000/get_trucks
curl -X GET http://localhost:5000/get_shipments
```

#### generate_report
Visit `http://localhost:5000/get_shipments` or run the following to get an HTML report of the trucks and shipments currently in the database.
```bash
curl -X GET http://localhost:5000/generate_report
```

## Further Work
The following tasks were left incomplete to ensure I had something to submit for sake of this test.
- [ ] Trucks must be loaded with shipments without exceeding capacity
- [ ] Shipments must fit on one truck, **cannot** be divided among multiple trucks
- [ ] Must include report endpoint for:
  - [ ] All successful matches
  - [ ] Trucks without shipments
  - [ ] Shipments without a truck