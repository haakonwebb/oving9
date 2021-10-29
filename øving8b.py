# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:25:27 2021

@author: Haakon Webb
"""

class Question:
    def __init__(self, qtext, qlist, qcorrectanswer):
        self.qtext = qtext
        self.qlist = qlist
        self.qcorrectanswer = qcorrectanswer
           
    def checkanswer(self, qanswer):
        if qanswer == self.qcorrectanswer:
            print("\nThat is the correct answer! \n")
        else:
            print("\nThat is the wrong answer! \n")
    def __str__(self):
        j = 0
        answerstring = ""
        for i in range(len(self.qlist)):
            j += 1
            answerstring += f"{j}. {self.qlist[i]} \n"
        return f"{self.qtext} \n{answerstring}"
        
if __name__ == "__main__":   
    q1 = Question("Which is the largest country?", ["Russia", "China", "America"], 1)
    print(q1)
    qanswer = int(input("Which of these is the correct answer?: "))
    q1.checkanswer(qanswer)
    q2 = Question("Who's the best player in LoL?", ["Melty", "Faker", "Tyler1"], 2)
    print(q2)
    qanswer = int(input("Which of these is the correct answer?: "))
    q2.checkanswer(qanswer)