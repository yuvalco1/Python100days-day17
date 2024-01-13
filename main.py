from question_model import Question
# from data import question_data
from new_data import question_data
from quiz_brain import QuizBrain
class User:
    def __init__(self, user_id,username):
        self.user_id = user_id
        self.username = username
        self.followers = 0  # Default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

if __name__ == '__main__':
    user1 = User('001', 'angela')
    user2 = User('002', 'jack')
    question_bank = []

    for i in range(len(question_data)):
        question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))

    my_quiz = QuizBrain(question_bank)

    while my_quiz.still_has_question():
        my_quiz.next_question()
    print("You completed the quiz")
    print(f"Your final score was: {my_quiz.score}/{len(question_bank)}")
