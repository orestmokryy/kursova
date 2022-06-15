import datetime

import serial
from flask import Flask, render_template
from pymysql import connect

app = Flask(__name__)


@app.route("/")
def hello():
    port = serial.Serial('COM3', 9600, timeout=0.1)
    data = str(port.readline().decode('UTF-8'))
    if data != '':
        try:
            with connect(host="localhost",
                         user="maxym",
                         password="1527956Makc"
                         ) as connection:
                QUERY = "INSERT INTO sensors.sensor_data(value, recorded.at) VALUES (%s, %s)"
                with connection.cursor() as cursor:
                    cursor.execute(QUERY, [str(data), datetime.datetime.now()])
                    connection.commit()
        except:
            print(e)


    return render_template('index.html', data=data[:5])

if __name__ == "__main__":
    app.run(debug=True)
