import pymongo
import sys
import json

## Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb+srv://molit:cr78tq47o4DTEuem@trialize.gs0xa.mongodb.net/?retryWrites=true&w=majority&appName=trialize') 

## Specify the database to be used
db = client.trialize_main

## Load JSON data
with open('synth_data/trial_data/sample_trials.json') as f:
    trial_data = json.load(f)

db.trials.insert_many(trial_data['trials'])

##Find the document that was previously written
x = db.trials.find_one({'name':"Phase 1 Clinical Trial for Peripheral Artery Disease Treatment"})

## Print the result to the screen
print(x[''])

## Close the connection
client.close()