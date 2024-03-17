from pydantic import BaseModel
from datetime import datetime

class UserInformation(BaseModel):
    name: str
    age: int
    weight: int
    gender: str
    disease_list: list[str]
    height: int


class MedicalHistory(BaseModel):
    Diagnosis: dict[datetime, str]
    Medications: dict[datetime, str]
    Allergies: dict[datetime, str]
    Surgeries: dict[datetime, str]


class LifestyleFactors(BaseModel):
    Diet: dict[datetime, str]
    Exercise: dict[datetime, str]
    Smoking: dict[datetime, str]
    AlcoholConsumption: dict[datetime, str]


class SymptomsConcerns(BaseModel):
    Symptome: dict[datetime, str]


class AdditionalNotes(BaseModel):
    Notes: dict[datetime, str]


class UserCard(BaseModel):
    userInformation: dict[UserInformation, str]
    medicalHistory: dict[MedicalHistory, str]
    lifestyleFactors: dict[LifestyleFactors, str]
    symptomsConcerns: dict[SymptomsConcerns, str]
    additionalNotes: dict[AdditionalNotes, str] 

class UserCardSimple(BaseModel):
    sex: str
    age: int
    weight: int
    height: int
    special_conditions: str
    

