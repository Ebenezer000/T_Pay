from admin_controls.admin_codes import client, ussd_sender


#####
def replies():

    new_data = ussd_sender.get_new_conversation
    client = new_data["client"]
    session = new_data["session"]
    mobile = new_data["mobile"]

    using = client.query(q.get(q.ref(q.collection("userData"), mobile)))
    tkey = using["data"]["tkey"]
    signed = using["data"]["signed"]

    if signed == "":
        ussd_sender.reply_user(message=f"WELCOME")