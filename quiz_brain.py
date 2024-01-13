class QuizBrain:
    def __init__(self, list_of_questions):
        self.question_number = 0
        self.question_list = list_of_questions
        self.score = 0

    def next_question(self):
        q_text = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        q_answer = input(f"Q.{self.question_number}: {q_text}. (True/False)?: ")
        if self.check_answer(q_answer, correct_answer):
            self.score += 1

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score +=1
        else:
            print("That is wrong.")
        print(f"the correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


    def still_has_question(self):
        return self.question_number < len(self.question_list)
