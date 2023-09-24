from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    name = Column(String)
    length = Column(String)

class StudentSubject(Base):
    __tablename__ = 'student_subjects'

    student_subject_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()