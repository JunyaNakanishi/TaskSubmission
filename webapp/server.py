from flask import Flask, render_template, request
import serial
from time import sleep

app = Flask(__name__)
@app.route('/')
def index()->str:
    return render_template('ar_contrl.html')

@app.route('/', methods=['POST'])
def red()->str:
 with serial.Serial("/dev/cu.usbmodem1421",9600,timeout=1) as ser:
    sleep(2)
    while True:
        res = request.form['post_value']
        if res == 'REDLEDON':
            flag = bytes('a','utf-8')
            ser.write(flag)

        elif res == 'REDLEDOFF':
            flag = bytes('b','utf-8')
            ser.write(flag)

        elif res == 'BLUELEDON':
            flag = bytes('c','utf-8')
            ser.write(flag)

        elif res == 'BLUELEDOFF':
            flag = bytes('d','utf-8')
            ser.write(flag)

        elif res == 'MOTORON':
            flag = bytes('e','utf-8')
            ser.write(flag)

        elif res == 'MOTOROFF':
            flag = bytes('f','utf-8')
            ser.write(flag)

        return render_template('getpost.html')
 ser.close()

if __name__ == '__main__':
    app.run(port = 8080)
