# FlightFinder-App

✈️ Flight Finder
A modern flight search web application built with Python Flask and Tailwind CSS. Search for flights by origin, destination, and date with real-time pricing data from Google Flights via SerpAPI.
🚀 Live Demo

Note: The demo is hosted on a free tier service. Initial load may take up to 60 seconds as the server spins up. Subsequent requests will be much faster!

📋 Features

Real-time Flight Data - Live pricing and availability from Google Flights
Detailed Flight Information - View airline, flight numbers, departure/arrival times
Layover Details - See connection information and layover durations
Responsive Design - Works seamlessly on desktop and mobile devices
Clean Interface - Modern UI built with Tailwind CSS

🛠️ Technology Stack

Backend: Python Flask
Frontend: HTML, Tailwind CSS, Jinja2 Templates
API: SerpAPI for Google Flights data
Deployment: Render

🎯 How to Test the Demo

Visit the live demo (may take ~60 seconds to load initially)
Enter flight details:

From: Airport code (e.g., LAX, JFK, ORD)
To: Destination airport code
Date: Select your departure date


Click "Find Flights" to search
View results with pricing, duration, and layover information

Sample Test Data:

From: LAX (Los Angeles)
To: JFK (New York)
Date: Any future date

🏃‍♂️ Local Development
Prerequisites

Python 3.8+
SerpAPI key (Get one free here)

Installation

Clone the repository
bashgit clone https://github.com/yourusername/FlightFinder-App.git
cd FlightFinder-App

Create virtual environment
bashpython3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies
bashpip install -r requirements.txt

Set up API key
Create a keys.py file in the root directory:
pythonSERPAPI_KEY = "your_serpapi_key_here"

Run the application
bashpython app.py

Open in browser
Navigate to http://localhost:5000
