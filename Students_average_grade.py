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
		print("----- STUDENT INFORMATION -----")
		print(f"Student name: {self.name} ")
		print(f"Student surname: {self.surname} ")
		print(f"Student class name: {self.class_name}")


	def grade_information(self,history,mathematics,art):
		print("-----  GRADE'S INFORMATION -----")
		self.dic = {"History": history,
			   		"Mathematics":mathematics,
			   		"Arts": art}

		for subject, grade in self.dic.items():
			print(f"{subject}:{grade}")

	def average_grade_calculation(self):
		average_grade = sum(self.dic.values()) / len(self.dic.values())
		self.rounded_average_grade = round(average_grade,1)
		print(f"Average grade: {self.rounded_average_grade}")
		return self.rounded_average_grade

	def grade_classification(self):
		if self.rounded_average_grade <5:
			print('Classified for Basic Academy')
			print('---------------------------------------')
		elif self.rounded_average_grade >5 and self.rounded_average_grade <=7:
			print('Classified for Mid Academy')
			print('---------------------------------------')
		else:
			print('Classified for Advanced Academy')
			print('---------------------------------------')



student1 = Student_grade_calculation("Marcos","Garcia","B")
student1.print_student_idendification()
student1.grade_information(3,8,2)
student1.average_grade_calculation()
student1.grade_classification()

student2 = Student_grade_calculation('Patricia','Lopez','C')
student2.print_student_idendification()
student2.grade_information(7,9,2)
student2.average_grade_calculation()
student2.grade_classification()

student3 = Student_grade_calculation('Sola','Murillo','A')
student3.print_student_idendification()
student3.grade_information(6,3,7)
student3.average_grade_calculation()
student3.grade_classification()



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