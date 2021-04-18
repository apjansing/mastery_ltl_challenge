# Mastery Data Coding Challenge
The purpose of this exercise is to simulate real world requirements and delivering on those requirements.

## LTL Service
You have been tasked with implementing a Less-than-load (LTL) truck-shipment matching system.
The system combines LTL shipments into a single truckload so that all shipments can be completed by a single truck.
For example, you can assume that the average truck can haul 48,000 lbs while the average LTL shipment is 8,000 lbs or less. 

### Requirements
* Must expose some kind of API (REST/GraphQL or other) to create trucks and shipments
  * Must be able to create trucks and shipments
  * Trucks and shipments are immutable, will not change once created
  * Trucks and shipments must be created even if a match is not currently available, only deny creation if validation fails
* Trucks must be loaded with shipments without exceeding capacity
* Shipments must fit on one truck, **cannot** be divided among multiple trucks
* Must include report endpoint for:
  * All successful matches
  * Trucks without shipments
  * Shipments without a truck
* **Bonus** Optimize LTL shipments based on location (i.e., minimize the distance between shipments for each truck)

### Data Model
Trucks
```
ID: String
Capacity: Number
Origin_Latitude: Float
Origin_Longitude: Float
Destination_Latitude: Float
Destination_Longitude: Float
```

Shipment
```
ID: String
Weight: Number
Origin_Latitude: Float
Origin_Longitude: FLoat
Destination_Latitude: Float
Destination_Longitude: Float
```

## Expectations
* Use any language/framework/databases/techniques you are comfortable with.
* Solution should be packaged in docker container(s)
  * Please provider docker-compose for multi-container solutions.
* Include a README that includes:
  * Instructions on how to run the solution.
  * What/Why you chose the solution you did.
* There is no time limit.

### To Submit
Provide a link to the code on GitHub/Dropbox.