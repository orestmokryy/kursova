import datetime

import serial
from flask import Flask, render_template
import psycopg2
from settings import credentials

app = Flask(__name__)


def get_db_connection():
    connection = psycopg2.connect(dbname=credentials['database_name'],
                                  user=credentials['database_user'],
                                  password=credentials['database_password'],
                                  host=credentials['database_host'])

    return connection

@app.route("/")
def hello():
    port = serial.Serial('COM3', 9600, timeout=0.1)
    data = str(port.readline().decode('UTF-8'))
    # print(data)
    if data != '':
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            QUERY = "INSERT INTO sensor_data(value) VALUES (%s)"

            cursor.execute(QUERY, (str(data),))
            connection.commit()
        except Exception as e:
            print(e)
    connection = get_db_connection()
    cursor = connection.cursor()
    SELECT_QUERY = "SELECT * FROM sensor_data ORDER BY id DESC LIMIT 1"
    cursor.execute(SELECT_QUERY)
    result = cursor.fetchone()
    print(result)
        # connection.close()
        # value = result[1]

    return render_template('index.html', data=result[1])



    # return '1'
if __name__ == "__main__":
    app.run(debug=True)