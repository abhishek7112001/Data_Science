'''
There are several ways to request data in a Flask application:


Files: This is data sent in the request body as files. 
This type of data is typically sent in a POST request and can be accessed using the request.files attribute,
which is a dictionary-like object containing all the files in the request.

Path parameters: 
This is data passed in the URL as part of the endpoint. 
For example, http://localhost:5000/users/1. 
In Flask, you can access path parameters by defining placeholders in the endpoint and 
using the route() decorator to specify the endpoint. 
The placeholders can then be accessed using the request.view_args attribute, 
which is a dictionary-like object containing all the key-value pairs in the path parameters.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

# +
'''
Query parameters: 
These are data passed in the URL as key-value pairs after the endpoint. 
In Flask, you can access query parameters using the request.args attribute, 
which is a dictionary-like object containing all the key-value pairs in the query string.
'''

@app.route('/hello',methods=['POST'])
def hello():
    data  = request.args
    name  = data.get('name')
    other = data.get('other')
    
    return jsonify({'Name =' : name.upper(), 'Surname' : other.upper()})


# +
'''
JSON data: This is data sent in the request body in JSON format. 
This type of data is typically sent in a POST request and can be accessed using the request.get_json() method, 
which parses the JSON data and returns it as a Python dictionary.
'''

@app.route('/user',methods=['POST'])
def user():
    data  = request.get_json()
    name  = data['name']
    other = data['other']
    
    return jsonify({'Name =' : name.upper(), 'Surname' : other.upper()})\


# +
'''
Form data: 
This is data sent in the request body in the format of key-value pairs. 
This type of data is typically sent in a POST request and can be accessed using the request.form attribute, 
which is a dictionary-like object containing all the key-value pairs in the form data.
'''

@app.route('/greet', methods=['POST'])
def greet():
    data = request.form
    Name =  data['name']
    Other = data['other']
    return f'Hello, {Name.upper(), Other.upper()}!'



# -

if __name__ == '__main__':
    app.run(debug=True)
