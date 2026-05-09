# 🍎 AI Fruit Prediction API

This project is a RESTful API developed with FastAPI designed to predict and classify 20 distinct types of fruits. The core prediction engine is powered by a Random Forest machine learning model (fruit_model.pkl).

## 🚀 Key Features
- Predicts and classifies up to 20 different fruit categories based on input data.
- Built with FastAPI, ensuring high performance and asynchronous request handling.
- Includes integrated HTML templates for immediate testing and preliminary usage.
- Fully containerized, supporting seamless deployment via Docker and Docker Compose.

## ⚙️ Installation and Setup

### 🐍 Method 1 Running in a Local Python Environment

**1. Clone the repository to your local machine**
```bash
git clone https://github.com/Kittithad-Ittipon/ai-prediction-fruit.git
cd ai-prediction-fruit
```

**2. Create and activate a virtual environment**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required dependencies**
```bash
pip install -r app/requirements.txt
```

**4. Start the FastAPI server** 
```bash
uvicorn app.main:app --reload
```

### 🐳 Method 2 Running with Docker Compose

If Docker is installed on your system, you can easily deploy the application with a single command
```bash
docker-compose up -d --build
```
The system will automatically build the necessary Docker image and start the container in the background.