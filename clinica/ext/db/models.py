from clinica.ext.db import db


class User(db.Model):
    __tablename__= 'users'

    id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True, index=True)
    password = db.Column("passwd", db.Unicode)

    patient = db.relationship("Patient", backref='user', uselist=False)



class Patient(db.Model):
    __tablename__= "patients"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    cpf = db.Column(db.String(11))
    endereco_1 = db.Column(db.String(100))
    num = db.Column(db.Integer)
    bairro = db.Column(db.String(40))
    cidade = db.Column(db.String(40))
    estado = db.Column(db.String(40))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))



class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)

class Exam(db.Model):
    __tablename__ = "exams"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    