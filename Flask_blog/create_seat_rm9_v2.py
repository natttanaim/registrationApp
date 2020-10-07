# filename:		seatDisplay_RM9.py
# Created date:	Sep 16, 2020
# Last modified:	Sep 16, 2020
# Created by:	Pete

import smtplib
import mysql.connector
from mysql.connector import Error

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connect to MySQL Database of VAN Code website
try:
    '''
    # Connection to Localhost MySQL database
    connection = mysql.connector.connect(host='localhost',
                                         database='graduation_2020',
                                         user='root',
                                         password='')
    '''

    # Connection to RM9 MySQL database
    connection = mysql.connector.connect(host = 'rm9-prd-prx01.ident.stamford.edu',
                                         database = 'stamford_accounts',
                                         user = 'stamford_accroot',
                                         password = 'wrUna9o!#kVM5FYA')

    '''
    # Code to test database connection
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    '''

except Error as e:
    print("Error while connecting to MySQL", e)

# Global variable
check_value = ''
seat_total = 60
row_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


# Function to Query Data
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

    cursor.close()


def extract_queried_data(queried_data):
    # print(f"Queried data = {queried_data}\n")
    # extracted_value = queried_data[2:len(queried_data)-3] # to match with registered value as "Yes" or null
    extracted_value = queried_data[1:len(queried_data) - 2]  # to match with registered value as tinyint (1)
    # extracted_value = queried_data[1:3]
    # print(f"Extracted queried data is {extracted_value}\n")
    return extracted_value


def check_registered(seat_num):
    check_result = ''
    # query_registered = f"SELECT registered FROM registration WHERE seat=\'{seat_num}\';"
    query_registered = f"SELECT registered FROM graduate_students WHERE seat_number=\'{seat_num}\';"  # for RM9 database
    try:
        result = execute_read_query(connection, query_registered)
        # result1 = result[0][0]
        # output_file.write(f"result of {seat_num} = {result}")
        # output_file.write(f"result[0] of {seat_num} = {result[0]}")
        result1 = extract_queried_data(str(result[0]))
        # output_file.write(f"result1 of {seat_num} = {result}")
        # print(f"Seat Number = {seat_num} Registered = {result1}\n")

        # if result1 == 'Yes':
        if result1 == '1':
            check_result = 'checked'
        else:
            check_result = ''

    except IndexError:  # To return the value if seat has not search result
        check_result = ''
    # print("Seat search: Seat cannot be found in the database.\n")

    return check_result


output_filename = "templates/seatDisplay.html"

output_file = open(output_filename, "w")

# Create Key-Value Variables for all seats
row_A = {
    'A1': '', 'A2': '', 'A3': '', 'A4': '', 'A5': '', 'A6': '', 'A7': '', 'A8': '', 'A9': '', 'A10': '', 'A11': '',
    'A12': '', 'A13': '', 'A14': '', 'A15': '', 'A16': '', 'A17': '', 'A18': '', 'A19': '', 'A20': '', 'A21': '',
    'A22': '', 'A23': '', 'A24': '', 'A25': '', 'A26': '', 'A27': '', 'A28': '', 'A29': '', 'A30': '', 'A31': '',
    'A32': '', 'A33': '', 'A34': '', 'A35': '', 'A36': '', 'A37': '', 'A38': '', 'A39': '', 'A40': '', 'A41': '',
    'A42': '', 'A43': '', 'A44': '', 'A45': '', 'A46': '', 'A47': '', 'A48': '', 'A49': '', 'A50': '', 'A51': '',
    'A52': '', 'A53': '', 'A54': '', 'A55': '', 'A56': '', 'A57': '', 'A58': '', 'A59': '', 'A60': ''
}
row_B = {
    'B1': '', 'B2': '', 'B3': '', 'B4': '', 'B5': '', 'B6': '', 'B7': '', 'B8': '', 'B9': '', 'B10': '', 'B11': '',
    'B12': '', 'B13': '', 'B14': '', 'B15': '', 'B16': '', 'B17': '', 'B18': '', 'B19': '', 'B20': '', 'B21': '',
    'B22': '', 'B23': '', 'B24': '', 'B25': '', 'B26': '', 'B27': '', 'B28': '', 'B29': '', 'B30': '', 'B31': '',
    'B32': '', 'B33': '', 'B34': '', 'B35': '', 'B36': '', 'B37': '', 'B38': '', 'B39': '', 'B40': '', 'B41': '',
    'B42': '', 'B43': '', 'B44': '', 'B45': '', 'B46': '', 'B47': '', 'B48': '', 'B49': '', 'B50': '', 'B51': '',
    'B52': '', 'B53': '', 'B54': '', 'B55': '', 'B56': '', 'B57': '', 'B58': '', 'B59': '', 'B60': ''
}
row_C = {
    'C1': '', 'C2': '', 'C3': '', 'C4': '', 'C5': '', 'C6': '', 'C7': '', 'C8': '', 'C9': '', 'C10': '', 'C11': '',
    'C12': '', 'C13': '', 'C14': '', 'C15': '', 'C16': '', 'C17': '', 'C18': '', 'C19': '', 'C20': '', 'C21': '',
    'C22': '', 'C23': '', 'C24': '', 'C25': '', 'C26': '', 'C27': '', 'C28': '', 'C29': '', 'C30': '', 'C31': '',
    'C32': '', 'C33': '', 'C34': '', 'C35': '', 'C36': '', 'C37': '', 'C38': '', 'C39': '', 'C40': '', 'C41': '',
    'C42': '', 'C43': '', 'C44': '', 'C45': '', 'C46': '', 'C47': '', 'C48': '', 'C49': '', 'C50': '', 'C51': '',
    'C52': '', 'C53': '', 'C54': '', 'C55': '', 'C56': '', 'C57': '', 'C58': '', 'C59': '', 'C60': ''
}
row_D = {
    'D1': '', 'D2': '', 'D3': '', 'D4': '', 'D5': '', 'D6': '', 'D7': '', 'D8': '', 'D9': '', 'D10': '', 'D11': '',
    'D12': '', 'D13': '', 'D14': '', 'D15': '', 'D16': '', 'D17': '', 'D18': '', 'D19': '', 'D20': '', 'D21': '',
    'D22': '', 'D23': '', 'D24': '', 'D25': '', 'D26': '', 'D27': '', 'D28': '', 'D29': '', 'D30': '', 'D31': '',
    'D32': '', 'D33': '', 'D34': '', 'D35': '', 'D36': '', 'D37': '', 'D38': '', 'D39': '', 'D40': '', 'D41': '',
    'D42': '', 'D43': '', 'D44': '', 'D45': '', 'D46': '', 'D47': '', 'D48': '', 'D49': '', 'D50': '', 'D51': '',
    'D52': '', 'D53': '', 'D54': '', 'D55': '', 'D56': '', 'D57': '', 'D58': '', 'D59': '', 'D60': ''
}
row_E = {
    'E1': '', 'E2': '', 'E3': '', 'E4': '', 'E5': '', 'E6': '', 'E7': '', 'E8': '', 'E9': '', 'E10': '', 'E11': '',
    'E12': '', 'E13': '', 'E14': '', 'E15': '', 'E16': '', 'E17': '', 'E18': '', 'E19': '', 'E20': '', 'E21': '',
    'E22': '', 'E23': '', 'E24': '', 'E25': '', 'E26': '', 'E27': '', 'E28': '', 'E29': '', 'E30': '', 'E31': '',
    'E32': '', 'E33': '', 'E34': '', 'E35': '', 'E36': '', 'E37': '', 'E38': '', 'E39': '', 'E40': '', 'E41': '',
    'E42': '', 'E43': '', 'E44': '', 'E45': '', 'E46': '', 'E47': '', 'E48': '', 'E49': '', 'E50': '', 'E51': '',
    'E52': '', 'E53': '', 'E54': '', 'E55': '', 'E56': '', 'E57': '', 'E58': '', 'E59': '', 'E60': ''
}
row_F = {
    'F1': '', 'F2': '', 'F3': '', 'F4': '', 'F5': '', 'F6': '', 'F7': '', 'F8': '', 'F9': '', 'F10': '', 'F11': '',
    'F12': '', 'F13': '', 'F14': '', 'F15': '', 'F16': '', 'F17': '', 'F18': '', 'F19': '', 'F20': '', 'F21': '',
    'F22': '', 'F23': '', 'F24': '', 'F25': '', 'F26': '', 'F27': '', 'F28': '', 'F29': '', 'F30': '', 'F31': '',
    'F32': '', 'F33': '', 'F34': '', 'F35': '', 'F36': '', 'F37': '', 'F38': '', 'F39': '', 'F40': '', 'F41': '',
    'F42': '', 'F43': '', 'F44': '', 'F45': '', 'F46': '', 'F47': '', 'F48': '', 'F49': '', 'F50': '', 'F51': '',
    'F52': '', 'F53': '', 'F54': '', 'F55': '', 'F56': '', 'F57': '', 'F58': '', 'F59': '', 'F60': ''
}
row_G = {
    'G1': '', 'G2': '', 'G3': '', 'G4': '', 'G5': '', 'G6': '', 'G7': '', 'G8': '', 'G9': '', 'G10': '', 'G11': '',
    'G12': '', 'G13': '', 'G14': '', 'G15': '', 'G16': '', 'G17': '', 'G18': '', 'G19': '', 'G20': '', 'G21': '',
    'G22': '', 'G23': '', 'G24': '', 'G25': '', 'G26': '', 'G27': '', 'G28': '', 'G29': '', 'G30': '', 'G31': '',
    'G32': '', 'G33': '', 'G34': '', 'G35': '', 'G36': '', 'G37': '', 'G38': '', 'G39': '', 'G40': '', 'G41': '',
    'G42': '', 'G43': '', 'G44': '', 'G45': '', 'G46': '', 'G47': '', 'G48': '', 'G49': '', 'G50': '', 'G51': '',
    'G52': '', 'G53': '', 'G54': '', 'G55': '', 'G56': '', 'G57': '', 'G58': '', 'G59': '', 'G60': ''
}
row_H = {
    'H1': '', 'H2': '', 'H3': '', 'H4': '', 'H5': '', 'H6': '', 'H7': '', 'H8': '', 'H9': '', 'H10': '', 'H11': '',
    'H12': '', 'H13': '', 'H14': '', 'H15': '', 'H16': '', 'H17': '', 'H18': '', 'H19': '', 'H20': '', 'H21': '',
    'H22': '', 'H23': '', 'H24': '', 'H25': '', 'H26': '', 'H27': '', 'H28': '', 'H29': '', 'H30': '', 'H31': '',
    'H32': '', 'H33': '', 'H34': '', 'H35': '', 'H36': '', 'H37': '', 'H38': '', 'H39': '', 'H40': '', 'H41': '',
    'H42': '', 'H43': '', 'H44': '', 'H45': '', 'H46': '', 'H47': '', 'H48': '', 'H49': '', 'H50': '', 'H51': '',
    'H52': '', 'H53': '', 'H54': '', 'H55': '', 'H56': '', 'H57': '', 'H58': '', 'H59': '', 'H60': ''
}
row_I = {
    'I1': '', 'I2': '', 'I3': '', 'I4': '', 'I5': '', 'I6': '', 'I7': '', 'I8': '', 'I9': '', 'I10': '', 'I11': '',
    'I12': '', 'I13': '', 'I14': '', 'I15': '', 'I16': '', 'I17': '', 'I18': '', 'I19': '', 'I20': '', 'I21': '',
    'I22': '', 'I23': '', 'I24': '', 'I25': '', 'I26': '', 'I27': '', 'I28': '', 'I29': '', 'I30': '', 'I31': '',
    'I32': '', 'I33': '', 'I34': '', 'I35': '', 'I36': '', 'I37': '', 'I38': '', 'I39': '', 'I40': '', 'I41': '',
    'I42': '', 'I43': '', 'I44': '', 'I45': '', 'I46': '', 'I47': '', 'I48': '', 'I49': '', 'I50': '', 'I51': '',
    'I52': '', 'I53': '', 'I54': '', 'I55': '', 'I56': '', 'I57': '', 'I58': '', 'I59': '', 'I60': ''
}
row_J = {
    'J1': '', 'J2': '', 'J3': '', 'J4': '', 'J5': '', 'J6': '', 'J7': '', 'J8': '', 'J9': '', 'J10': '', 'J11': '',
    'J12': '', 'J13': '', 'J14': '', 'J15': '', 'J16': '', 'J17': '', 'J18': '', 'J19': '', 'J20': '', 'J21': '',
    'J22': '', 'J23': '', 'J24': '', 'J25': '', 'J26': '', 'J27': '', 'J28': '', 'J29': '', 'J30': '', 'J31': '',
    'J32': '', 'J33': '', 'J34': '', 'J35': '', 'J36': '', 'J37': '', 'J38': '', 'J39': '', 'J40': '', 'J41': '',
    'J42': '', 'J43': '', 'J44': '', 'J45': '', 'J46': '', 'J47': '', 'J48': '', 'J49': '', 'J50': '', 'J51': '',
    'J52': '', 'J53': '', 'J54': '', 'J55': '', 'J56': '', 'J57': '', 'J58': '', 'J59': '', 'J60': ''
}

