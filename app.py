from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Demo</title>
        </head>
        <body>
            <h1>🚀 DevOps CI/CD Pipeline</h1>
            <h2>Application is Running Successfully!</h2>
            <p>Environment: Local Docker</p>
            <p>CI/CD: Jenkins</p>
            <p>Version Control: GitHub</p>
            <p>Time: {}</p>
        </body>
    </html>
    """.format(datetime.now())

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "DevOps Demo",
        "message": "Application is healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)