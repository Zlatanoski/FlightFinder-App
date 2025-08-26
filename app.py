from flask import Flask, render_template, request
import requests

from keys import SERPAPI_KEY
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])

def index():
    flight_data = []

    if request.method == "POST":
        origin = request.form['origin']
        destination = request.form['destination']
        outbound_date = request.form['outbound_date']

        params = {
            "engine":"google_flights",
            "departure_id" : origin,
            "arrival_id": destination,
            "outbound_date" : outbound_date,
            "type" : 2,
            "api_key" : SERPAPI_KEY



        }

        req = requests.get("https://serpapi.com/search", params=params)
        data = req.json()
        if 'error' in data:
            return render_template("index.html", error=data['error'])

        flight_data = data.get("best_flights",[])

        return render_template("index.html", flights = flight_data)
    return render_template("index.html", flights=flight_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)