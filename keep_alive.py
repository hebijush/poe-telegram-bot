# Import the Flask library and the threading module
from flask import Flask
from threading import Thread

# Create a Flask app object
app = Flask('')

# Define a route for the root path
@app.route('/')
def index():
    # Return a simple hello world message
    return 'Hello, world!'

# Define a function to run the app
def run():
    # Run the app on port 8080
    app.run(host='0.0.0.0', port=8080)

# Define a function to keep the app alive
def keep_alive():
    # Create a thread to run the app
    server = Thread(target=run)
    # Start the thread
    server.start()

# Call the keep_alive function
keep_alive()
