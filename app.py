from flask import Flask, request, render_template, redirect,url_for
import sqlite3

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data = cursor.execute("SELECT * from ALERTS;")
    entries = []
    for entry in data:
        entries.append(entry)
    entries.reverse()
    return render_template('index.html', entries=entries, name='Home')
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        data = request.form
        email = data["email"]
        phone_num = data["phone"]
        helper = 0
        try:
            if data["provide_help"] == 'on':
                helper = 1
        except Exception as e:
            print("not a helper")
        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            cursor.execute(f"INSERT INTO CONTACTS VALUES ('{email}', '{phone_num}', {helper})")
            sqliteConnection.commit()
            print("successfully inserted in CONTACTS table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return redirect("/")
    else:
        return render_template('add.html', content='add')
    
@app.route('/notification', methods=['GET', 'POST'])
def notification():
    if request.method == "POST":
        data = request.form
        title = data["title"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            print(title)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{title}', '{body}', 'info')")
            sqliteConnection.commit()
            print("inserted into ALERTS table ", cursor.rowcount)
            cursor.close()
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("SQLite connection closed")
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("select * from CONTACTS")
        entries = []
        for entry in data:
            entries.append(entry)
        def sendmail():
            #write a sendmail funtion later
            print("sending mail...")
        return redirect("/")
    else:
        return render_template('notification.html', content='notification')

@app.route('/help_request', methods=['GET', 'POST'])
def help_request():
    if request.method == "POST":
        data = request.form
        title = data["title"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            print(title)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{title}', '{body}', 'warning')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("SELECT * from CONTACTS WHERE Helper=1 ")
        entries = []
        for entry in data:
            entries.append(entry)

        def sendmail():
            #write a sendmail funtion later
            print("sending mail...")
        return redirect("/")
    else:
        return render_template('help_request.html', content='help')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == "POST":
        data = request.form
        title = data["title"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            print(title)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{title}', '{body}', 'danger')")
            sqliteConnection.commit()
            print(" successfully inserted into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("SQLite connection closed")
        
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("SELECT * from CONTACTS;")
        entries = []
        for entry in data:
            entries.append(entry)

        for entry in entries:
            def sendMessage():
                #write a sendMessage function later
                print("sending message...")
            #send email via Gmail
            def sendMail():
                #write a sendmail funtion later
                print("sending mail...")

        return redirect("/")
    else:
        return render_template('emergency.html', content='emergency')

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000,debug=False)