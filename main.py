from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)
large_number = 8
prime_number = 8683317618811886495518194401279999999

def saltify():
  password = request.get_json()['password']
  print(password)
  first_encoded_number = 0
  first_encoded_string = ""
  second_encoded_number = large_number
  third_encoded_number = 0
  for letter in password:
    first_encoded_string = f"{first_encoded_string}{ord(letter)}"
  first_encoded_number = int(first_encoded_string)

  for counter in range(0, second_encoded_number, 1):
    first_encoded_number *= first_encoded_number

  third_encoded_number = first_encoded_number % prime_number
  print(third_encoded_number)
  return third_encoded_number

@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/encode', methods=["POST"])
def encode():
  saltify()
  return render_template("index.html")

@web_site.route("/api/encrypt", methods=["POST"])
def encrypt():
  print("encrypting")
  data = str(int(saltify()))
  print(data)
  data_string = '{"salt":' + '"' + f'{data}' +'"' + "}"
  print(data_string)
  return data_string

web_site.run(host='0.0.0.0', port=8080)