from flask import Flask, request, make_response
from faunadb import query as q
from admin_controls.admin_codes import client, headers
from ussd_codes.ussd_codes import replies
import requests

url = "https://deep.qrios.com/api/v1/ussd/app/push"


data = """
{
  "appId": "T_pay",
  "msisdn": "2348177642325",
  "contextData": "devCorrelation:1234"
}
"""




app = Flask(__name__)

@app.route("/ussd", methods=["GET", "POST"])
def index():
    response = ""
    resp
    data = f"""
{
  "appId": "T_pay",
  "msisdn": "2348177642325",
  "contextData": {response}
}
"""
    if request.method == "GET":
        response = "Hello it works wonders"
    if request.method == 'POST' :
        mobile = request.values.get('phoneNumber')
        text = request.values.get('text')
        
        try:
            client.query(q.get(q.match(q.index("loginData"), mobile)))
        except:
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

        response = replies(mobile, text)
        print(response)
        resp = requests.post(url, headers=headers, data=data)

        print(resp)

    return (resp)

if __name__ == '__main__': 
    app.run(debug=True)
