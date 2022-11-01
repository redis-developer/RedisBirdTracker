import csv 
import json
from datetime import datetime, timezone

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for index, row in enumerate(csvReader):
            #add this python dict to json array
            if index == 0:
                continue
            if index == 100000:
                break
            date = row.pop('LAST_EDITED_DATE')
            try:
                ts = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc).timestamp()
            except:
                ts = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp()
            row['LAST_EDITED_DATE'] = int(ts)

            # obs_date = row['OBSERVATION_DATE']
            # obs_ts = datetime.strptime(obs_date, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()
            # row['OBSERVATION_DATE_TS'] = int(obs_ts)
                
            # row['GUID'] = row.pop('GLOBAL_UNIQUE_IDENTIFIER')
            # row['DURATION_MINUTES'] = int(row.pop('DURATION_MINUTES'))
            # try:
            #     row['OBSERVATION_COUNT'] = int(row.pop('OBSERVATION_COUNT'))       
            # except:
            #     row['OBSERVATION_COUNT'] = -1
            # row['NUMBER_OBSERVERS'] = int(row.pop('NUMBER_OBSERVERS'))          
            
            # if row['EFFORT_DISTANCE_KM']:
            #     row['EFFORT_DISTANCE_KM'] = float(row['EFFORT_DISTANCE_KM'])
            
            # # time_int = int(time)
            # # print(time_int)

            # # time = int(time)
            
            
            row['TAXONOMY'] = {}
            taxonomy = row['TAXONOMY']
            taxonomy['TAXONOMIC_ORDER'] = row.pop('TAXONOMIC_ORDER')
            taxonomy['CATEGORY'] = row.pop('CATEGORY')
            taxonomy['TAXON_CONCEPT_ID'] = row.pop('TAXON_CONCEPT_ID')
            taxonomy['COMMON_NAME'] = row.pop('COMMON_NAME')
            taxonomy['SCIENTIFIC_NAME'] = row.pop('SCIENTIFIC_NAME')
            taxonomy['SUBSPECIES_COMMON_NAME'] = row.pop('SUBSPECIES_COMMON_NAME')
            taxonomy['SUBSPECIES_SCIENTIFIC_NAME'] = row.pop('SUBSPECIES SCIENTIFIC_NAME')
            
            row['LOCATION'] = {}
            location = row['LOCATION']
            
            location['USFWS_CODE'] = row.pop('USFWS_CODE')
            location['ATLAS_BLOCK'] = row.pop('ATLAS_BLOCK')            
            location['IBA_CODE'] = row.pop('IBA_CODE')
            location['BCR_CODE'] = row.pop('BCR_CODE')
            location['LOCATION_NAME'] = row.pop('LOCALITY')
            location['LOCATION_ID'] = row.pop('LOCALITY_ID')
            location['LOCATION_TYPE'] = row.pop('LOCALITY_TYPE')
            location['COUNTRY'] = row.pop('COUNTRY')
            location['COUNTRY_CODE'] = row.pop('COUNTRY_CODE')
            location['STATE'] = row.pop('STATE')
            location['STATE_CODE'] = row.pop('STATE_CODE')
            location['COUNTY'] = row.pop('COUNTY')
            location['COUNTY_CODE'] = row.pop('COUNTY_CODE')
            location['COORDINATES'] = {}
            location['COORDINATES']['LATITUDE'] = row.pop('LATITUDE')
            row['LOCATION']['COORDINATES']['LONGITUDE'] = row.pop('LONGITUDE')
            jsonArray.append(row)
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        # print(jsonString)
        jsonf.write(jsonString)

csvFilePath = r'bird_data.csv'
jsonFilePath = r'bird_data.json'
csv_to_json(csvFilePath, jsonFilePath)
