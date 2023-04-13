from admin_controls.admin_codes import client, ussd_sender
from faunadb import query as q


#####
def replies(request):

    new_data = ussd_sender.get_new_conversation(request)
    client = new_data["client"]
    session = new_data["session"]
    mobile = new_data["mobile"]

    using = client.query(q.get(q.ref(q.collection("userData"), mobile)))
    tkey = using["data"]["tkey"]
    signed = using["data"]["signed"]

    if signed == "":
        ussd_sender.reply_user(message=f"""WELCOME TO TPAY

Please set up your TPay PIN to use this service """)

    else:
        ussd_sender.reply_user(
            message="""WELCOME TO TPAY
What would you like to do today
1. Transfer 
2. Check Balance
3. Account Settings"""
        )