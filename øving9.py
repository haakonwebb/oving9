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
            return True
        else:
            print("\nThat is the wrong answer! \n")
            return False
    
    def __str__(self):
        answerstring = ""
        for i in range(len(self.qlist)):
            answerstring += f"{i}. {self.qlist[i]} \n"
        return f"{self.qtext} \n{answerstring}"
    
def readfile():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as file:
        questions = list()
        for line in file:
            linetemp = line.split(":")
            questionslist = linetemp[2]
            questionslist = questionslist.replace("[","")
            questionslist = questionslist.replace("]", "")
            questionslist = questionslist.split(",")
            q = Question(linetemp[0], questionslist, int(linetemp[1]))
            questions.append(q)
        return questions

if __name__ == "__main__":   
    questions = readfile()
    p1points = 0
    p2points = 0
    for i in range(len(questions)):
        print(questions[i])
        p1answer = int(float(input("Player 1 please enter your answer here: ")))
        p2answer = int(float(input("Player 2 please enter your answer here: ")))
        print("Player 1:")
        if questions[i].checkanswer(p1answer) == True:
            p1points += 1
        elif questions[i].checkanswer(p1answer) == True:
            p2points -= 1
        print("Player 2:")
        if questions[i].checkanswer(p2answer) == True:
            p2points += 1
        elif questions[i].checkanswer(p2answer) == False:
            p2points -= 1

    print(f"Player 1 had: {p1points} points")
    print(f"Player 2 had: {p2points} points")
    if p1points > p2points:
        print("Player 1 is the winner!")
    elif p2points > p1points:
        print("Player 2 is the winner!")
    else:
        print("There was no winner")