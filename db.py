# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('database.db')

title = "พิสูจน์หลักฐานจังหวัดภูเก็ต1"
line_one = "พิสูจน์หลักฐานจังหวัดภูเก็ต"
line_two = "323/39 ถ.เยาวราช"
line_three = "ต.ตลาดใหญ่ อ.เมืองภูเก็ต"
line_four = "จ.ภูเก็ต 83000"
line_five = "076 211 176"

# with conn:
# 	cursor = conn.cursor()
# 	cursor.execute(f'''INSERT INTO ADDRESSEE (TITLE, LINE_ONE, LINE_TWO, LINE_THREE, LINE_FOUR, LINE_FIVE) VALUES ('{title}', '{line_one}', '{line_two}', '{line_three}', '{line_four}', '{line_five}')''')
# 	conn.commit()

with conn:
	cursor = conn.cursor()
	data = cursor.execute('''SELECT * FROM ADDRESSEE''')
for row in data:
	print(row)
