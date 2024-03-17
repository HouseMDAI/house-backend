from pydantic import BaseModel
from datetime import datetime

class UserInformation(BaseModel):
    name: str = "Alice Smith"
    age: int = 45
    weight: int = 65  # in kilograms
    gender: str = "Female"
    disease_list: list[str] = ["Hypertension", "Type 2 Diabetes"]
    height: int = 160  # in centimeters

class MedicalHistory(BaseModel):
    diagnosis: dict[datetime, str] = {
        datetime(2019, 5, 10): "Hypertension",
        datetime(2020, 2, 15): "Type 2 Diabetes",
        datetime(2022, 1, 5): "Hyperlipidemia"
    }
    medications: dict[datetime, str] = {
        datetime(2019, 5, 10): "Lisinopril (10 mg daily)",
        datetime(2020, 2, 15): "Metformin (1000 mg twice daily)",
        datetime(2022, 1, 5): "Atorvastatin (20 mg daily)"
    }
    allergies: dict[datetime, str] = {
        datetime(2020, 2, 15): "None reported"
    }
    surgeries: dict[datetime, str] = {
        datetime(2018, 8, 20): "Appendectomy"
    }

class LifestyleFactors(BaseModel):
    diet: dict[datetime, str] = {
        datetime(2021, 1, 1): "Mediterranean diet rich in fruits, vegetables, and whole grains"
    }
    exercise: dict[datetime, str] = {
        datetime(2021, 1, 1): "Regular exercise regimen including cardio and strength training, 3 times per week"
    }
    smoking: dict[datetime, str] = {
        datetime(2019, 5, 10): "Non-smoker"
    }
    alcohol_consumption: dict[datetime, str] = {
        datetime(2019, 5, 10): "Occasional social drinker (1-2 drinks per week)"
    }

class SymptomsConcerns(BaseModel):
    symptome: dict[datetime, str] = {
        datetime(2022, 2, 10): "Intermittent chest pain"
    }

class AdditionalNotes(BaseModel):
    notes: dict[datetime, str] = {
        datetime(2022, 2, 10): "Family history of heart disease; Currently experiencing stress due to work and family responsibilities"
    }

class UserCard(BaseModel):
    userInformation: UserInformation
    medicalHistory: MedicalHistory
    lifestyleFactors: LifestyleFactors
    symptomsConcerns: SymptomsConcerns
    additionalNotes: AdditionalNotes

def get_default_user_card():
# Create a more detailed sample UserCard instance
    user_card = UserCard(
        userInformation=UserInformation(),
        medicalHistory=MedicalHistory(),
        lifestyleFactors=LifestyleFactors(),
        symptomsConcerns=SymptomsConcerns(),
        additionalNotes=AdditionalNotes()
    )
    return user_card
