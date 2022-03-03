from flask import Flask, jsonify, request


app = Flask(__name__)

tasks = [
    {
        "Contact":"4024959249",
        "Name":"Antwan",
        "done":False,
        "id":1
    },{
        "Contact":"4398285789",
        "Name":"Guy",
        "done":False,
        "id":2
    }

]

def add_task():
    

    info = {
    "id":tasks[-1]["id"]+1,
    "Name":request.json["Name"],
    "Contact":request.json.get("Contact", ""),
    "done":False
   }

    tasks.append(info)
    return jsonify({
       "status":"success",
       "message":"Task added successfully"
   })


@app.route("/get-data")
def add_task():
    return jsonify({
        "data":tasks
    })
    

if(__name__ == "__main__"):
    app.run(debug = True)
