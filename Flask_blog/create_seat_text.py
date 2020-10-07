# filename:		create_seats_text.py

index = 600

seat_alphabet = ''
seats_in_row = 60
seats_left_flank = 30
seats_right_flank = 30
total_row = 10
row_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

output_filename = "seatDisplay_test.txt"
output_file = open(output_filename, "w")

# create HTML Top part
output_file.write('''
<html>
	<head>
		<!-- <link rel="stylesheet" href="style.css"> -->
	</head>
	
	<style>
      .img-container {
        text-align: center;
      }
    </style>
    

	<body>
		<h3>Seat Display</h3>
		
		
		<div class="img-container"> <!-- Block parent element -->
			<img src="stage1.png" alt="Stage">
    	</div>

    	<br><br>

		<form action="">

''')

for row in row_label:

    output_file.write(f"<label style=\"font-family:'Courier New'\">[{row}1-{row}60]</label>\n")
    # for seat1 in range(seats_in_row):
    for seat1 in range(seats_left_flank):
        output_file.write(
                f'''<input type="checkbox" id="{row}{seat1 + 1}" name="{row}{seat1 + 1}" value="{row}{seat1 + 1}" ''' \
                + "{" + f"row_{row}[\'{row}{seat1 + 1}\']" + "}>")

    output_file.write("&emsp;&emsp;")

    for seat2 in range(seats_right_flank):
        output_file.write(
                f'''<input type="checkbox" id="{row}{seat2 + 31}" name="{row}{seat2 + 31}" value="{row}{seat2 + 31}" ''' \
                + "{" + f"row_{row}[\'{row}{seat2 + 31}\']" + "}>")

    # output_file.write("<br>")

    output_file.write("<br><br>\n")

# Create bottom part of HTML
output_file.write('''
    </form>
    </body>
    </html>
''')

# Close the output file
output_file.close