# Seat Check-in checking process - query from the database
row_group = ['row_A', 'row_B', 'row_C', 'row_D', 'row_E', 'row_F', 'row_G', 'row_H', 'row_I', 'row_J']
'''
for row in row_group:
	for index in range (seat_total):
		row[""] = check_registered(row.keys(index))
'''

for key, value in row_A.items():
    row_A[key] = check_registered(key)

for key, value in row_B.items():
    row_B[key] = check_registered(key)

for key, value in row_C.items():
    row_C[key] = check_registered(key)

for key, value in row_D.items():
    row_D[key] = check_registered(key)

for key, value in row_E.items():
    row_E[key] = check_registered(key)

for key, value in row_F.items():
    row_F[key] = check_registered(key)

for key, value in row_G.items():
    row_G[key] = check_registered(key)

for key, value in row_H.items():
    row_H[key] = check_registered(key)

for key, value in row_I.items():
    row_I[key] = check_registered(key)

for key, value in row_J.items():
    row_J[key] = check_registered(key)

# Just to check dictionary - key-value pairs
'''
print(f"Row_A = {row_A.items()}\n")
print(f"Row_B = {row_B.items()}\n")
print(f"Row_C = {row_C.items()}\n")
print(f"Row_D = {row_D.items()}\n")
print(f"Row_E = {row_E.items()}\n")
print(f"Row_F = {row_F.items()}\n")
print(f"Row_G = {row_G.items()}\n")
print(f"Row_H = {row_H.items()}\n")
print(f"Row_I = {row_I.items()}\n")
print(f"Row_J = {row_J.items()}\n")
'''

# write html output file for seat display
# create HTML Top part
output_file.write('''
<html>
	<head>
		<!-- <link rel="stylesheet" href="style.css"> -->
		<title>Graduation 2020 Seat Display</title>
		
		<script type = "text/JavaScript">
         <!--
            function AutoRefresh( t ) {
               setTimeout("location.reload(true);", t);
            }
         //-->
      </script>
	</head>
	
	<style>
      .img-container {
        text-align: center;
      }
    </style>
    

	<body onload = "JavaScript:AutoRefresh(5000);">
		<h3 style="font-family:Courier New; color:2D75E3">Seat Display</h3>
		
		
		<div class="img-container"> <!-- Block parent element -->
			<img src="stage1.png" alt="Stage">
    	</div>

    	<br><br>

		<form action="">

''')

