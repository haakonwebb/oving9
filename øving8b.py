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
    
def readfile():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as file:
        questions = list()
        for line in file:
            linetemp = line.split(":")
            questions.append(Question(linetemp[0], linetemp[2], linetemp[1]))
        return questions
if __name__ == "__main__":   
    question = readfile()
    
