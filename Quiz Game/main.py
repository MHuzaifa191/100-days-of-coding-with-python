from question_model import Question
from data import question_data
import html
from ui import QuizUI

question_bank = []


for i in question_data["results"]:
    question_text = i['question']
    question_answer = i["correct_answer"]
    unescaped_question = html.unescape(question_text)
    new_question = Question(unescaped_question, question_answer)
    question_bank.append(new_question)


window = QuizUI(question_bank)


print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_number}")
