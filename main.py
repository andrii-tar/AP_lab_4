from itertools import product
from platform import python_version
from flask import Flask, request

app = Flask(__name__)


def get_variant(student_id):
    # student_id = 24
    print(list(product(
        ('python 3.8.*', 'python 3.7.*', 'python 3.6.*'),
        ('venv + requirements.txt', 'virtualenv + requirements.txt', 'poetry', 'pipenv'))
    )[(student_id - 1) % 12])
    print("Current Python Version-", python_version())


@app.route('/api/v1/hello-world-24', methods=['GET'])
def helloworld():
    if request.method == 'GET':
        # data = {"data": "Hello World"}
        # return jsonify(data)
        return "Hello World 24", 200


if __name__ == '__main__':
    my_num = 24
    app.run(debug=False)
