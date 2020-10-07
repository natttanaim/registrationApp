import mysql.connector
from flask import Flask, logging

app = Flask(__name__)
app.config['SECRET_KEY'] = '13137a5685deb14119a8bce78825349b'
mydb = mysql.connector.connect(
        host = "rm9-prd-prx01.ident.stamford.edu",
        user = "stamford_accroot",
        password = "wrUna9o!#kVM5FYA",
        database = "stamford_accounts",
        port = "3306"
)
mycursor = mydb.cursor()


class StudentRegistered:
    std_id = ''
    mycursor.execute("UPDATE graduate_students SET register =1 WHERE student_id =%s", (std_id,))
    mydb.commit()

