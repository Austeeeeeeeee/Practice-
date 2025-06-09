import time
class Student_grade_calculation():
	def __init__(self,name,surname,class_name):
		self.name = name
		self.surname = surname
		self.class_name = class_name
		self.dic = {}

	def student_identification(self,name,surname,class_name):
		self.name = input('Introduce your name: ')
		self.surname = input('Introduce your surname: ')
		self.class_name = input("Introduce your class name: ")

	def print_student_idendification(self):
		print("-- STUDENT INFORMATION --")
		print(f"Student name: {self.name} ")
		print(f"Student surname: {self.surname} ")
		print(f"Student class name: {self.class_name}")


	def grade_information(self,history,mathematics,art):
		print("-- GRADE'S INFORMATION --")
		self.dic = {"History": history,
			   		"Mathematics":mathematics,
			   		"Arts": art}


		print("\n Printing out grades information...")
		time.sleep(2)
		for subject, grade in self.dic.items():
			print(f"{subject}:{grade}")

	def average_grade_calculation(self):
		average_grade = sum(self.dic.values()) / len(self.dic.values())
		rounded_average_grade = round(average_grade,1)
		print(f"Average grade: {rounded_average_grade}")
		return rounded_average_grade



step_one = Student_grade_calculation("Marcos","Garcia","B")
step_one.print_student_idendification()
print("\n")
step_one.grade_information(1,1,1)
step_one.average_grade_calculation()


'''
THIS IS HOW THE FUNCTION SHOULD LOOK IF YOU LET THE USER INSERT INPUT


def grade_information(self):
print("-- GRADE'S INFORMATION --")
		self.dic = {"History": 0,
			   		"Mathematics": 0,
			   		"Arts": 0}

		History = int(input("Enter your history grade: "))
		self.dic['History'] = History
		Mathematics = int(input("Enter your mathematics grade: "))
		self.dic['Mathematics'] = Mathematics
		Arts = int(input("Enter your arts grade: "))
		self.dic['Arts'] = Arts
'''