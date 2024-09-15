from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# checks if a numbers is a Armstrong number or not
@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")

        # creates "result" dict. which will later be returned as a JSON object
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.234.213.53"
        }

    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.234.213.53"
        }

    # returns "result" dict. converted to JSON object
    return jsonify(result)

# instead of everything thing, this retrieves only the "Armstrong" attribute of JSON
@app.route("/check/<int:id>")
def check(id):

    # first we will refer the original dataset for JSON object
    url = f"http://127.0.0.1:5000/armstrong/{id}" 

    # makes a GET request to "url"
    response = requests.get(url)

    # "data" is the actual dataset for the speicified "id"
    data = response.json()

    # only retrieves the "Armstrong" attribute from JSON object "data"
    armstrong = data.get("Armstrong")

    # returns the final answer in <h1> tags
    return f"<h1>{armstrong}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

