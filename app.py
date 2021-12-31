from flask import Flask,jsonify,request
app=Flask(__name__)

contacts=[
    {
        "id":1,
        "number":1234567890,
        "name":u"Rith boi",
        "done":False,
    },
    {
        "id":2,
        "number":7666201482,
        "name":u"noob boi",
        "done":True,
    }
]
@app.route("/add-data",methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"plz provide the data"
        },400)
    number={
            "id":contacts[-1]["id"]+1,
            "name":request.json["name"],
            "number":request.json["number"],
            "done":False
        }
    contacts.append(number)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")   
def get_data():
    return jsonify({
        "data":contacts
    })
if __name__ == '__main__':
    app.run(debug=True)

