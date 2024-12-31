import random
class Student:
    def __init__(self, name, student_Id, grade):
        self.name = name
        self.student_Id = student_Id
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_Id}, Grade: {self.grade}"
        
class VotingSystem:
    def __init__(self, minimum_grade = 9):
        self.students = []
        self.minimum_grade = minimum_grade

    def register_student(self, student):
        try:
            if int(student.grade) >= self.minimum_grade:
                self.students.append(student)
                print(f"{student.name} registered successfully.")
            else:
                print(f"{student.name} is not eligible to vote.Grade must be {self.minimum_grade} or above.")
        except ValueError:
            print(f"Invalid grade for {student.name}.Please enter a valid integer.")

    def display_registered_students(self):
        print("\nRegistered Students:")
        for student in self.students:
            print(student)

    def conduct_elections(self):
        votes_for_candidate_a = 0
        votes_for_candidate_b = 0

        for student in self.students:
            vote = student.can_vote()
            if vote == "A":
                votes_for_candidate_a += 1
            elif vote == "B":
                votes_for_candidate_b += 1

        print(f"Votes for Candidate A: {votes_for_candidate_a}")
        print(f"Votes for candidate B: {votes_for_candidate_b}")

        if votes_for_candidate_a > votes_for_candidate_b:
            print("Candidate A wins!")
        elif votes_for_candidate_b > votes_for_candidate_a:
            print("Candidate B wins!")
        else:
            print("It's a tie!")

def get_student_details():
    name = input("Enter student name(or q to quit): ")
    if name.lower() == 'q':
        print("Thank you or stayig with us")
        return 0
    student_Id = input("Enter student ID: ")
    grade = input("Enter student grade: ")
    try:
        return Student(name, student_Id, grade)
    except ValueError as e:
        print(f"Error: {e}")
        return None  
        
voting_system = VotingSystem()
while True:
    student = get_student_details()
    if student:
        voting_system.register_student(student)
    else:
        break

voting_system.register_student(student)
