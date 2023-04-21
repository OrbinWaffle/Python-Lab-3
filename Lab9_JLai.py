# Name: Joshua Lai
# Lab 9
# Completed 4/21/2022

import os
import random

class Student:
   _name : str
   _email : str
   _id : int
   _high_score : int
   _curr_score : int
   def __init__(self, name, email, id) -> None:
      self._name = name
      self._email = email
      self._id = id
      self._high_score = 0
      self._curr_score = 0
   
class Statistics:
   _students = [Student]
   def __init__(self, student_list = []) -> None:
      self._students = student_list
   def display_students(self):
      for stud in self._students:
         print(stud._name)
   def get_student_num(self):
      return (len(self._students))
   def get_average_score(self):
      try: 
         total = 0
         for stud in self._students:
            total += stud._curr_score
         return (total / len(self._students))
      except ZeroDivisionError:
         return 0
   

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
      print()
   def try_answer(self, answer : str) -> bool:
      return(answer == self._correct_answer)

def session():
   print("What would you like to do?\nlogin: Log in\nstats: Display statistics\nq: Quit")
   action = input("> ").lower()
   if(action == "login"):
      curr_user = login()
      test(curr_user)
   elif (action == "stats"):
      print(f"\n{stats.get_student_num()} students have taken the test.")
      print(f"The average score is {stats.get_average_score()}.\n")
   elif(action == "q"):
      quit()

def test(user : Student):
   print("\nLet's get started.\n")
   questions_asked = []
   score_log = []
   score = 0
   for question_number in range(5):
      question_to_ask : Question
      while True:
         question_index = random.randint(0, len(question_bank) - 1)
         if(question_index in questions_asked):
            continue
         questions_asked.append(question_index)
         question_to_ask = question_bank[question_index]
         break
      question_to_ask.display()
      student_answer = input("> ").upper()
      if(question_to_ask.try_answer(student_answer) == True):
         score += 1
         score_log.append(True)
      else:
         score_log.append(False)
   user._curr_score = score
   if(score > user._high_score):
      user._high_score = score

   for ques_num in range(len(score_log)):
      print(f"Question {ques_num + 1}: " + ("Correct" if score_log[ques_num] else "Incorrect") + ".")
   print(f"You got {score} " + ("question" if score == 1 else "questions") + " correct.")
   print()
         

def login():
   global stats
   global id_index
   print("\nHello. Welcome to the test-taking system.")
   while True:
      name = input("Please input your name (q to quit): ")
      if(name == "q"):
         quit()
      email = input("Please input your email: ")
      if(email == "q"):
         quit()

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
         new_student = Student(name, email, stats.get_student_num)
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
      if(line == ""):
         continue
      if(line == "END"):
         break
      if(line.startswith("QUESTION ")):
         mode = 0
      elif(line == "OPTIONS"):
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
               answer = (line)
               question_bank.append(Question(question, options, answer))
               question = ""
               options = []
               answer = ""

   question_file.close()

question_bank = []

stats = Statistics()

id_index = 0

if __name__ == "__main__":
   get_questions()
   while(True):
      session()

# TEST OUTPUT:

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): Bob
# Please input your email: bob@gmail.com
# Creating new user Bob with email bob@gmail.com...
# Sucessfully created user. Welcome, Bob.

# Let's get started.

# Which of the following is not a valid way to create a dictionary in Python?

# A: {'a': 1, 'b': 2, 'c': 3}
# B: dict(a=1, b=2, c=3)
# C: dict([('a', 1), ('b', 2), ('c', 3)])
# D: {1: 'a', 2: 'b', 3: 'c'}

# > D
# Which of the following is not a valid way to access a value in a dictionary in Python?

# A: my_dict['key']
# B: my_dict.get('key')
# C: my_dict.key
# D: my_dict.getkey()

# > d
# What is the output of the following code snippet?
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4])

# A: [2, 3, 4]
# B: [1, 2, 3, 4]
# C: [2, 3, 4, 5]
# D: [1, 3, 5]

# > A
# What is the difference between a list and a tuple in Python?

# A: A list is immutable while a tuple is mutable
# B: A tuple is ordered while a list is unordered
# C: A list can contain only integers while a tuple can contain any data type
# D: A tuple can be indexed while a list cannot be indexed

# > b
# Which of the following is not a valid way to declare a variable in Python?

# A: my_variable = 5
# B: 5 = my_variable
# C: my_variable_2 = "hello"
# D: _my_variable = True

# > b
# Question 1: Correct.
# Question 2: Correct.
# Question 3: Correct.
# Question 4: Correct.
# Question 5: Correct.
# You got 5 questions correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): Joe
# Please input your email: bob@gmail.com
# User already exists with email bob@gmail.com. Please try again.
# Please input your name (q to quit): Joe
# Please input your email: Joe@gmail.com
# Creating new user Joe with email Joe@gmail.com...
# Sucessfully created user. Welcome, Joe.

# Let's get started.

# Python is a strongly typed language.

# A: True
# B: False

# > B
# Which of the following is not a built-in data type in Python?

# A: list
# B: tuple
# C: dictionary
# D: array
# E: set

# > D
# Which of the following is a valid way to define a list containing the values 1, 2, and 3?

# A: [1 2 3]
# B: (1, 2, 3)
# C: {1, 2, 3}
# D: [1, 2, 3]

# > a
# What is the output of the following code snippet?
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print('d' in my_dict)

