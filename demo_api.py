from flask import Flask ,request

import sqlite3  

app = Flask(__name__) 

@app.route('/student', methods = ['GET'])
def index(): 
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  
    id =  request.args.get('student_id')
    cursor = conn.cursor() 
    cursor.execute(f'''SELECT * FROM Students WHERE student_id={id};''')
    student = cursor.fetchone()
    conn.close()
    return dict(student)


app.run(host='0.0.0.0' ,port=80 )