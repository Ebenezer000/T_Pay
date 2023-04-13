from flask import Flask, request, make_response
from faunadb import query as q
from admin_controls.admin_codes import client
from ussd_codes.ussd_codes import replies

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, It Works"

@app.route("/ussd", methods=["GET", "POST"])
def hook():
    print("level 1")
    if request.method == 'POST':
        print("level 2")
        mobile = request.values.get('phoneNumber')
        text = request.values.get('text')
        
        try:
            print("level 3")
            client.query(q.get(q.match(q.index("loginData"), mobile)))
        except:
            print("level 4")
            client.query(q.create(q.ref(q.collection("userData"), mobile), {
                "data": {
                "id": mobile,
                "trans_acc": "",
                "tkey": "",
                "amount": "",
                "birth": "",
                "hold_reply": "",
                "last_session": "",
                "signed": ""
            }
            }))

        responce = replies(mobile, text)
        print("all done")
    return responce

if __name__ == '__main__': 
    app.run(debug=True)
