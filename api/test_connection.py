import pymongo
import sys

##Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
client = pymongo.MongoClient('mongodb://freakathon:mypassword@docdb-2024-10-16-05-06-03.czka0iao0bxo.us-east-2.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false') 

##Specify the database to be used
db = client.test

##Insert a single document
db.example.insert_one({
            "name": "Phase 2 Clinical Trial for Type 2 Diabetes Medication",
            "location": {
                "city": "San Francisco",
                "state": "CA",
                "zip": "94103"
            },
            "qualifications": {
                "ageRange": {
                    "minAge": 18,
                    "maxAge": 65
                },
                "gender": "Any",
                "race": "Any",
                "veteran_status": false,
                "disability_status": false,
                "past_conditions": [
                    "Type 2 Diabetes",
                    "High Blood Pressure"
                ],
                "immunization": "Up-to-date COVID-19 vaccination",
                "observation": [
                    "Glucose levels",
                    "Blood pressure",
                    "Body mass index"
                ],
                "allergies": [
                    "None"
                ],
                "procedure": "Daily oral medication for 12 weeks, with bi-weekly check-ins."
            }
        })

##Find the document that was previously written
x = db.example.find_one({'name':'Phase 2 Clinical Trial for Type 2 Diabetes Medication'})

##Print the result to the screen
print(x)

##Close the connection
client.close()