from flask import Flask, render_template_string, jsonify
import threading

# Define the HTML content as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Flask Example</title>
</head>
<body>
    <h1>Hello from Flask!</h1>
    <button onclick="getMessage()">Get Message from Server</button>
    <p id="message"></p>

    <script>
        async function getMessage() {
            const response = await fetch('/api/message');
            const data = await response.json();
            document.getElementById('message').innerText = data.message;
        }
    </script>
</body>
</html>
"""

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML content as a response
    return render_template_string(html_content)

@app.route('/api/message')
def message():
    # Return a JSON response
    return jsonify(message="Hello from Python server!")

# Function to run the Flask app in a separate thread
def run_flask_app():
    app.run(port=5030)

# Start the Flask server in a new thread
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.start()
