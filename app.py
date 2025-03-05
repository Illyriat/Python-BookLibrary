from flask import Flask
from controllers.controller import controller  # Import the Blueprint

app = Flask(__name__)

# Register the Blueprint with the app
app.register_blueprint(controller)

if __name__ == "__main__":
    app.run(debug=True)
