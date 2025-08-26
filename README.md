# ✈️ Flight Finder

A modern flight search web application built with Python Flask and Tailwind CSS. Search for flights by origin, destination, and date with real-time pricing data from Google Flights via SerpAPI.

## 🚀 [Live Demo](https://flightfinder-app.onrender.com/)

> **Note:** The demo is hosted on a free tier service. Initial load may take up to 60 seconds as the server spins up. Subsequent requests will be much faster!

## 📋 Features

- **Real-time Flight Data** - Live pricing and availability from Google Flights
- **Detailed Flight Information** - View airline, flight numbers, departure/arrival times
- **Layover Details** - See connection information and layover durations
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Clean Interface** - Modern UI built with Tailwind CSS

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML, Tailwind CSS, Jinja2 Templates
- **API**: SerpAPI for Google Flights data
- **Deployment**: Render

## 🎯 How to Test the Demo

1. **Visit the live demo** (may take ~60 seconds to load initially)
<div align="center">
  
## 🚀 **[🔗 Try Live Demo](https://flightfinder-app.onrender.com/)**

*⚠️ Note: Demo may take up to 60 seconds to load initially (free hosting)*

</div>
2. 
3. **Enter flight details**:
   - **From**: Airport code (e.g., LAX, JFK, ORD)
   - **To**: Destination airport code
   - **Date**: Select your departure date
4. **Click "Find Flights"** to search
5. **View results** with pricing, duration, and layover information

### Sample Test Data:
- **From**: `LAX` (Los Angeles)
- **To**: `JFK` (New York)
- **Date**: Any future date

## 🏃‍♂️ Local Development

### Prerequisites
- Python 3.8+
- SerpAPI key 

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FlightFinder-App.git
   cd FlightFinder-App
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API key**
   Create a `keys.py` file in the root directory:
   ```python
   SERPAPI_KEY = "your_serpapi_key_here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## 📸 Screenshots
At:
https://imgur.com/a/tGCUFxB

## ⚡ API Information

This application uses [SerpAPI](https://serpapi.com) to fetch real-time flight data from Google Flights. SerpAPI provides:
- Live pricing information
- Flight schedules and availability  
- Airline and aircraft details
- Layover and connection information

## 📝 Project Structure

```
FlightFinder-App/
├── app.py              # Main Flask application
├── keys.py             # API keys (not tracked in git)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main template file
└── README.md          # This file
```



---

