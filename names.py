#Part 1:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def studentNames(students):
    for value in students:
        print value["first_name"], value["last_name"]
studentNames(students)

#Part 2:
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentsInstructors(users):
    for key, value in users.items():
        print key
        for x in value:
            print value.index(x)+1, x["first_name"], x["last_name"], len(x["first_name"]) + len(x["last_name"])
studentsInstructors(users)