# Create middle part of HTML -- Checkboxes
output_file.write(f'''

<label style="font-family:'Courier New'">[A1-A60]</label>
<input type="checkbox" id="A1" name="A1" value="A1" {row_A['A1']}><input type="checkbox" id="A2" name="A2" value="A2" {row_A['A2']}><input type="checkbox" id="A3" name="A3" value="A3" {row_A['A3']}><input type="checkbox" id="A4" name="A4" value="A4" {row_A['A4']}><input type="checkbox" id="A5" name="A5" value="A5" {row_A['A5']}><input type="checkbox" id="A6" name="A6" value="A6" {row_A['A6']}><input type="checkbox" id="A7" name="A7" value="A7" {row_A['A7']}><input type="checkbox" id="A8" name="A8" value="A8" {row_A['A8']}><input type="checkbox" id="A9" name="A9" value="A9" {row_A['A9']}><input type="checkbox" id="A10" name="A10" value="A10" {row_A['A10']}><input type="checkbox" id="A11" name="A11" value="A11" {row_A['A11']}><input type="checkbox" id="A12" name="A12" value="A12" {row_A['A12']}><input type="checkbox" id="A13" name="A13" value="A13" {row_A['A13']}><input type="checkbox" id="A14" name="A14" value="A14" {row_A['A14']}><input type="checkbox" id="A15" name="A15" value="A15" {row_A['A15']}><input type="checkbox" id="A16" name="A16" value="A16" {row_A['A16']}><input type="checkbox" id="A17" name="A17" value="A17" {row_A['A17']}><input type="checkbox" id="A18" name="A18" value="A18" {row_A['A18']}><input type="checkbox" id="A19" name="A19" value="A19" {row_A['A19']}><input type="checkbox" id="A20" name="A20" value="A20" {row_A['A20']}><input type="checkbox" id="A21" name="A21" value="A21" {row_A['A21']}><input type="checkbox" id="A22" name="A22" value="A22" {row_A['A22']}><input type="checkbox" id="A23" name="A23" value="A23" {row_A['A23']}><input type="checkbox" id="A24" name="A24" value="A24" {row_A['A24']}><input type="checkbox" id="A25" name="A25" value="A25" {row_A['A25']}><input type="checkbox" id="A26" name="A26" value="A26" {row_A['A26']}><input type="checkbox" id="A27" name="A27" value="A27" {row_A['A27']}><input type="checkbox" id="A28" name="A28" value="A28" {row_A['A28']}><input type="checkbox" id="A29" name="A29" value="A29" {row_A['A29']}><input type="checkbox" id="A30" name="A30" value="A30" {row_A['A30']}>&emsp;&emsp;<input type="checkbox" id="A31" name="A31" value="A31" {row_A['A31']}><input type="checkbox" id="A32" name="A32" value="A32" {row_A['A32']}><input type="checkbox" id="A33" name="A33" value="A33" {row_A['A33']}><input type="checkbox" id="A34" name="A34" value="A34" {row_A['A34']}><input type="checkbox" id="A35" name="A35" value="A35" {row_A['A35']}><input type="checkbox" id="A36" name="A36" value="A36" {row_A['A36']}><input type="checkbox" id="A37" name="A37" value="A37" {row_A['A37']}><input type="checkbox" id="A38" name="A38" value="A38" {row_A['A38']}><input type="checkbox" id="A39" name="A39" value="A39" {row_A['A39']}><input type="checkbox" id="A40" name="A40" value="A40" {row_A['A40']}><input type="checkbox" id="A41" name="A41" value="A41" {row_A['A41']}><input type="checkbox" id="A42" name="A42" value="A42" {row_A['A42']}><input type="checkbox" id="A43" name="A43" value="A43" {row_A['A43']}><input type="checkbox" id="A44" name="A44" value="A44" {row_A['A44']}><input type="checkbox" id="A45" name="A45" value="A45" {row_A['A45']}><input type="checkbox" id="A46" name="A46" value="A46" {row_A['A46']}><input type="checkbox" id="A47" name="A47" value="A47" {row_A['A47']}><input type="checkbox" id="A48" name="A48" value="A48" {row_A['A48']}><input type="checkbox" id="A49" name="A49" value="A49" {row_A['A49']}><input type="checkbox" id="A50" name="A50" value="A50" {row_A['A50']}><input type="checkbox" id="A51" name="A51" value="A51" {row_A['A51']}><input type="checkbox" id="A52" name="A52" value="A52" {row_A['A52']}><input type="checkbox" id="A53" name="A53" value="A53" {row_A['A53']}><input type="checkbox" id="A54" name="A54" value="A54" {row_A['A54']}><input type="checkbox" id="A55" name="A55" value="A55" {row_A['A55']}><input type="checkbox" id="A56" name="A56" value="A56" {row_A['A56']}><input type="checkbox" id="A57" name="A57" value="A57" {row_A['A57']}><input type="checkbox" id="A58" name="A58" value="A58" {row_A['A58']}><input type="checkbox" id="A59" name="A59" value="A59" {row_A['A59']}><input type="checkbox" id="A60" name="A60" value="A60" {row_A['A60']}><br><br>
<label style="font-family:'Courier New'">[B1-B60]</label>
<input type="checkbox" id="B1" name="B1" value="B1" {row_B['B1']}><input type="checkbox" id="B2" name="B2" value="B2" {row_B['B2']}><input type="checkbox" id="B3" name="B3" value="B3" {row_B['B3']}><input type="checkbox" id="B4" name="B4" value="B4" {row_B['B4']}><input type="checkbox" id="B5" name="B5" value="B5" {row_B['B5']}><input type="checkbox" id="B6" name="B6" value="B6" {row_B['B6']}><input type="checkbox" id="B7" name="B7" value="B7" {row_B['B7']}><input type="checkbox" id="B8" name="B8" value="B8" {row_B['B8']}><input type="checkbox" id="B9" name="B9" value="B9" {row_B['B9']}><input type="checkbox" id="B10" name="B10" value="B10" {row_B['B10']}><input type="checkbox" id="B11" name="B11" value="B11" {row_B['B11']}><input type="checkbox" id="B12" name="B12" value="B12" {row_B['B12']}><input type="checkbox" id="B13" name="B13" value="B13" {row_B['B13']}><input type="checkbox" id="B14" name="B14" value="B14" {row_B['B14']}><input type="checkbox" id="B15" name="B15" value="B15" {row_B['B15']}><input type="checkbox" id="B16" name="B16" value="B16" {row_B['B16']}><input type="checkbox" id="B17" name="B17" value="B17" {row_B['B17']}><input type="checkbox" id="B18" name="B18" value="B18" {row_B['B18']}><input type="checkbox" id="B19" name="B19" value="B19" {row_B['B19']}><input type="checkbox" id="B20" name="B20" value="B20" {row_B['B20']}><input type="checkbox" id="B21" name="B21" value="B21" {row_B['B21']}><input type="checkbox" id="B22" name="B22" value="B22" {row_B['B22']}><input type="checkbox" id="B23" name="B23" value="B23" {row_B['B23']}><input type="checkbox" id="B24" name="B24" value="B24" {row_B['B24']}><input type="checkbox" id="B25" name="B25" value="B25" {row_B['B25']}><input type="checkbox" id="B26" name="B26" value="B26" {row_B['B26']}><input type="checkbox" id="B27" name="B27" value="B27" {row_B['B27']}><input type="checkbox" id="B28" name="B28" value="B28" {row_B['B28']}><input type="checkbox" id="B29" name="B29" value="B29" {row_B['B29']}><input type="checkbox" id="B30" name="B30" value="B30" {row_B['B30']}>&emsp;&emsp;<input type="checkbox" id="B31" name="B31" value="B31" {row_B['B31']}><input type="checkbox" id="B32" name="B32" value="B32" {row_B['B32']}><input type="checkbox" id="B33" name="B33" value="B33" {row_B['B33']}><input type="checkbox" id="B34" name="B34" value="B34" {row_B['B34']}><input type="checkbox" id="B35" name="B35" value="B35" {row_B['B35']}><input type="checkbox" id="B36" name="B36" value="B36" {row_B['B36']}><input type="checkbox" id="B37" name="B37" value="B37" {row_B['B37']}><input type="checkbox" id="B38" name="B38" value="B38" {row_B['B38']}><input type="checkbox" id="B39" name="B39" value="B39" {row_B['B39']}><input type="checkbox" id="B40" name="B40" value="B40" {row_B['B40']}><input type="checkbox" id="B41" name="B41" value="B41" {row_B['B41']}><input type="checkbox" id="B42" name="B42" value="B42" {row_B['B42']}><input type="checkbox" id="B43" name="B43" value="B43" {row_B['B43']}><input type="checkbox" id="B44" name="B44" value="B44" {row_B['B44']}><input type="checkbox" id="B45" name="B45" value="B45" {row_B['B45']}><input type="checkbox" id="B46" name="B46" value="B46" {row_B['B46']}><input type="checkbox" id="B47" name="B47" value="B47" {row_B['B47']}><input type="checkbox" id="B48" name="B48" value="B48" {row_B['B48']}><input type="checkbox" id="B49" name="B49" value="B49" {row_B['B49']}><input type="checkbox" id="B50" name="B50" value="B50" {row_B['B50']}><input type="checkbox" id="B51" name="B51" value="B51" {row_B['B51']}><input type="checkbox" id="B52" name="B52" value="B52" {row_B['B52']}><input type="checkbox" id="B53" name="B53" value="B53" {row_B['B53']}><input type="checkbox" id="B54" name="B54" value="B54" {row_B['B54']}><input type="checkbox" id="B55" name="B55" value="B55" {row_B['B55']}><input type="checkbox" id="B56" name="B56" value="B56" {row_B['B56']}><input type="checkbox" id="B57" name="B57" value="B57" {row_B['B57']}><input type="checkbox" id="B58" name="B58" value="B58" {row_B['B58']}><input type="checkbox" id="B59" name="B59" value="B59" {row_B['B59']}><input type="checkbox" id="B60" name="B60" value="B60" {row_B['B60']}><br><br>
<label style="font-family:'Courier New'">[C1-C60]</label>
<input type="checkbox" id="C1" name="C1" value="C1" {row_C['C1']}><input type="checkbox" id="C2" name="C2" value="C2" {row_C['C2']}><input type="checkbox" id="C3" name="C3" value="C3" {row_C['C3']}><input type="checkbox" id="C4" name="C4" value="C4" {row_C['C4']}><input type="checkbox" id="C5" name="C5" value="C5" {row_C['C5']}><input type="checkbox" id="C6" name="C6" value="C6" {row_C['C6']}><input type="checkbox" id="C7" name="C7" value="C7" {row_C['C7']}><input type="checkbox" id="C8" name="C8" value="C8" {row_C['C8']}><input type="checkbox" id="C9" name="C9" value="C9" {row_C['C9']}><input type="checkbox" id="C10" name="C10" value="C10" {row_C['C10']}><input type="checkbox" id="C11" name="C11" value="C11" {row_C['C11']}><input type="checkbox" id="C12" name="C12" value="C12" {row_C['C12']}><input type="checkbox" id="C13" name="C13" value="C13" {row_C['C13']}><input type="checkbox" id="C14" name="C14" value="C14" {row_C['C14']}><input type="checkbox" id="C15" name="C15" value="C15" {row_C['C15']}><input type="checkbox" id="C16" name="C16" value="C16" {row_C['C16']}><input type="checkbox" id="C17" name="C17" value="C17" {row_C['C17']}><input type="checkbox" id="C18" name="C18" value="C18" {row_C['C18']}><input type="checkbox" id="C19" name="C19" value="C19" {row_C['C19']}><input type="checkbox" id="C20" name="C20" value="C20" {row_C['C20']}><input type="checkbox" id="C21" name="C21" value="C21" {row_C['C21']}><input type="checkbox" id="C22" name="C22" value="C22" {row_C['C22']}><input type="checkbox" id="C23" name="C23" value="C23" {row_C['C23']}><input type="checkbox" id="C24" name="C24" value="C24" {row_C['C24']}><input type="checkbox" id="C25" name="C25" value="C25" {row_C['C25']}><input type="checkbox" id="C26" name="C26" value="C26" {row_C['C26']}><input type="checkbox" id="C27" name="C27" value="C27" {row_C['C27']}><input type="checkbox" id="C28" name="C28" value="C28" {row_C['C28']}><input type="checkbox" id="C29" name="C29" value="C29" {row_C['C29']}><input type="checkbox" id="C30" name="C30" value="C30" {row_C['C30']}>&emsp;&emsp;<input type="checkbox" id="C31" name="C31" value="C31" {row_C['C31']}><input type="checkbox" id="C32" name="C32" value="C32" {row_C['C32']}><input type="checkbox" id="C33" name="C33" value="C33" {row_C['C33']}><input type="checkbox" id="C34" name="C34" value="C34" {row_C['C34']}><input type="checkbox" id="C35" name="C35" value="C35" {row_C['C35']}><input type="checkbox" id="C36" name="C36" value="C36" {row_C['C36']}><input type="checkbox" id="C37" name="C37" value="C37" {row_C['C37']}><input type="checkbox" id="C38" name="C38" value="C38" {row_C['C38']}><input type="checkbox" id="C39" name="C39" value="C39" {row_C['C39']}><input type="checkbox" id="C40" name="C40" value="C40" {row_C['C40']}><input type="checkbox" id="C41" name="C41" value="C41" {row_C['C41']}><input type="checkbox" id="C42" name="C42" value="C42" {row_C['C42']}><input type="checkbox" id="C43" name="C43" value="C43" {row_C['C43']}><input type="checkbox" id="C44" name="C44" value="C44" {row_C['C44']}><input type="checkbox" id="C45" name="C45" value="C45" {row_C['C45']}><input type="checkbox" id="C46" name="C46" value="C46" {row_C['C46']}><input type="checkbox" id="C47" name="C47" value="C47" {row_C['C47']}><input type="checkbox" id="C48" name="C48" value="C48" {row_C['C48']}><input type="checkbox" id="C49" name="C49" value="C49" {row_C['C49']}><input type="checkbox" id="C50" name="C50" value="C50" {row_C['C50']}><input type="checkbox" id="C51" name="C51" value="C51" {row_C['C51']}><input type="checkbox" id="C52" name="C52" value="C52" {row_C['C52']}><input type="checkbox" id="C53" name="C53" value="C53" {row_C['C53']}><input type="checkbox" id="C54" name="C54" value="C54" {row_C['C54']}><input type="checkbox" id="C55" name="C55" value="C55" {row_C['C55']}><input type="checkbox" id="C56" name="C56" value="C56" {row_C['C56']}><input type="checkbox" id="C57" name="C57" value="C57" {row_C['C57']}><input type="checkbox" id="C58" name="C58" value="C58" {row_C['C58']}><input type="checkbox" id="C59" name="C59" value="C59" {row_C['C59']}><input type="checkbox" id="C60" name="C60" value="C60" {row_C['C60']}><br><br>
<label style="font-family:'Courier New'">[D1-D60]</label>
<input type="checkbox" id="D1" name="D1" value="D1" {row_D['D1']}><input type="checkbox" id="D2" name="D2" value="D2" {row_D['D2']}><input type="checkbox" id="D3" name="D3" value="D3" {row_D['D3']}><input type="checkbox" id="D4" name="D4" value="D4" {row_D['D4']}><input type="checkbox" id="D5" name="D5" value="D5" {row_D['D5']}><input type="checkbox" id="D6" name="D6" value="D6" {row_D['D6']}><input type="checkbox" id="D7" name="D7" value="D7" {row_D['D7']}><input type="checkbox" id="D8" name="D8" value="D8" {row_D['D8']}><input type="checkbox" id="D9" name="D9" value="D9" {row_D['D9']}><input type="checkbox" id="D10" name="D10" value="D10" {row_D['D10']}><input type="checkbox" id="D11" name="D11" value="D11" {row_D['D11']}><input type="checkbox" id="D12" name="D12" value="D12" {row_D['D12']}><input type="checkbox" id="D13" name="D13" value="D13" {row_D['D13']}><input type="checkbox" id="D14" name="D14" value="D14" {row_D['D14']}><input type="checkbox" id="D15" name="D15" value="D15" {row_D['D15']}><input type="checkbox" id="D16" name="D16" value="D16" {row_D['D16']}><input type="checkbox" id="D17" name="D17" value="D17" {row_D['D17']}><input type="checkbox" id="D18" name="D18" value="D18" {row_D['D18']}><input type="checkbox" id="D19" name="D19" value="D19" {row_D['D19']}><input type="checkbox" id="D20" name="D20" value="D20" {row_D['D20']}><input type="checkbox" id="D21" name="D21" value="D21" {row_D['D21']}><input type="checkbox" id="D22" name="D22" value="D22" {row_D['D22']}><input type="checkbox" id="D23" name="D23" value="D23" {row_D['D23']}><input type="checkbox" id="D24" name="D24" value="D24" {row_D['D24']}><input type="checkbox" id="D25" name="D25" value="D25" {row_D['D25']}><input type="checkbox" id="D26" name="D26" value="D26" {row_D['D26']}><input type="checkbox" id="D27" name="D27" value="D27" {row_D['D27']}><input type="checkbox" id="D28" name="D28" value="D28" {row_D['D28']}><input type="checkbox" id="D29" name="D29" value="D29" {row_D['D29']}><input type="checkbox" id="D30" name="D30" value="D30" {row_D['D30']}>&emsp;&emsp;<input type="checkbox" id="D31" name="D31" value="D31" {row_D['D31']}><input type="checkbox" id="D32" name="D32" value="D32" {row_D['D32']}><input type="checkbox" id="D33" name="D33" value="D33" {row_D['D33']}><input type="checkbox" id="D34" name="D34" value="D34" {row_D['D34']}><input type="checkbox" id="D35" name="D35" value="D35" {row_D['D35']}><input type="checkbox" id="D36" name="D36" value="D36" {row_D['D36']}><input type="checkbox" id="D37" name="D37" value="D37" {row_D['D37']}><input type="checkbox" id="D38" name="D38" value="D38" {row_D['D38']}><input type="checkbox" id="D39" name="D39" value="D39" {row_D['D39']}><input type="checkbox" id="D40" name="D40" value="D40" {row_D['D40']}><input type="checkbox" id="D41" name="D41" value="D41" {row_D['D41']}><input type="checkbox" id="D42" name="D42" value="D42" {row_D['D42']}><input type="checkbox" id="D43" name="D43" value="D43" {row_D['D43']}><input type="checkbox" id="D44" name="D44" value="D44" {row_D['D44']}><input type="checkbox" id="D45" name="D45" value="D45" {row_D['D45']}><input type="checkbox" id="D46" name="D46" value="D46" {row_D['D46']}><input type="checkbox" id="D47" name="D47" value="D47" {row_D['D47']}><input type="checkbox" id="D48" name="D48" value="D48" {row_D['D48']}><input type="checkbox" id="D49" name="D49" value="D49" {row_D['D49']}><input type="checkbox" id="D50" name="D50" value="D50" {row_D['D50']}><input type="checkbox" id="D51" name="D51" value="D51" {row_D['D51']}><input type="checkbox" id="D52" name="D52" value="D52" {row_D['D52']}><input type="checkbox" id="D53" name="D53" value="D53" {row_D['D53']}><input type="checkbox" id="D54" name="D54" value="D54" {row_D['D54']}><input type="checkbox" id="D55" name="D55" value="D55" {row_D['D55']}><input type="checkbox" id="D56" name="D56" value="D56" {row_D['D56']}><input type="checkbox" id="D57" name="D57" value="D57" {row_D['D57']}><input type="checkbox" id="D58" name="D58" value="D58" {row_D['D58']}><input type="checkbox" id="D59" name="D59" value="D59" {row_D['D59']}><input type="checkbox" id="D60" name="D60" value="D60" {row_D['D60']}><br><br>
<label style="font-family:'Courier New'">[E1-E60]</label>
<input type="checkbox" id="E1" name="E1" value="E1" {row_E['E1']}><input type="checkbox" id="E2" name="E2" value="E2" {row_E['E2']}><input type="checkbox" id="E3" name="E3" value="E3" {row_E['E3']}><input type="checkbox" id="E4" name="E4" value="E4" {row_E['E4']}><input type="checkbox" id="E5" name="E5" value="E5" {row_E['E5']}><input type="checkbox" id="E6" name="E6" value="E6" {row_E['E6']}><input type="checkbox" id="E7" name="E7" value="E7" {row_E['E7']}><input type="checkbox" id="E8" name="E8" value="E8" {row_E['E8']}><input type="checkbox" id="E9" name="E9" value="E9" {row_E['E9']}><input type="checkbox" id="E10" name="E10" value="E10" {row_E['E10']}><input type="checkbox" id="E11" name="E11" value="E11" {row_E['E11']}><input type="checkbox" id="E12" name="E12" value="E12" {row_E['E12']}><input type="checkbox" id="E13" name="E13" value="E13" {row_E['E13']}><input type="checkbox" id="E14" name="E14" value="E14" {row_E['E14']}><input type="checkbox" id="E15" name="E15" value="E15" {row_E['E15']}><input type="checkbox" id="E16" name="E16" value="E16" {row_E['E16']}><input type="checkbox" id="E17" name="E17" value="E17" {row_E['E17']}><input type="checkbox" id="E18" name="E18" value="E18" {row_E['E18']}><input type="checkbox" id="E19" name="E19" value="E19" {row_E['E19']}><input type="checkbox" id="E20" name="E20" value="E20" {row_E['E20']}><input type="checkbox" id="E21" name="E21" value="E21" {row_E['E21']}><input type="checkbox" id="E22" name="E22" value="E22" {row_E['E22']}><input type="checkbox" id="E23" name="E23" value="E23" {row_E['E23']}><input type="checkbox" id="E24" name="E24" value="E24" {row_E['E24']}><input type="checkbox" id="E25" name="E25" value="E25" {row_E['E25']}><input type="checkbox" id="E26" name="E26" value="E26" {row_E['E26']}><input type="checkbox" id="E27" name="E27" value="E27" {row_E['E27']}><input type="checkbox" id="E28" name="E28" value="E28" {row_E['E28']}><input type="checkbox" id="E29" name="E29" value="E29" {row_E['E29']}><input type="checkbox" id="E30" name="E30" value="E30" {row_E['E30']}>&emsp;&emsp;<input type="checkbox" id="E31" name="E31" value="E31" {row_E['E31']}><input type="checkbox" id="E32" name="E32" value="E32" {row_E['E32']}><input type="checkbox" id="E33" name="E33" value="E33" {row_E['E33']}><input type="checkbox" id="E34" name="E34" value="E34" {row_E['E34']}><input type="checkbox" id="E35" name="E35" value="E35" {row_E['E35']}><input type="checkbox" id="E36" name="E36" value="E36" {row_E['E36']}><input type="checkbox" id="E37" name="E37" value="E37" {row_E['E37']}><input type="checkbox" id="E38" name="E38" value="E38" {row_E['E38']}><input type="checkbox" id="E39" name="E39" value="E39" {row_E['E39']}><input type="checkbox" id="E40" name="E40" value="E40" {row_E['E40']}><input type="checkbox" id="E41" name="E41" value="E41" {row_E['E41']}><input type="checkbox" id="E42" name="E42" value="E42" {row_E['E42']}><input type="checkbox" id="E43" name="E43" value="E43" {row_E['E43']}><input type="checkbox" id="E44" name="E44" value="E44" {row_E['E44']}><input type="checkbox" id="E45" name="E45" value="E45" {row_E['E45']}><input type="checkbox" id="E46" name="E46" value="E46" {row_E['E46']}><input type="checkbox" id="E47" name="E47" value="E47" {row_E['E47']}><input type="checkbox" id="E48" name="E48" value="E48" {row_E['E48']}><input type="checkbox" id="E49" name="E49" value="E49" {row_E['E49']}><input type="checkbox" id="E50" name="E50" value="E50" {row_E['E50']}><input type="checkbox" id="E51" name="E51" value="E51" {row_E['E51']}><input type="checkbox" id="E52" name="E52" value="E52" {row_E['E52']}><input type="checkbox" id="E53" name="E53" value="E53" {row_E['E53']}><input type="checkbox" id="E54" name="E54" value="E54" {row_E['E54']}><input type="checkbox" id="E55" name="E55" value="E55" {row_E['E55']}><input type="checkbox" id="E56" name="E56" value="E56" {row_E['E56']}><input type="checkbox" id="E57" name="E57" value="E57" {row_E['E57']}><input type="checkbox" id="E58" name="E58" value="E58" {row_E['E58']}><input type="checkbox" id="E59" name="E59" value="E59" {row_E['E59']}><input type="checkbox" id="E60" name="E60" value="E60" {row_E['E60']}><br><br>
<label style="font-family:'Courier New'">[F1-F60]</label>
<input type="checkbox" id="F1" name="F1" value="F1" {row_F['F1']}><input type="checkbox" id="F2" name="F2" value="F2" {row_F['F2']}><input type="checkbox" id="F3" name="F3" value="F3" {row_F['F3']}><input type="checkbox" id="F4" name="F4" value="F4" {row_F['F4']}><input type="checkbox" id="F5" name="F5" value="F5" {row_F['F5']}><input type="checkbox" id="F6" name="F6" value="F6" {row_F['F6']}><input type="checkbox" id="F7" name="F7" value="F7" {row_F['F7']}><input type="checkbox" id="F8" name="F8" value="F8" {row_F['F8']}><input type="checkbox" id="F9" name="F9" value="F9" {row_F['F9']}><input type="checkbox" id="F10" name="F10" value="F10" {row_F['F10']}><input type="checkbox" id="F11" name="F11" value="F11" {row_F['F11']}><input type="checkbox" id="F12" name="F12" value="F12" {row_F['F12']}><input type="checkbox" id="F13" name="F13" value="F13" {row_F['F13']}><input type="checkbox" id="F14" name="F14" value="F14" {row_F['F14']}><input type="checkbox" id="F15" name="F15" value="F15" {row_F['F15']}><input type="checkbox" id="F16" name="F16" value="F16" {row_F['F16']}><input type="checkbox" id="F17" name="F17" value="F17" {row_F['F17']}><input type="checkbox" id="F18" name="F18" value="F18" {row_F['F18']}><input type="checkbox" id="F19" name="F19" value="F19" {row_F['F19']}><input type="checkbox" id="F20" name="F20" value="F20" {row_F['F20']}><input type="checkbox" id="F21" name="F21" value="F21" {row_F['F21']}><input type="checkbox" id="F22" name="F22" value="F22" {row_F['F22']}><input type="checkbox" id="F23" name="F23" value="F23" {row_F['F23']}><input type="checkbox" id="F24" name="F24" value="F24" {row_F['F24']}><input type="checkbox" id="F25" name="F25" value="F25" {row_F['F25']}><input type="checkbox" id="F26" name="F26" value="F26" {row_F['F26']}><input type="checkbox" id="F27" name="F27" value="F27" {row_F['F27']}><input type="checkbox" id="F28" name="F28" value="F28" {row_F['F28']}><input type="checkbox" id="F29" name="F29" value="F29" {row_F['F29']}><input type="checkbox" id="F30" name="F30" value="F30" {row_F['F30']}>&emsp;&emsp;<input type="checkbox" id="F31" name="F31" value="F31" {row_F['F31']}><input type="checkbox" id="F32" name="F32" value="F32" {row_F['F32']}><input type="checkbox" id="F33" name="F33" value="F33" {row_F['F33']}><input type="checkbox" id="F34" name="F34" value="F34" {row_F['F34']}><input type="checkbox" id="F35" name="F35" value="F35" {row_F['F35']}><input type="checkbox" id="F36" name="F36" value="F36" {row_F['F36']}><input type="checkbox" id="F37" name="F37" value="F37" {row_F['F37']}><input type="checkbox" id="F38" name="F38" value="F38" {row_F['F38']}><input type="checkbox" id="F39" name="F39" value="F39" {row_F['F39']}><input type="checkbox" id="F40" name="F40" value="F40" {row_F['F40']}><input type="checkbox" id="F41" name="F41" value="F41" {row_F['F41']}><input type="checkbox" id="F42" name="F42" value="F42" {row_F['F42']}><input type="checkbox" id="F43" name="F43" value="F43" {row_F['F43']}><input type="checkbox" id="F44" name="F44" value="F44" {row_F['F44']}><input type="checkbox" id="F45" name="F45" value="F45" {row_F['F45']}><input type="checkbox" id="F46" name="F46" value="F46" {row_F['F46']}><input type="checkbox" id="F47" name="F47" value="F47" {row_F['F47']}><input type="checkbox" id="F48" name="F48" value="F48" {row_F['F48']}><input type="checkbox" id="F49" name="F49" value="F49" {row_F['F49']}><input type="checkbox" id="F50" name="F50" value="F50" {row_F['F50']}><input type="checkbox" id="F51" name="F51" value="F51" {row_F['F51']}><input type="checkbox" id="F52" name="F52" value="F52" {row_F['F52']}><input type="checkbox" id="F53" name="F53" value="F53" {row_F['F53']}><input type="checkbox" id="F54" name="F54" value="F54" {row_F['F54']}><input type="checkbox" id="F55" name="F55" value="F55" {row_F['F55']}><input type="checkbox" id="F56" name="F56" value="F56" {row_F['F56']}><input type="checkbox" id="F57" name="F57" value="F57" {row_F['F57']}><input type="checkbox" id="F58" name="F58" value="F58" {row_F['F58']}><input type="checkbox" id="F59" name="F59" value="F59" {row_F['F59']}><input type="checkbox" id="F60" name="F60" value="F60" {row_F['F60']}><br><br>
<label style="font-family:'Courier New'">[G1-G60]</label>
<input type="checkbox" id="G1" name="G1" value="G1" {row_G['G1']}><input type="checkbox" id="G2" name="G2" value="G2" {row_G['G2']}><input type="checkbox" id="G3" name="G3" value="G3" {row_G['G3']}><input type="checkbox" id="G4" name="G4" value="G4" {row_G['G4']}><input type="checkbox" id="G5" name="G5" value="G5" {row_G['G5']}><input type="checkbox" id="G6" name="G6" value="G6" {row_G['G6']}><input type="checkbox" id="G7" name="G7" value="G7" {row_G['G7']}><input type="checkbox" id="G8" name="G8" value="G8" {row_G['G8']}><input type="checkbox" id="G9" name="G9" value="G9" {row_G['G9']}><input type="checkbox" id="G10" name="G10" value="G10" {row_G['G10']}><input type="checkbox" id="G11" name="G11" value="G11" {row_G['G11']}><input type="checkbox" id="G12" name="G12" value="G12" {row_G['G12']}><input type="checkbox" id="G13" name="G13" value="G13" {row_G['G13']}><input type="checkbox" id="G14" name="G14" value="G14" {row_G['G14']}><input type="checkbox" id="G15" name="G15" value="G15" {row_G['G15']}><input type="checkbox" id="G16" name="G16" value="G16" {row_G['G16']}><input type="checkbox" id="G17" name="G17" value="G17" {row_G['G17']}><input type="checkbox" id="G18" name="G18" value="G18" {row_G['G18']}><input type="checkbox" id="G19" name="G19" value="G19" {row_G['G19']}><input type="checkbox" id="G20" name="G20" value="G20" {row_G['G20']}><input type="checkbox" id="G21" name="G21" value="G21" {row_G['G21']}><input type="checkbox" id="G22" name="G22" value="G22" {row_G['G22']}><input type="checkbox" id="G23" name="G23" value="G23" {row_G['G23']}><input type="checkbox" id="G24" name="G24" value="G24" {row_G['G24']}><input type="checkbox" id="G25" name="G25" value="G25" {row_G['G25']}><input type="checkbox" id="G26" name="G26" value="G26" {row_G['G26']}><input type="checkbox" id="G27" name="G27" value="G27" {row_G['G27']}><input type="checkbox" id="G28" name="G28" value="G28" {row_G['G28']}><input type="checkbox" id="G29" name="G29" value="G29" {row_G['G29']}><input type="checkbox" id="G30" name="G30" value="G30" {row_G['G30']}>&emsp;&emsp;<input type="checkbox" id="G31" name="G31" value="G31" {row_G['G31']}><input type="checkbox" id="G32" name="G32" value="G32" {row_G['G32']}><input type="checkbox" id="G33" name="G33" value="G33" {row_G['G33']}><input type="checkbox" id="G34" name="G34" value="G34" {row_G['G34']}><input type="checkbox" id="G35" name="G35" value="G35" {row_G['G35']}><input type="checkbox" id="G36" name="G36" value="G36" {row_G['G36']}><input type="checkbox" id="G37" name="G37" value="G37" {row_G['G37']}><input type="checkbox" id="G38" name="G38" value="G38" {row_G['G38']}><input type="checkbox" id="G39" name="G39" value="G39" {row_G['G39']}><input type="checkbox" id="G40" name="G40" value="G40" {row_G['G40']}><input type="checkbox" id="G41" name="G41" value="G41" {row_G['G41']}><input type="checkbox" id="G42" name="G42" value="G42" {row_G['G42']}><input type="checkbox" id="G43" name="G43" value="G43" {row_G['G43']}><input type="checkbox" id="G44" name="G44" value="G44" {row_G['G44']}><input type="checkbox" id="G45" name="G45" value="G45" {row_G['G45']}><input type="checkbox" id="G46" name="G46" value="G46" {row_G['G46']}><input type="checkbox" id="G47" name="G47" value="G47" {row_G['G47']}><input type="checkbox" id="G48" name="G48" value="G48" {row_G['G48']}><input type="checkbox" id="G49" name="G49" value="G49" {row_G['G49']}><input type="checkbox" id="G50" name="G50" value="G50" {row_G['G50']}><input type="checkbox" id="G51" name="G51" value="G51" {row_G['G51']}><input type="checkbox" id="G52" name="G52" value="G52" {row_G['G52']}><input type="checkbox" id="G53" name="G53" value="G53" {row_G['G53']}><input type="checkbox" id="G54" name="G54" value="G54" {row_G['G54']}><input type="checkbox" id="G55" name="G55" value="G55" {row_G['G55']}><input type="checkbox" id="G56" name="G56" value="G56" {row_G['G56']}><input type="checkbox" id="G57" name="G57" value="G57" {row_G['G57']}><input type="checkbox" id="G58" name="G58" value="G58" {row_G['G58']}><input type="checkbox" id="G59" name="G59" value="G59" {row_G['G59']}><input type="checkbox" id="G60" name="G60" value="G60" {row_G['G60']}><br><br>
<label style="font-family:'Courier New'">[H1-H60]</label>
<input type="checkbox" id="H1" name="H1" value="H1" {row_H['H1']}><input type="checkbox" id="H2" name="H2" value="H2" {row_H['H2']}><input type="checkbox" id="H3" name="H3" value="H3" {row_H['H3']}><input type="checkbox" id="H4" name="H4" value="H4" {row_H['H4']}><input type="checkbox" id="H5" name="H5" value="H5" {row_H['H5']}><input type="checkbox" id="H6" name="H6" value="H6" {row_H['H6']}><input type="checkbox" id="H7" name="H7" value="H7" {row_H['H7']}><input type="checkbox" id="H8" name="H8" value="H8" {row_H['H8']}><input type="checkbox" id="H9" name="H9" value="H9" {row_H['H9']}><input type="checkbox" id="H10" name="H10" value="H10" {row_H['H10']}><input type="checkbox" id="H11" name="H11" value="H11" {row_H['H11']}><input type="checkbox" id="H12" name="H12" value="H12" {row_H['H12']}><input type="checkbox" id="H13" name="H13" value="H13" {row_H['H13']}><input type="checkbox" id="H14" name="H14" value="H14" {row_H['H14']}><input type="checkbox" id="H15" name="H15" value="H15" {row_H['H15']}><input type="checkbox" id="H16" name="H16" value="H16" {row_H['H16']}><input type="checkbox" id="H17" name="H17" value="H17" {row_H['H17']}><input type="checkbox" id="H18" name="H18" value="H18" {row_H['H18']}><input type="checkbox" id="H19" name="H19" value="H19" {row_H['H19']}><input type="checkbox" id="H20" name="H20" value="H20" {row_H['H20']}><input type="checkbox" id="H21" name="H21" value="H21" {row_H['H21']}><input type="checkbox" id="H22" name="H22" value="H22" {row_H['H22']}><input type="checkbox" id="H23" name="H23" value="H23" {row_H['H23']}><input type="checkbox" id="H24" name="H24" value="H24" {row_H['H24']}><input type="checkbox" id="H25" name="H25" value="H25" {row_H['H25']}><input type="checkbox" id="H26" name="H26" value="H26" {row_H['H26']}><input type="checkbox" id="H27" name="H27" value="H27" {row_H['H27']}><input type="checkbox" id="H28" name="H28" value="H28" {row_H['H28']}><input type="checkbox" id="H29" name="H29" value="H29" {row_H['H29']}><input type="checkbox" id="H30" name="H30" value="H30" {row_H['H30']}>&emsp;&emsp;<input type="checkbox" id="H31" name="H31" value="H31" {row_H['H31']}><input type="checkbox" id="H32" name="H32" value="H32" {row_H['H32']}><input type="checkbox" id="H33" name="H33" value="H33" {row_H['H33']}><input type="checkbox" id="H34" name="H34" value="H34" {row_H['H34']}><input type="checkbox" id="H35" name="H35" value="H35" {row_H['H35']}><input type="checkbox" id="H36" name="H36" value="H36" {row_H['H36']}><input type="checkbox" id="H37" name="H37" value="H37" {row_H['H37']}><input type="checkbox" id="H38" name="H38" value="H38" {row_H['H38']}><input type="checkbox" id="H39" name="H39" value="H39" {row_H['H39']}><input type="checkbox" id="H40" name="H40" value="H40" {row_H['H40']}><input type="checkbox" id="H41" name="H41" value="H41" {row_H['H41']}><input type="checkbox" id="H42" name="H42" value="H42" {row_H['H42']}><input type="checkbox" id="H43" name="H43" value="H43" {row_H['H43']}><input type="checkbox" id="H44" name="H44" value="H44" {row_H['H44']}><input type="checkbox" id="H45" name="H45" value="H45" {row_H['H45']}><input type="checkbox" id="H46" name="H46" value="H46" {row_H['H46']}><input type="checkbox" id="H47" name="H47" value="H47" {row_H['H47']}><input type="checkbox" id="H48" name="H48" value="H48" {row_H['H48']}><input type="checkbox" id="H49" name="H49" value="H49" {row_H['H49']}><input type="checkbox" id="H50" name="H50" value="H50" {row_H['H50']}><input type="checkbox" id="H51" name="H51" value="H51" {row_H['H51']}><input type="checkbox" id="H52" name="H52" value="H52" {row_H['H52']}><input type="checkbox" id="H53" name="H53" value="H53" {row_H['H53']}><input type="checkbox" id="H54" name="H54" value="H54" {row_H['H54']}><input type="checkbox" id="H55" name="H55" value="H55" {row_H['H55']}><input type="checkbox" id="H56" name="H56" value="H56" {row_H['H56']}><input type="checkbox" id="H57" name="H57" value="H57" {row_H['H57']}><input type="checkbox" id="H58" name="H58" value="H58" {row_H['H58']}><input type="checkbox" id="H59" name="H59" value="H59" {row_H['H59']}><input type="checkbox" id="H60" name="H60" value="H60" {row_H['H60']}><br><br>
<label style="font-family:'Courier New'">[I1-I60]</label>
<input type="checkbox" id="I1" name="I1" value="I1" {row_I['I1']}><input type="checkbox" id="I2" name="I2" value="I2" {row_I['I2']}><input type="checkbox" id="I3" name="I3" value="I3" {row_I['I3']}><input type="checkbox" id="I4" name="I4" value="I4" {row_I['I4']}><input type="checkbox" id="I5" name="I5" value="I5" {row_I['I5']}><input type="checkbox" id="I6" name="I6" value="I6" {row_I['I6']}><input type="checkbox" id="I7" name="I7" value="I7" {row_I['I7']}><input type="checkbox" id="I8" name="I8" value="I8" {row_I['I8']}><input type="checkbox" id="I9" name="I9" value="I9" {row_I['I9']}><input type="checkbox" id="I10" name="I10" value="I10" {row_I['I10']}><input type="checkbox" id="I11" name="I11" value="I11" {row_I['I11']}><input type="checkbox" id="I12" name="I12" value="I12" {row_I['I12']}><input type="checkbox" id="I13" name="I13" value="I13" {row_I['I13']}><input type="checkbox" id="I14" name="I14" value="I14" {row_I['I14']}><input type="checkbox" id="I15" name="I15" value="I15" {row_I['I15']}><input type="checkbox" id="I16" name="I16" value="I16" {row_I['I16']}><input type="checkbox" id="I17" name="I17" value="I17" {row_I['I17']}><input type="checkbox" id="I18" name="I18" value="I18" {row_I['I18']}><input type="checkbox" id="I19" name="I19" value="I19" {row_I['I19']}><input type="checkbox" id="I20" name="I20" value="I20" {row_I['I20']}><input type="checkbox" id="I21" name="I21" value="I21" {row_I['I21']}><input type="checkbox" id="I22" name="I22" value="I22" {row_I['I22']}><input type="checkbox" id="I23" name="I23" value="I23" {row_I['I23']}><input type="checkbox" id="I24" name="I24" value="I24" {row_I['I24']}><input type="checkbox" id="I25" name="I25" value="I25" {row_I['I25']}><input type="checkbox" id="I26" name="I26" value="I26" {row_I['I26']}><input type="checkbox" id="I27" name="I27" value="I27" {row_I['I27']}><input type="checkbox" id="I28" name="I28" value="I28" {row_I['I28']}><input type="checkbox" id="I29" name="I29" value="I29" {row_I['I29']}><input type="checkbox" id="I30" name="I30" value="I30" {row_I['I30']}>&emsp;&emsp;<input type="checkbox" id="I31" name="I31" value="I31" {row_I['I31']}><input type="checkbox" id="I32" name="I32" value="I32" {row_I['I32']}><input type="checkbox" id="I33" name="I33" value="I33" {row_I['I33']}><input type="checkbox" id="I34" name="I34" value="I34" {row_I['I34']}><input type="checkbox" id="I35" name="I35" value="I35" {row_I['I35']}><input type="checkbox" id="I36" name="I36" value="I36" {row_I['I36']}><input type="checkbox" id="I37" name="I37" value="I37" {row_I['I37']}><input type="checkbox" id="I38" name="I38" value="I38" {row_I['I38']}><input type="checkbox" id="I39" name="I39" value="I39" {row_I['I39']}><input type="checkbox" id="I40" name="I40" value="I40" {row_I['I40']}><input type="checkbox" id="I41" name="I41" value="I41" {row_I['I41']}><input type="checkbox" id="I42" name="I42" value="I42" {row_I['I42']}><input type="checkbox" id="I43" name="I43" value="I43" {row_I['I43']}><input type="checkbox" id="I44" name="I44" value="I44" {row_I['I44']}><input type="checkbox" id="I45" name="I45" value="I45" {row_I['I45']}><input type="checkbox" id="I46" name="I46" value="I46" {row_I['I46']}><input type="checkbox" id="I47" name="I47" value="I47" {row_I['I47']}><input type="checkbox" id="I48" name="I48" value="I48" {row_I['I48']}><input type="checkbox" id="I49" name="I49" value="I49" {row_I['I49']}><input type="checkbox" id="I50" name="I50" value="I50" {row_I['I50']}><input type="checkbox" id="I51" name="I51" value="I51" {row_I['I51']}><input type="checkbox" id="I52" name="I52" value="I52" {row_I['I52']}><input type="checkbox" id="I53" name="I53" value="I53" {row_I['I53']}><input type="checkbox" id="I54" name="I54" value="I54" {row_I['I54']}><input type="checkbox" id="I55" name="I55" value="I55" {row_I['I55']}><input type="checkbox" id="I56" name="I56" value="I56" {row_I['I56']}><input type="checkbox" id="I57" name="I57" value="I57" {row_I['I57']}><input type="checkbox" id="I58" name="I58" value="I58" {row_I['I58']}><input type="checkbox" id="I59" name="I59" value="I59" {row_I['I59']}><input type="checkbox" id="I60" name="I60" value="I60" {row_I['I60']}><br><br>
<label style="font-family:'Courier New'">[J1-J60]</label>
<input type="checkbox" id="J1" name="J1" value="J1" {row_J['J1']}><input type="checkbox" id="J2" name="J2" value="J2" {row_J['J2']}><input type="checkbox" id="J3" name="J3" value="J3" {row_J['J3']}><input type="checkbox" id="J4" name="J4" value="J4" {row_J['J4']}><input type="checkbox" id="J5" name="J5" value="J5" {row_J['J5']}><input type="checkbox" id="J6" name="J6" value="J6" {row_J['J6']}><input type="checkbox" id="J7" name="J7" value="J7" {row_J['J7']}><input type="checkbox" id="J8" name="J8" value="J8" {row_J['J8']}><input type="checkbox" id="J9" name="J9" value="J9" {row_J['J9']}><input type="checkbox" id="J10" name="J10" value="J10" {row_J['J10']}><input type="checkbox" id="J11" name="J11" value="J11" {row_J['J11']}><input type="checkbox" id="J12" name="J12" value="J12" {row_J['J12']}><input type="checkbox" id="J13" name="J13" value="J13" {row_J['J13']}><input type="checkbox" id="J14" name="J14" value="J14" {row_J['J14']}><input type="checkbox" id="J15" name="J15" value="J15" {row_J['J15']}><input type="checkbox" id="J16" name="J16" value="J16" {row_J['J16']}><input type="checkbox" id="J17" name="J17" value="J17" {row_J['J17']}><input type="checkbox" id="J18" name="J18" value="J18" {row_J['J18']}><input type="checkbox" id="J19" name="J19" value="J19" {row_J['J19']}><input type="checkbox" id="J20" name="J20" value="J20" {row_J['J20']}><input type="checkbox" id="J21" name="J21" value="J21" {row_J['J21']}><input type="checkbox" id="J22" name="J22" value="J22" {row_J['J22']}><input type="checkbox" id="J23" name="J23" value="J23" {row_J['J23']}><input type="checkbox" id="J24" name="J24" value="J24" {row_J['J24']}><input type="checkbox" id="J25" name="J25" value="J25" {row_J['J25']}><input type="checkbox" id="J26" name="J26" value="J26" {row_J['J26']}><input type="checkbox" id="J27" name="J27" value="J27" {row_J['J27']}><input type="checkbox" id="J28" name="J28" value="J28" {row_J['J28']}><input type="checkbox" id="J29" name="J29" value="J29" {row_J['J29']}><input type="checkbox" id="J30" name="J30" value="J30" {row_J['J30']}>&emsp;&emsp;<input type="checkbox" id="J31" name="J31" value="J31" {row_J['J31']}><input type="checkbox" id="J32" name="J32" value="J32" {row_J['J32']}><input type="checkbox" id="J33" name="J33" value="J33" {row_J['J33']}><input type="checkbox" id="J34" name="J34" value="J34" {row_J['J34']}><input type="checkbox" id="J35" name="J35" value="J35" {row_J['J35']}><input type="checkbox" id="J36" name="J36" value="J36" {row_J['J36']}><input type="checkbox" id="J37" name="J37" value="J37" {row_J['J37']}><input type="checkbox" id="J38" name="J38" value="J38" {row_J['J38']}><input type="checkbox" id="J39" name="J39" value="J39" {row_J['J39']}><input type="checkbox" id="J40" name="J40" value="J40" {row_J['J40']}><input type="checkbox" id="J41" name="J41" value="J41" {row_J['J41']}><input type="checkbox" id="J42" name="J42" value="J42" {row_J['J42']}><input type="checkbox" id="J43" name="J43" value="J43" {row_J['J43']}><input type="checkbox" id="J44" name="J44" value="J44" {row_J['J44']}><input type="checkbox" id="J45" name="J45" value="J45" {row_J['J45']}><input type="checkbox" id="J46" name="J46" value="J46" {row_J['J46']}><input type="checkbox" id="J47" name="J47" value="J47" {row_J['J47']}><input type="checkbox" id="J48" name="J48" value="J48" {row_J['J48']}><input type="checkbox" id="J49" name="J49" value="J49" {row_J['J49']}><input type="checkbox" id="J50" name="J50" value="J50" {row_J['J50']}><input type="checkbox" id="J51" name="J51" value="J51" {row_J['J51']}><input type="checkbox" id="J52" name="J52" value="J52" {row_J['J52']}><input type="checkbox" id="J53" name="J53" value="J53" {row_J['J53']}><input type="checkbox" id="J54" name="J54" value="J54" {row_J['J54']}><input type="checkbox" id="J55" name="J55" value="J55" {row_J['J55']}><input type="checkbox" id="J56" name="J56" value="J56" {row_J['J56']}><input type="checkbox" id="J57" name="J57" value="J57" {row_J['J57']}><input type="checkbox" id="J58" name="J58" value="J58" {row_J['J58']}><input type="checkbox" id="J59" name="J59" value="J59" {row_J['J59']}><input type="checkbox" id="J60" name="J60" value="J60" {row_J['J60']}><br><br>

''')

# Create bottom part of HTML
output_file.write('''
		</form>
	</body>


</html>
''')

# Close output file
output_file.close

########## End of the File ##########
