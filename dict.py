students={
    1:{"name": "Sai charan", "age": 19},
    2:{"name": "Sai Rithik", "age":209},
    3:{"name": "Sai Micharl", "age": 21},
    4:{"name": "Sai Girish", "age": 22},
    5:{"name": "Sai Sup", "age": 23},

}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")