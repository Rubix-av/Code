from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api_stock")
def api_stock() -> list:
 
    result_list = []

    # loops through all 200 ids which are there on "url" and appends to "result_list"
    for i in range(1,201):
        url = f"https://jsonplaceholder.typicode.com/todos/{i}"
        response = requests.get(url)
        data = response.json()
        result_list.append(data)
    
    return jsonify(result_list)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

