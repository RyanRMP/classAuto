studentDict = {}

students = open('data/students.csv', "r")
for student in students:
	data = student.split(",")
	email = data[25] + "@rmpscholars.org"
	key = data[1]
	studentDict[key] = email 
students.close()

enrollments = open('data/enrollments.csv', "r")
for enrollment in enrollments:
	data = enrollment.split(",")
	studentId = data[2].rsplit()[0]
	sectionId = data[1]
	if 'Section' in enrollment:
		print "Section_id,Student_id,Student_email"
		continue
	print sectionId,",",studentId,",",studentDict[studentId]
