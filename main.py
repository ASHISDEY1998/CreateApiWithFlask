from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/armstrong/<int:num>')
def armstrong_num(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_cubes = 0
    for digit in num_str:
        digit_int = int(digit)
        cube = digit_int ** num_len
        sum_of_cubes += cube
    if sum_of_cubes == num:
        result = {
            'number': num,
            'armstrong': True,
            'server-ip': '192.168.2.24'
        }
    else:
        result = {
            'number': num,
            'armstrong': False,
            'server-ip': '192.168.2.24'
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)