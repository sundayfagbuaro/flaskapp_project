#!/usr/bin/env python3
from flask import Flask, render_template, request

import pymysql


#db = pymysql.connect(host='localhost', user='root', password='password', database='users_db') # connect to localhost
#db = pymysql.connect(host='flask_db', user='root', password='password', database='users_db', port=3306) # Connect to docker.
db = pymysql.connect(host='flask-db', user='root', password='password', database='users_db', port=3306) # Connect to k8s.

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        address = request.form['address']
        phone = request.form['phone']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = db.cursor()
        cursor.execute("INSERT INTO new_users (f_name,l_name,address,phone,username,password,email) VALUES (%s,%s,%s,%s,%s,%s,%s)", (f_name, l_name, address, phone, username, password, email))
        db.commit()
        cursor.close()
        return "records successfully submited"
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



# Manual Run
#    flask --app app --debug run


