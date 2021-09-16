#CS 101 Lab
#Program 2
#Alex Fonseca
#ajf8nd@umsystem.edu

#Firstly I will ask the user for the name of the person we will be calculating the grade for then ask them for the inputs of the grades

#After printing the results, I go back up to the inputs, and give exams and labs an if statment if exams and labs are above or below on what to put down
print('**** welcome to the LAB grade calculator! ****')

name = input('Who are we calculating grades for? ==> ')

labs = int(input('Enter Labs grade? ==> '))
if labs > 100:
    print('The lab value should been 100 or less. It has been changed to 100.')
    labs = 100

exams = int(input('Enter Exams grade? ==> '))
if exams < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    exams = 0

Attendances = int(input('Enter Attendance grade? ==> '))

#Secondly I will would defind each grade and letter grade by muiltlyplying it by each of the weight
labG = labs * 0.7
examG = exams * 0.2
AttG = Attendances * 0.1
full = labG + examG + AttG

#After getting the results, I then made it print out the weighted grade, but then I made a if/elif statement for the letter grade
print('The weighted grade for', name, 'is', full)
if full > 90:
    print(name, 'Has a letter grade of A')
elif full > 80:
    print(name, 'Has a letter grade of B')
elif full > 70:
    print(name, 'Has a letter grade of C')
elif full > 60:
    print(name, 'Has a letter grade of D')
elif full > 0:
    print(name, 'Has a letter grade of F')

# Finally, I print out this statement to thank the user.
print('**** Thanks for using the Lab grade calculator ****')




