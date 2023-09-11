# importing modules
from flask import Flask, request, jsonify
import datetime
import pytz

# creating the application
app = Flask(__name__)

@app.route('/api', method = ["GET"])
def get_data():
    # Get query parameters from the URL
    slack_name = request.args.get("slack_name")
    track = request.args.get('track')

    # validating parameters
    if not slack_name or not track:
        return jsonify({"error": "Missing parameters"}), 400
    
    # get the current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime("%A")

    # get the current UTC time
    utc_time = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # get the github URL of the "endpoint.py" file
    github_file_url = ""

    # get the github URL of my repo source codes
    github_repo_url = ""

    # creating the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run()                                                 