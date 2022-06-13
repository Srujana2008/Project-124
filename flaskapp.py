from flask import Flask, jsonify, request
app = Flask(__name__)
contacts = [
    {
        "id": 1,
        "name": u"Raj",
        "contact": u"9949968698",
        "done": False
    },
    {
        "id": 2,
        "name": u"Jasmine",
        "contact": u"8519968698",
        "done": False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if(not request.json):
        return jsonify({
            "status": "error", 
            "message": "Please provide the data!"
        },
        400)

    contact = {
        "id": contacts[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json.get("contact", ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added successfully!"
    })  