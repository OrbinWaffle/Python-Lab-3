# Name: Joshua Lai
# Lab 9
# Completed 4/19/2022

import os
from enum import Enum

class Student:
   _name : str
   _email : str
   _id : int
   _curr_score : int
   _high_score : int
   def __init__(self, name, email) -> None:
      self._name = name
      self._email = email
   
class Statistics:
   _students = [Student]
   def __init__(self, student_list = []) -> None:
      self._students = student_list
   def display_students(self):
      for stud in self._students:
         print(stud._name)
   

class Question:
   _question_content : str
   _answers = [str]
   _correct_answer : str
   def __init__(self, ques : str, answers, correct : str) -> None:
      self._question_content = ques
      self._answers = answers
      self._correct_answer = correct
   def display(self):
      ch = 'A'
      print(self._question_content)
      for index in range(len(self._answers)):
         print(str(chr(ord(ch) + index)) + ": " + str(self._answers[index]))
   def try_answer(self, answer : str) -> bool:
      return(answer == self._correct_answer)

def session():
   curr_user = login()
   test(curr_user)

def test(user : Student):
   print("Let's get started.")


def login():
   global stats
   global id_index
   print("Hello. Welcome to the test-taking system.")
   while True:
      name = input("Please input your name: ")
      email = input("Please input your email: ")

      # Get a list of all users that match this email
      matching_users = [stud for stud in stats._students if stud._email == email]
      matching_user = None

      # If the list is not empty, we found a match
      if(len(matching_users) > 0):
         matching_user = matching_users[0]
      if(not matching_user == None):
         if(not name == matching_user._name):
            print(f"User already exists with email {email}. Please try again.")
            continue
         else:
            print(f"Sucessfully logged in. Welcome, {name}.")
            return matching_user
      else:
         print(f"Creating new user {name} with email {email}...")
         new_student = Student(name, email)
         stats._students.append(new_student)
         print(f"Sucessfully created user. Welcome, {name}.")
         return new_student

def get_questions():
   global question_bank
   mode = 0
   dir_path = os.path.dirname(os.path.realpath(__file__))
   question_file = open(dir_path + "\\" + "Questions.txt", "r")
   question = ""
   options = []
   while True:
      line = question_file.readline()
      line = line.rstrip("\n")
      if(line == "END"):
         break
      if(line == "QUESTION"):
         mode = 0
      elif(line == "OPTION"):
         mode = 1
      elif(line == "ANSWER"):
         mode = 2
      else:
         match mode:
            case 0:
               question += (line + "\n")
            case 1:
               options.append(line)
            case 2:
               answer = (line + "\n")
               question_bank.append(Question(question, options, answer))

   question_file.close()

question_bank = []

student_one = Student("bob", "bob@mogus.com")
studs = [student_one]
stats = Statistics(studs)

id_index = 0

if __name__ == "__main__":
   ques = Question("Do you love Among Us?", ["yes", "no"], "A")
   ques.display()
   print(ques.try_answer("A"))
   get_questions()
   print(len(question_bank))
   question_bank[0].display()
   while(True):
      stats.display_students()
      session()