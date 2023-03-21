class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_num = self.question_number
        user_ans = input(f"Q.{int(question_num) + 1}: {self.question_list[question_num].text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_ans, self.question_list[question_num].answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{int(self.question_number)} \n")

