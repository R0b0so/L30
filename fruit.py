import random
class FruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red","banana":"yellow","watermelon":"green","orange":"orange",}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of {}" .format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print('correct answer')
            else:
                print('wrong answer')
            option = int(input("Enter 0 if you want to do another quiz. Enter 1 if you want to stop : "))
            if(option):
             break
print("welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()