from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
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

Session = sessionmaker(bind=engine)

session = Session()

# Заповнення таблиці "students" даними
student1 = Student(name='Bae', age=18)
student2 = Student(name='Eddy', age=21)
student3 = Student(name='Lily', age=22)
student4 = Student(name='Jenny', age=19)
student5 = Student(name='Lily', age=22)

session.add_all([student1, student2, student3, student4, student5])
session.commit()

# Заповнення таблиці "subjects" даними
subject1 = Subject(name='English', length='32 weeks')
subject2 = Subject(name='Spanish', length='27 weeks')
subject3 = Subject(name='Chinese', length='142 weeks')
subject4 = Subject(name='Math', length='73 weeks')


session.add_all([subject1, subject2, subject3, subject4])
session.commit()

# Заповнення таблиці "student_subjects" даними
student_subject1 = StudentSubject(student_id=1, subject_id=1)
student_subject2 = StudentSubject(student_id=1, subject_id=2)
student_subject3 = StudentSubject(student_id=2, subject_id=3)
student_subject4 = StudentSubject(student_id=3, subject_id=1)
student_subject5 = StudentSubject(student_id=4, subject_id=4)

session.add_all([student_subject1, student_subject2, student_subject3, student_subject4, student_subject5])
session.commit()