import mysql.connector
from flask import Flask, render_template, flash, redirect, url_for, request
from Flask_blog.forms import RegistrationForm, LoginForm, StudentInfo, QuestionTHForm, OfficeLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = '13137a5685deb14119a8bce78825349b'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login", methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        std_id = request.form['username']
        mydb = mysql.connector.connect(
                host = "graduation.stamford.edu",
                user = "graduati_dbadmin",
                password = "y5wiE&RfprAnyrJS",
                database = "graduati_dbserver",
                port = "3306"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name,student_id,seat_number,registered FROM graduate_students WHERE student_id =%s",
                         (std_id,))
        my_result = mycursor.fetchall()
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        if my_result:
            if my_result[0][3] == 1:
                current_student = StudentInfo
                current_student.student_name = my_result[0][0]
                current_student.student_id = my_result[0][1]
                current_student.student_seat = my_result[0][2]
                return redirect(url_for('success'))
            else:
                current_student = StudentInfo
                current_student.student_name = my_result[0][0]
                current_student.student_id = my_result[0][1]
                current_student.student_seat = my_result[0][2]
                return redirect(url_for('question'))
        else:
            return redirect(url_for('about'))

    return render_template('login.html', title = 'Login', form = form)


@app.route("/office_login", methods = ['POST', 'GET'])
def office_login():
    form = OfficeLogin()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        if username == 'staff' & password == 'admin2020':
            return redirect(url_for('home'))
    return render_template('office_login.html', form = form)


@app.route("/question", methods = ['POST', 'GET'])
def question():
    student_info = StudentInfo
    name = student_info.student_name
    stid = student_info.student_id
    seat = student_info.student_seat
    form = QuestionTHForm()
    if form.validate_on_submit():
        age = request.form['age']
        phone = request.form['phone']
        company = request.form['company']
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']

        # insert question to table
        mydb = mysql.connector.connect(
                host = "graduation.stamford.edu",
                user = "graduati_dbadmin",
                password = "y5wiE&RfprAnyrJS",
                database = "graduati_dbserver",
                port = "3306"
        )
        mycursor = mydb.cursor()
        recordTuple = (stid, stid, name, age, phone, company, question1, question2, question3, question4, question5)
        mySql_insert_query = """INSERT INTO graduate_survey (Id, student_id, name, age, phone, company,
        question1, question2, question3, question4, question5) 
                           VALUES 
                           (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        mycursor.execute(mySql_insert_query, recordTuple)
        mydb.commit()
        # update register status
        mycursor.execute("SELECT MAX(number) FROM graduate_students")
        my_result = mycursor.fetchall()
        maxvalue = my_result[0][0] + 1
        register_number = "STIU-" + str(maxvalue)
        mycursor.execute(
                "UPDATE graduate_students SET registered =1,register_number = %s,number =%s WHERE student_id =%s",
                (register_number, maxvalue, stid,))
        mydb.commit()
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        return render_template('success.html', stid = stid, seat = seat)
    return render_template('question.html', form = form, name = name, stid = stid)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/backoffice")
def backoffice():
    return render_template('backoffice.html')


@app.route("/success")
def success():
    student_info = StudentInfo
    seat = student_info.student_seat
    stid = student_info.student_id
    return render_template('success.html', stid = stid, seat = seat)


@app.route("/seat")
def seat():
    return render_template('seatDisplay.html')


@app.route("/register", methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


if __name__ == '__main__':
    app.run(debug = False)
