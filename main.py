from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    t = i["question"]
    a = i["correct_answer"]
    question = Question(t, a)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print(f"your total score is: {quiz.score}")

