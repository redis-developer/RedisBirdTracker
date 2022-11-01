# Redis Bird Tracker

Goal: Create new bird sightings and search through recorded bird sightings using Redis as a data store. Similar to Merlin or EBird.com


## Data Set

[EBird API 2.0](https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest#intro)


# Data models

## Birds

| Key | Description |
|---|---|
|`bird:<BIRD_ID>`| Taxonomy info on `<BIRD_ID>` |

Sample JSON:
```json
{
    "TAXONOMIC_ORDER": "30836",
    "CATEGORY": "species",
    "TAXON_CONCEPT_ID": "avibase-8F268682",
    "COMMON_NAME": "American Pipit",
    "SCIENTIFIC_NAME": "Anthus rubescens",
    "SUBSPECIES_COMMON_NAME": "",
    "SUBSPECIES_SCIENTIFIC_NAME": ""
}
```



## Sightings
| Key | Description |
|---|---|
|`bird:<BIRD_ID>:sightings:<SIGHTING_ID>`| One specific sighting object for bird `<BIRD_ID>` |

Sample JSON:
```json
{
    "GUID": "OBS541292727",
    "EXOTIC_CODE": "",
    "OBSERVATION_COUNT": "1",
    "BREEDING_CODE": "",
    "BREEDING_CATEGORY": "",
    "BEHAVIOR_CODE": "",
    "AGE/SEX": "",
    "OBSERVATION_DATE": "2017-10-13",
    "TIME_OBSERVATIONS_STARTED": "09:47:00",
    "OBSERVER_ID": "obsr282709",
    "SAMPLING_EVENT_IDENTIFIER": "S39901050",
    "PROTOCOL_TYPE": "Traveling",
    "PROTOCOL_CODE": "P22",
    "PROJECT_CODE": "EBIRD_PNW",
    "DURATION_MINUTES": "176",
    "EFFORT_DISTANCE_KM": "4.828",
    "EFFORT_AREA_HA": "",
    "NUMBER_OBSERVERS": "1",
    "ALL_SPECIES_REPORTED": "1",
    "GROUP_IDENTIFIER": "",
    "HAS_MEDIA": "0",
    "APPROVED": "1",
    "REVIEWED": "0",
    "REASON": "",
    "TRIP_COMMENTS": "Quite breezy at first but by 11am calmed down.  1pm high tide.  First ANMU for kitsap.",
    "SPECIES_COMMENTS": "",
    "": "",
    "LAST_EDITED_DATE": 1630411923,
}
```

## Location

| Key | Description |
|---|---|
|`location:<LOCATION_ID>`| Location info on `<LOCATION_INFO>`|

Sample JSON:

```json
    "LOCATION": {
        "USFWS_CODE": "",
        "ATLAS_BLOCK": "",
        "IBA_CODE": "",
        "BCR_CODE": "",
        "LOCATION_NAME": "Point No Point",
        "LOCATION_ID": "L109542",
        "LOCATION_TYPE": "H",
        "COUNTRY": "United States",
        "COUNTRY_CODE": "US",
        "STATE": "Washington",
        "STATE_CODE": "US-WA",
        "COUNTY": "Kitsap",
        "COUNTY_CODE": "US-WA-035",
        "COORDINATES": {
            "LATITUDE": "47.9118696",
            "LONGITUDE": "-122.5283182"
        }
    }
```



## Specific Bird Sightings
| Key | Description |
|---|---|
| `bird:<BIRD_ID>:sightings` | All sightings for one specific bird `<BIRD_ID>` | 

Sample Set:
`[sighting:OBS541292727, sighting:OBS537451909, sighting:OBS538571392, ...]`

| Key | Description |
|---|---|
| `location:<LOCATION_ID>:sightings`| All sightings for one specific `<LOCATION_ID>` |

| Key | Description |
|---|---|
| `location:<LOCATION_ID>:birds`| All birds found in one specific `<LOCATION_ID>`|

### Sighting
TODO:
change 'date' to 'timestamp' when we switch to unix timestamp


### Location 
Where the siting happened

TODO: 
GEOSPATIAL indexing on coordinates
Conversion to and from LOCATION_ID and COUNTY_CODE?

Sighting -> Specific information on Location of Bird

EBird Washington State Sighting Data from 2017 to present

Sample JSON:
```json
{
    "GUID": "OBS541292727",
    "EXOTIC_CODE": "",
    "OBSERVATION_COUNT": "1",
    "BREEDING_CODE": "",
    "BREEDING_CATEGORY": "",
    "BEHAVIOR_CODE": "",
    "AGE/SEX": "",
    "OBSERVATION_DATE": "2017-10-13",
    "TIME_OBSERVATIONS_STARTED": "09:47:00",
    "OBSERVER_ID": "obsr282709",
    "SAMPLING_EVENT_IDENTIFIER": "S39901050",
    "PROTOCOL_TYPE": "Traveling",
    "PROTOCOL_CODE": "P22",
    "PROJECT_CODE": "EBIRD_PNW",
    "DURATION_MINUTES": "176",
    "EFFORT_DISTANCE_KM": "4.828",
    "EFFORT_AREA_HA": "",
    "NUMBER_OBSERVERS": "1",
    "ALL_SPECIES_REPORTED": "1",
    "GROUP_IDENTIFIER": "",
    "HAS_MEDIA": "0",
    "APPROVED": "1",
    "REVIEWED": "0",
    "REASON": "",
    "TRIP_COMMENTS": "Quite breezy at first but by 11am calmed down.  1pm high tide.  First ANMU for kitsap.",
    "SPECIES_COMMENTS": "",
    "": "",
    "LAST_EDITED_DATE": 1630411923,

}
```


## Technologies

Datastore: Redis Stack

Backend: Flask or FastAPI (Python)
Client: Redis Om Python
Data ingestion: https://github.com/redis-developer/riot

RedisInsight

Frontend: React or Vue




