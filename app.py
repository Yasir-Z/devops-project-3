from flask import Flask, jsonify

app = Flask(__name__)


# Logic for Unit Testing
def calculate_priority(task_count):
    if task_count > 5:
        return "High"
    return "Low"


@app.route("/status")
def get_status():
    # Integration point: Logic + Web Route
    priority = calculate_priority(2)
    return jsonify({"status": "Active", "priority": priority})


if __name__ == "__main__":
    app.run(debug=True)
