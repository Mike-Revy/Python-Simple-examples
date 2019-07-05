import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []
    
    def __init__(self):
        #tell python what types of questions there are 
        question_types = (Add, Multiply)
        #questions_types[0](1,1)
        #above gives an Add question of 1 plus 1
        for _ in range(10):
            # using underscore tells python we dont care about iteration variable
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)
        #generate 10 random questions with numbers from 1 to 10
        #add these questions into self.questions
    
    def take_quiz(self): 
        #log the start time 
        self.start_time = datetime.datetime.now()
        #ask all of the questions
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        #log if they got the question right
        #log the end time
        #show summary
        return self.summary()
    
    def ask(self, question):
        correct = False
        question_start = datetime.datetime.now()
        #log the start time
        #capture the answers
        answer = input(question.text + '= ')
        #check the answer 
        if answer == str(question.answer):
            correct = True
        #log end time 
        question_end = datetime.datetime.now()
        #if answer right, send back True
        #otherwise, send back False
        #send back the elapsed time, too
        return correct, question_end - question_start
        
    def total_correct(self):
        #return the total # of correct answers 
        #each answer in answers is a tuple or list itself with first elemeint is true or false
        total = 0
        for answer in self.answers:
            if answer[0]:
                # could have tested == True 
                total +=1
        return total
        
    def summary(self):
        #print how many you got right and the total # of questions. 5/10
        print("You got {} out of {} right.".format(
                self.total_correct(), len(self.questions)
        ))
        #print the total time for the quiz: 30 seconds! 
        #use parens after format to tell python to caluclate timedelta
        print("It too you {} seconds total.".format(
                (self.end_time-self.start_time).seconds
        ))
        
    
Quiz().take_quiz()

 ### https://github.com/carsenk   