from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://qminh:flaskpass@127.0.0.1:3306/myuni"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    class_name = db.Column(db.String(10), unique=False, nullable=False)
    mark = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f"<Student {self.name}, class: {self.class_name}>"

@app.route('/create_tables')
def create_tables():
    db.create_all()
    return "Table create!"

@app.route("/add_student")
def add_student():
    id = request.args.get("id")
    name = request.args.get("name")
    class_name = request.args.get("class_name")
    mark = request.args.get("mark")

    if not id or not name or not class_name or not mark:
        return "Please provide enough info", 400

    new_student = Student(id=int(id), name=name, class_name=class_name, mark=float(mark))
    db.session.add(new_student)
    db.session.commit()

    return f"Student {name} added succesfully!"

# List all of the student
@app.route("/students")
def list_students():
    students = Student.query.all()
    return render_template("listStudents.html", students=students)

@app.route("/update")
def update():
    students = Student.query.filter(Student.mark < 60).all()
    for s in students:
        s.class_name = "Two"
    db.session.commit()
    return "Updated all students having mark below 60 to class Two!"   

@app.route("/group")
def group():
    excellents = Student.query.filter(Student.mark > 75).all()
    goods = Student.query.filter(Student.mark.between(60, 75)).all()
    averages = Student.query.filter(Student.mark < 60).all()

    return render_template("groupStudents.html", excellents=excellents, goods=goods, averages=averages) 