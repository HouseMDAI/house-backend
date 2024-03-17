import os
from openai import OpenAI
from .models import FilledQuestionary


api_key = os.environ.get("API_KEY")
print("api_key", api_key)
client = OpenAI(api_key=api_key)

def get_response(user_card: str, message: str, filled_questionary: FilledQuestionary, max_tokens=100):
    system_prompt = """You are a doctor that gives user an opportunity to swiftly check up health and diagnos an illness using anamnes and a short questionary. 
    Your task is to ask questions and give your opinion and advices.
    You can ask questions until you sure abour your advice. Try to strive to about 5 questions per request.
    You can respond in two formats: 
    1. ask more questions in json format {"questions":[{"text":"first question"},{"text":"second question"}]}
    2. give your final opinion, assumption, or advice in json format {"text":"Advice: Drink more water"}
    """
    prompt = f"""request message: {message}; anamnesis: {user_card}; filled questionary: {filled_questionary}"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"{system_prompt}",
            },
            {
                "role": "user",
                "content": f"{prompt}",
            },
        ],
        model="gpt-3.5-turbo",
        max_tokens=max_tokens
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":

    from user_card import UserCard
    

    card = UserCard(age=20, 
                    weight=60, 
                    height=150,
                    gender="female",
                    disease_list=["diabetes", "hypertension"])
    print(card)

    #user_card = f"age: {age}, weight: {weight}, gender: {gender}, list of disease: {disease}"

    print(get_response(card))