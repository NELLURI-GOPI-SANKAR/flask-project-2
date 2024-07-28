from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

# Oracle DB connection details
dsn = cx_Oracle.makedsn("DESKTOP-IT2AN7M", 1521, service_name="xe")
connection = cx_Oracle.connect(user="system", password="gopi9392", dsn=dsn)
cursor = connection.cursor()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = request.form.get('remember')  # 'on' if checked, otherwise None
    
    try:
        cursor.execute("INSERT INTO login_table (username, password) VALUES (:1, :2)", (username, password))
        connection.commit()
        return redirect(url_for('success'))
    except cx_Oracle.DatabaseError as e:
        print(f"Error: {e}")
        return "An error occurred while processing your request."

@app.route('/success')
def success():
    return "Login details stored successfully!"

if __name__ == '__main__':
    app.run(debug=True)



