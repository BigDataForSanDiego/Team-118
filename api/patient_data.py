from typing import List, Dict
import json
from jsonschema import validate, ValidationError

with open('synth_data/patient_data/patient_schema.json', 'r') as schema_file:
    patient_schema = json.load(schema_file)

#print(patient_schema)

def get_age(mrn: str) -> int:
    pass

def get_location(mrn: str) -> Dict:
    pass

def get_gender(mrn: str) -> str:
    pass

def get_race(mrn: str) -> str:
    pass

def get_veteran_status(mrn: str) -> bool:
    pass

def get_disability_status(mrn: str) -> bool:
    pass

def get_condition(mrn: str) -> List:
    pass

def get_immunization(mrn: str) -> Dict:
    pass

def observations(mrn: str) -> List:
    pass

def get_allergy_intolerance(mrn: str) -> List:
    pass

def get_procedures(mrn: str) -> List:
    pass

def get_medications_requests(mrn: str) -> List:
    pass

def get_goal(mrn: str) -> str:
    pass


