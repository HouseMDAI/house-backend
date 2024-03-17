import os
from openai import OpenAI
from .models import FilledQuestionary
import ast


api_key = os.environ.get("API_KEY")
client = OpenAI(api_key=api_key)

def get_response(user_card: str, message: str, filled_questionary: FilledQuestionary, max_tokens=200):
    format_question = """{"questions":[{"text":"first question"},{"text":"second question"}]}"""
    format_advice = """{"text":"Advice: Drink more water"}"""
    
    system_prompt = f"""
    You are a doctor that gives user an opportunity to swiftly check up health and diagnos an illness using anamnes and a short questionary. 
    Your task is to ask short questions and give your opinion and advices.
    Your questions are accamulated in the filled questionary, which is empty in the first itteration. 
    
    Strive to about 1-2 questions per iteration and up to 6 questions in total (can be less). Questions must be short, clear, shouldn't repeat, 
    and should be relevant to the user's health condition, and should require easy answers.
    Ask questions only in the json format {format_question}.

    Number of answered questions: {len(filled_questionary.filled_questions)}
    If the Number of answered questions is more then 6, you should stop asking questions an`d provide an give your final opinion, 
    assumption or advice only in the json format {format_advice}.

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

    from user_card import get_default_user_card

    card = get_default_user_card()
    filled_questionary = FilledQuestionary(filledQuestions=dict())
    message = "Hallo I am feeling bad today, can you advise?"

    response = get_response(user_card=card, filled_questionary=filled_questionary, message=message)
    dict_response = ast.literal_eval(response)

    for i, text in enumerate(dict_response["questions"]):
        print(f"{i+1} {text['text']}")
    
    


    


    

