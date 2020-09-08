from clinica.ext.db import db


class User(db.Model):
    __tablename__= 'users'

    id = db.Column("id",db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True, index=True)
    passwd = db.Column("passwd", db.Unicode)


class Patient(db.Model):
    __tablename__= "patients"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)



class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)

class Exam(db.Model):
    __tablename__ = "exams"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    