import psycopg2
import os

#Prints all students
def getAllStudents():
    try:
        conn = psycopg2.connect(database="A3",
            host="localhost",
            user="postgres",
            password="postgres",
            port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STUDENTS")
        #Print data retrieved.
        for entry in cursor.fetchall():
            print(entry)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Retrieving students failed,", e)

#Adds a student
def addStudents(first_name, last_name, email, enrollment_date):
    try:
        conn = psycopg2.connect(database="A3",
                host="localhost",
                user="postgres",
                password="postgres",
                port="5432")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO STUDENTS(first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Adding students failed,", e)

#Updates the email of the student corresponding to student_id
def updateStudentEmail(student_id, new_email):
    try:
        conn = psycopg2.connect(database="A3",
                    host="localhost",
                    user="postgres",
                    password="postgres",
                    port="5432")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE STUDENTS SET email = '{new_email}' WHERE student_id = {student_id};")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Unable to update email,", e)

#Deletes a student
def deleteStudent(student_id):
    try:
        conn = psycopg2.connect(database="A3",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5432")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM STUDENTS WHERE student_id = {student_id};")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Deleting failed,", e)

while True:
    print('')
    print("To quit press 0")
    print("To execute getAllStudents() press 1")
    print("To execute addStudents() press 2")
    print("To execute updateStudentEmail() press 3")
    print("To execute deleteStudent() press 4")
    user_input = input("Input: ")
    print('')
    os.system('cls')

    #If statements to execute one of the above functions when the correct user input is inputted.
    if user_input == '0':
        break
    elif user_input == '1':
        getAllStudents()
    elif user_input == '2':
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        enrollment_date = input("Enrollment date: ")
        addStudents(first_name, last_name, email, enrollment_date)
    elif user_input == '3':
        student_id = input("Student ID: ")
        new_email = input ("New email: ")
        updateStudentEmail(student_id, new_email)
    elif user_input == '4':
        student_id = input("Student ID: ")
        deleteStudent(student_id)
    else:
        print("Invalid input.")
