from db import db

class Student(db.Model):

    __tablename__ = 'student'

    studentid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(5000))
    last_name = db.Column(db.String(5000))
    date_of_birth = db.Column(db.String(5000))
    amount_due = db.Column(db.Integer())

    def __init__(self , first_name, last_name, date_of_birth, amount_due):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.amount_due = amount_due

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_db(self,student_id , first_name, last_name,date_of_birth, amount_due):
        student = Student.query.filter_by(studentid= student_id).first()
        student.first_name = first_name
        student.last_name = last_name
        student.date_of_birth = date_of_birth
        student.amount_due = amount_due
        db.session.commit()
        return first_name
    
    def delete_student(self,student_id):
        Student.query.filter_by(studentid = student_id).delete()
        db.session.commit()
        return "Deleted"

    def get_student(self):
        Student_list = []
        for news in db.session.query(Student).all():
            Student_list.append({'studentid': news.studentid, 'first_name': news.first_name, 'last_name': news.last_name, 
            'date_of_birth': news.date_of_birth, 'amount_due': news.amount_due})
        return Student_list
