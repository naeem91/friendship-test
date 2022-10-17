import requests

url = 'https://opentdb.com/api.php?amount=100&category={cat}'
categories = (9,10,11)
BE_URL = 'http://localhost:8080/api/questions'


for cat in categories:
    response = requests.get(url.format(cat=cat)).json()
    for result in response.get('results'):
        question = result.get('question')
        choices = result.get('incorrect_answers')
        correct = result.get('correct_answer')
        choices.append(correct)

        payload = {
            "question_text": question,
            "choices":[{"choice_text": choice} for choice in choices]
        }
        
        requests.post(BE_URL, json=payload)
