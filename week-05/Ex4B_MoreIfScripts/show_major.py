# Israel Colman
# 11/13/2026

student_name = input("Enter your name: ")
student_major = input("Enter your Major: ")

if student_major == 'BIOL' or student_major == 'Biology':
    dept_office = 'Science Bldg, Room 310'
    print(f'Your major is {student_major}, Department office is {dept_office}')
elif student_major == 'CSCI' or student_major == 'Computer Science':
    dept_office = 'Sheppard Hall, Room 314'
    print(f'Your major is {student_major}, Department office is {dept_office}')
elif student_major == 'ENG' or student_major == 'English':
    dept_office = 'Kerr Hall, Room 201'
    print(f'Your major is {student_major}, Department office is {dept_office}')
elif student_major == 'HIST' or student_major == 'History':
    dept_office = 'Kerr Hall, Room 114'
    print(f'Your major is {student_major}, Department office is {dept_office}')
elif student_major == 'MKT' or student_major == 'Marketing':
    dept_office = 'Westly Hall, Room 310'
    print(f'Your major is {student_major}, Department office is {dept_office}')
elif student_major == 'MTH' or student_major == 'Math':
    dept_office = 'Sheppard Hall, Room 214'
    print(f'Your major is {student_major}, Department office is {dept_office}')
else:
    print(f"Your major is <unkown>, can't retrieve department office")