from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators = [DataRequired(), Length(min = 4, max = 20)])
    email = StringField('Email',
                        validators = [DataRequired(), Email()])
    password = PasswordField('Password',
                             validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class OfficeLogin(FlaskForm):
    username = StringField('Username',
                           validators = [DataRequired()])
    password = PasswordField('Password',
                             validators = [DataRequired()])
    submit = SubmitField('Login')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators = [DataRequired(), Length(min = 8, max = 10)])
    password = PasswordField('Password')
    submit = SubmitField('Login')


class StudentInfo:
    student_name = ''
    student_id = ''
    student_level = ''
    student_seat = ''


class QuestionTHForm(FlaskForm):
    age = StringField('อายุ', validators = [DataRequired()])
    phone = StringField('เบอร์โทรศัพท์', validators = [DataRequired()])
    company = StringField('ทำงานให้กับบริษัทฯ โปรดระบุ', validators = [DataRequired()])
    question1 = RadioField('ภายใน 14 วัน ท่านอุณหภูมิเกิน 37.3 องศาฯหรือไม่',
                           choices = [('Yes', 'เกิน'), ('No', 'ไม่เกิน')])
    question2 = RadioField('ท่านมีประวัติเดินทางออกนอกประเทศภายใน 14 วันที่ผ่านมาหรือไม่',
                           choices = [('Yes', 'ใช่'), ('No', 'ไม่ใช่')])
    question3 = RadioField('ท่านมีประวัติการเดินทางไปในสถานที่ประชาชนหนาแน่น ชุมชน หรือมีการรวมกลุ่มคน '
                           'เช่น ตลาดนัด ห้างสรรพสินค้า สถานพยาบาล หรือขนส่งสาธารณะ',
                           choices = [('Yes', 'เกิน'), ('No', 'ไม่เกิน')])
    question4 = RadioField('ท่านหรือบุคคลที่พักอาศัยร่วมบ้านเป็นบุคลากรทางการแพทย์หรือสัมผัส'
                           'ใกล้ชิดผู้ป่วยที่สงสัยติดเชื้อ Covid-19',
                           choices = [('Yes', 'ใช่'), ('No', 'ไม่ใช่')])
    question5 = RadioField('ท่านมีประวัติสัมผัสใกล้ชิดกับชาวต่างชาติหรือนักท่องเที่ยว',
                           choices = [('Yes', 'เกิน'), ('No', 'ไม่เกิน')])
    submit = SubmitField('Submit')
1