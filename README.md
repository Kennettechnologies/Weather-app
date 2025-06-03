# Weather App

A Django-based weather application that provides current weather conditions and forecasts for cities worldwide.

## Features

- City weather search
- Current weather display
- 5-day forecast
- Location detection
- Search history
- Dark/Light mode toggle
- Mobile responsive design

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Visit `http://localhost:8000` in your browser
2. Enter a city name to get current weather
3. View the 5-day forecast
4. Use the dark/light mode toggle for preferred viewing

## Technologies Used

- Django
- Bootstrap 5
- OpenWeatherMap API
- Chart.js for weather charts
- Django Crispy Forms 