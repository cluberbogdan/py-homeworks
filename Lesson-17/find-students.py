from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Student, Subject, StudentSubject

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='lesson-17',
        user='postgres',
        password='password',
        port=5432,
    )
)

session = Session(bind=engine)

english_students = (
    session.query(Student)
    .join(StudentSubject, StudentSubject.student_id == Student.student_id)
    .join(Subject, Subject.subject_id == StudentSubject.subject_id)
    .filter(Subject.name == 'English')
    .all()
)

# Отримайте імена студентів
english_student_names = [student.name for student in english_students]

print("Students name that visited 'English' classes:")
for name in english_student_names:
    print(name)