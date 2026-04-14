from flask import Flask, jsonify
from routes import register_routes
from db import init_db

# Need Postman
# Set method from GET to POST
# Enter URL
# Type {
 # "username": "StevieX",
  #"password": "mypassword123"
#}

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Global handler for Page not found
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "This route does not exist"}), 404

# Global handler for server crashed
@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error. Our bad!"}), 500

init_db()
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)