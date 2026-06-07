from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "student_management_secret"

students = []


@app.route("/")
def home():
    return render_template("index.html", total_students=len(students))


@app.route("/add-student")
def add_student_page():
    return render_template("add_students.html")


@app.route("/students")
def view_students():
    return render_template("view_students.html", students=students)


@app.route("/add_student", methods=["POST"])
def add_student():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    age = request.form["age"]
    course = request.form["course"]
    gender = request.form["gender"]

    student = {
        "name": name,
        "email": email,
        "phone": phone,
        "age": age,
        "course": course,
        "gender": gender
    }

    students.append(student)

    flash("✅ Student details submitted successfully!")

    return redirect("/add-student")


if __name__ == "__main__":
    app.run(debug=True)