# A: True
# B: False

# > b
# What is the output of the following code snippet?
# my_string = "hello world"
# print(my_string.upper())

# A: HELLO
# B: hello world
# C: HELLO WORLD
# D: hello World

# > c
# Question 1: Correct.
# Question 2: Correct.
# Question 3: Incorrect.
# Question 4: Correct.
# Question 5: Correct.
# You got 4 questions correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): Isaac
# Please input your email: itdiaz@deez.nuts
# Creating new user Isaac with email itdiaz@deez.nuts...
# Sucessfully created user. Welcome, Isaac.

# Let's get started.

# What is the difference between a list and a tuple in Python?

# A: A list is immutable while a tuple is mutable
# B: A tuple is ordered while a list is unordered
# C: A list can contain only integers while a tuple can contain any data type
# D: A tuple can be indexed while a list cannot be indexed

# > a
# A tuple is an immutable sequence of elements in Python.

# A: True
# B: False

# > a
# What is the output of the following code snippet?
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4])

# A: [2, 3, 4]
# B: [1, 2, 3, 4]
# C: [2, 3, 4, 5]
# D: [1, 3, 5]

# > a
# What is the purpose of the "append" method for lists in Python?

# A: To remove the last element from a list
# B: To add a new element to the end of a list
# C: To sort the elements of a list in ascending order
# D: To check whether a given element is present in a list

# > b
# Python is a strongly typed language.

# A: True
# B: False

# > b
# Question 1: Incorrect.
# Question 2: Correct.
# Question 3: Correct.
# Question 4: Correct.
# Question 5: Correct.
# You got 4 questions correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > stats

# 3 students have taken the test.
# The average score is 4.333333333333333.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): gogo
# Please input your email: itdiaz@deez.nuts
# User already exists with email itdiaz@deez.nuts. Please try again.
# Please input your name (q to quit): Isaac
# Please input your email: itdiaz@deez.nuts
# Sucessfully logged in. Welcome, Isaac.

# Let's get started.

# Which of the following is not a built-in data type in Python?

# A: list
# B: tuple
# C: dictionary
# D: array
# E: set

# > c
# Which of the following is not a valid way to access a value in a dictionary in Python?

# A: my_dict['key']
# B: my_dict.get('key')
# C: my_dict.key
# D: my_dict.getkey()

# > a
# The "range" function returns a list of integers.

# A: True
# B: False

# > b
# What is the output of the following code snippet?
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print('d' in my_dict)

# A: True
# B: False

# > b
# A variable declared inside a function in Python is accessible outside the function.

# A: True
# B: False

# > b
# Question 1: Incorrect.
# Question 2: Incorrect.
# Question 3: Correct.
# Question 4: Correct.
# Question 5: Correct.
# You got 3 questions correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > stats

# 3 students have taken the test.
# The average score is 4.0.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): Gronk
# Please input your email: grunk@grong.com
# Creating new user Gronk with email grunk@grong.com...
# Sucessfully created user. Welcome, Gronk.

# Let's get started.

# What is the difference between a list and a tuple in Python?

# A: A list is immutable while a tuple is mutable
# B: A tuple is ordered while a list is unordered
# C: A list can contain only integers while a tuple can contain any data type
# D: A tuple can be indexed while a list cannot be indexed

# > a
# What is the purpose of the "append" method for lists in Python?

# A: To remove the last element from a list
# B: To add a new element to the end of a list
# C: To sort the elements of a list in ascending order
# D: To check whether a given element is present in a list

# > b
# Which of the following is not a valid way to declare a variable in Python?

# A: my_variable = 5
# B: 5 = my_variable
# C: my_variable_2 = "hello"
# D: _my_variable = True

# > c
# Python is a strongly typed language.

# A: True
# B: False

# > d
# The "range" function returns a list of integers.

# A: True
# B: False

# > a
# Question 1: Incorrect.
# Question 2: Correct.
# Question 3: Incorrect.
# Question 4: Incorrect.
# Question 5: Incorrect.
# You got 1 question correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > login

# Hello. Welcome to the test-taking system.
# Please input your name (q to quit): yobo
# Please input your email: yams@jams.whams
# Creating new user yobo with email yams@jams.whams...
# Sucessfully created user. Welcome, yobo.

# Let's get started.

# What is the output of the following code snippet?
# my_string = "Hello, World!"
# print(my_string[7:12])

# A: World
# B: , Wor
# C: Worl
# D: orl

# > a
# What is the output of the following code snippet?
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print('d' in my_dict)

# A: True
# B: False

# > a
# What is the output of the following code snippet?
# my_string = "hello world"
# print(my_string.upper())

# A: HELLO
# B: hello world
# C: HELLO WORLD
# D: hello World

# > a
# Python has a built-in garbage collector that automatically frees memory for objects that are no longer being used.

# A: True
# B: False

# > a
# What is the output of the following code snippet?
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4])

# A: [2, 3, 4]
# B: [1, 2, 3, 4]
# C: [2, 3, 4, 5]
# D: [1, 3, 5]

# > a
# Question 1: Correct.
# Question 2: Incorrect.
# Question 3: Incorrect.
# Question 4: Correct.
# Question 5: Correct.
# You got 3 questions correct.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > stats

# 5 students have taken the test.
# The average score is 3.2.

# What would you like to do?
# login: Log in
# stats: Display statistics
# q: Quit
# > q