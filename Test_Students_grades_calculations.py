import pytest

from Students_average_grade import Student_grade_calculation

def test_average_grade_calculation():
	student = Student_grade_calculation('Marcos','Garcia','B')
	student.grade_information(1,1,1)
	result = student.average_grade_calculation()
	assert result == 1.0