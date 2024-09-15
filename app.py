from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="company"
    )

# Route to show the form for adding employee data (Employer view)
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        acf2_id = request.form['acf2_id']
        td_mail = request.form['td_mail']
        wipro_mail = request.form['wipro_mail']
        week1 = request.form['week1']
        week2 = request.form['week2']
        week3 = request.form['week3']
        week4 = request.form['week4']
        week5 = request.form['week5']
        total = int(week1) + int(week2) + int(week3) + int(week4) + int(week5)
        leave_count = request.form['leave_count']
        leave_details = request.form['leave_details']
        comments = request.form['comments']
        
        db = get_db_connection()
        cursor = db.cursor()
        
        cursor.execute("""
            INSERT INTO employees (employee_id, employee_name, acf2_id, td_mail, wipro_mail, week1, week2, week3, week4, week5, total, leave_count, leave_details, comments)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (employee_id, employee_name, acf2_id, td_mail, wipro_mail, week1, week2, week3, week4, week5, total, leave_count, leave_details, comments))
        
        db.commit()
        cursor.close()
        db.close()
        
        return redirect(url_for('add_employee'))
    
    return render_template('add_employee.html')

# Route to show employee data (Admin view)
@app.route('/view')
def view_employees():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template('view_employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
