#Written by Ryan Matthews. Purpose of taking class section data from sections.csv file and automating Google Classroom course creation using GAM for all the homeroom classes. Started 9/6/17

#Dynamic variables that are unique for each new course
sectionID = 0
teacherEmail = ''
emailDict = { -1 : 'email'}
name = ''
room = 0

#Opening csv files to read in data. The file teachers.csv file must be used to determine the email of the teacher who leads the course.
sections = open("data/sections.csv","r")
teachers = open("data/teachers.csv","r")

#Creating a dictionary of teacher ID's to the corresponding emails.
for teacher in teachers:
	if "School" in teacher:
		continue
	vars =  teacher.split(',')
	emailDict[vars[1]] = vars[4][:(vars[4].index('rockymountain'))] + "rmpscholars.org"

#Teacher file no longer required
teachers.close()

print "SectionId,TeacherEmail,CourseName"

#For loop to iterate over each line of the csv file and allocate the variables appropriately 
for section in sections:
	if "School" in section:
		continue
	if "Homeroom" not in section:
		continue
	if "AM" in section:
		continue
	vars = section.split(',')
	sectionID = vars[1]
	if vars[2] == '':
		print 'Cannot make course ' + vars[9] + ' Section ' + vars[7] + ', no teacher ID provided.'
		continue 
	try:
		teacherEmail = emailDict[vars[2]]
	except KeyError:
		print 'Error making class ' + vars[9] + ' Section ' + vars[7] + ' due to invalid teacher id value: ' + vars[2] + '.'
		continue
	name = vars[9]
	room = vars[0]
	print sectionID , "," , teacherEmail, "," , name
	#Call GAM commands. Must use a bash enabling module as GAM is only accessable through GAM.
	#Command for class creation: gam create course [id | alias <alias>] [teacher <teacher email>] [name <name>] [section <section>] [heading <heading>] [description <description>]
	

#Close sections file 
sections.close()	
