from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Demo Application</title>
        </head>
        <body>
            <h1>CI/CD Demo Application</h1>
            <p>Hello from Bhavya!</p>
            <p>This application will be deployed using GitHub Actions and AWS.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)