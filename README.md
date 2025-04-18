 # 🌦️ Weather Forecasting Service

A fully Dockerized Django REST API that fetches weather data from the OpenWeatherMap API and returns weather forecasts based on city input. This project also includes CI/CD integration using GitHub Actions to automatically build and push Docker images.

---

## 📁 Project Structure

weather_service/ 
├── weather/ # Django app 
  │ ├── views.py # Weather forecast view logic 
  │ ├── urls.py # App-specific URL routing 
  │ └── ... 
├── weather_service/ # Project config 
  │├── settings.py 
  │ ├── urls.py 
  │ └── ... 
├── Dockerfile # Docker configuration 
├── .dockerignore # Files to exclude from Docker image 
├── .github/ 
  │ └── workflows/ │
     └── docker-build.yml # GitHub Actions workflow 
├── manage.py 
├── requirements.txt 
└── README.md # Project documentation



---

## 🚀 Features

- Fetches live weather data using OpenWeatherMap API.
- Accepts city name as input via REST API.
- Returns structured JSON weather data.
- Fully containerized using Docker.
- CI/CD pipeline to build and push Docker images on each commit using GitHub Actions.

---

## 🛠️ Technologies Used

- Python 3.x
- Django & Django REST Framework
- Docker
- GitHub Actions
- OpenWeatherMap API

---

## 🐳 Docker Instructions

### 🔧 Build the Docker Image

```bash
docker build -t weather-service .

📡 API Usage
Endpoint:

GET /weather/?city=<city_name>

📦 Requirements

Install dependencies for local development (if needed):

pip install -r requirements.txt

👤 Author

Lokendra Shukla
GitHub: @LokiatHT
