# import the Flask library
from flask import Flask, render_template, request
# import the MySQL connector library
import mysql.connector

app = Flask(__name__)

# set up a connection to your MySQL database
mysql_config = {
  'user': 'kjatjhuwaf',
  'password': '4S8UzXR55E',
  'host': '104.248.126.173',
  'database': 'kjatjhuwaf'
}
# Execute the MySQL query
cnx = mysql.connector.connect(**mysql_config)
cursor = cnx.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input value from the form
        input_value = request.form['input']

        # execute an SQL query to retrieve data from your table
        query = "SELECT ClientKey, concat(LastName, ' ,', FirstName) AS ClientName FROM tblclients WHERE LastName = %s"
        cursor.execute(query,(input_value,))

        # fetch the results and store them in a variable
        results = cursor.fetchall()

        if not results:
            # Display "not found" message in the same form
            return render_template('index.html', not_found=True)
        else:
            # Display the results in the same form
            return render_template('index.html', results=results)

    return render_template('index.html')

@app.route('/detailedit/<int:id>', methods=['GET', 'POST'])
def edit_row(id):
    cursor = cnx.cursor()
    cursor.execute('SELECT ClientKey, LastName, FirstName, email FROM tblclients WHERE ClientKey=%s', (id,))
    row = cursor.fetchone()

    if request.method == 'POST':
        lastname = request.form['LastName']
        firstname = request.form['FirstName']
        email = request.form['email']
        cursor.execute('UPDATE tblclients SET LastName=%s, FirstName=%s, email=%s WHERE ClientKey=%s', (lastname, firstname, email, id))
        cnx.commit()
        return render_template('updated.html', row=row)

    return render_template('detailedit.html', row=row)

@app.route('/detailadd', methods=['POST'])
def add_row():
    cursor = cnx.cursor()

    if request.method == 'POST':
        lastname = request.form['LastName']
        firstname = request.form['FirstName']
        email = request.form['email']
        cursor.execute('INSERT INTO tblclients (LastName, FirstName, email) VALUES (lastname, firstname, email)')
        cnx.commit()
        return render_template('updated.html')

    return render_template('edit.html')

@app.route('/view-data')
def view_data():
    # Get the id and the value from the URL parameters
    id = request.args.get('id')
    value = request.args.get('value')
  
    # Connect to the MySQL database
    cnx = mysql.connector.connect(**mysql_config)
    cursor = cnx.cursor()
  
    # Query the MySQL table for the data using the id
    query = f"SELECT * FROM my_table WHERE id = {id}"
    cursor.execute(query)
    data = cursor.fetchone()
  
    # Close the MySQL connection
    cursor.close()
    cnx.close()
    return render_template('edit.html', data=data, value=value)

# run your application
if __name__ == '__main__':
    app.run(debug=True)
