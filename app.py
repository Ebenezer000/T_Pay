from flask import Flask, request, make_response
from faunadb import query as q
from admin_controls.admin_codes import client
from ussd_codes.ussd_codes import replies

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, It Works"

@app.route("/ussd", methods=["GET", "POST"])
def hook(request):

    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        mobile = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        
        try:
            client.query(q.get(q.match(q.index("loginData"), mobile)))
        except:
            client.query(q.create(q.ref(q.collection("userData"), mobile), {
                "data": {
                "id": mobile,
                "trans_acc": "",
                "tkey": "",
                "amount": "",
                "signed": ""
            }
            }))

        replies(mobile, text)

if __name__ == '__main__': 
    app.run(debug=True)
