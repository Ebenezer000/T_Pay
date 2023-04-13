from admin_controls.admin_codes import client
from faunadb import query as q


def user_replied(ussd, reply) ->bool:
    if ussd in reply and len(reply) != len(ussd):
        return True
    else:
        return False
    
def get_user_reply(ussd, reply) -> str:
    start = len(ussd) - 1
    end = len(reply) -1
    user_reply = reply[start, end]
    return user_reply


def replies(mobile, text) -> str:

    using = client.query(q.get(q.ref(q.collection("userData"), mobile)))
    trans_acc = using["data"]["trans_acc"]
    tkey = using["data"]["tkey"]
    birth = using["data"]["birth"]
    amount = using["data"]["amount"]
    hold_reply = using["data"]["hold_reply"]
    signed = using["data"]["signed"]


    response =""

    if signed == "" :
        response = f"""WELCOME TO TPAY

Please set up your TPay PIN to use this service """

    elif signed != "" and birth == "":
        response = f"""WELCOME TO TPAY

Please add your Date of Birth for security before proceeding """

    else:
        if text == "":
            response = """CON WELCOME TO TPAY\n 
    What would you like to do today. \n"""
            response += "1. Transfer \n"
            response += "2. Check Balance\n"
            response += "3. Account Settings\n"

        elif text == "1":
            response = "CON Please Enter the amount you would like to transfer: \n"

        elif user_replied("1*", text) == True:
            reply = get_user_reply("1*", text)
            client.query(q.update(q.ref(q.collection("userData"), mobile), {"data": {"amount": reply}}))
            response = "CON Please Enter the phone number of the user you would like to transfer to:"
        
        elif user_replied(f"1*{amount}*", text) == True:
            reply = get_user_reply(f"1*{amount}*", text)
            client.query(q.update(q.ref(q.collection("userData"), mobile), {"data": {"trans_acc": reply}}))
            response = "CON Please Enter your TPay PIN to complete this transaction"

        elif user_replied(f"1*{amount}*{trans_acc}*", text) == True:
            reply = get_user_reply(f"1*{amount}*{trans_acc}*", text)
            if reply == tkey:
                response = "END Transaction Successful\n"
                response += "You will recieve an SMS with your transaction details"
            else:
                response = "END Incorrect PIN"

        
        elif text == "2":
            response = "CON Please enter your TPay transaction PIN to complete this transaction \n"
        
        elif user_replied("2*", text) == True:
            reply = get_user_reply("2*", text)
            if reply == text:
                response = "CON Your TPay Balance is ₦0"
            else:
                response = "END Incorrect PIN"
        
            
        elif text == "3":
            response = "CON Account Options\n"
            response += "1. Change Password \n"
            response += "2. Retrive Password \n"

        elif text == "3*1":
            response = "CON Please Enter your old TPay Password:"

        elif user_replied("3*1*", text) == True:
            reply = get_user_reply("3*1*", text)
            if reply == tkey:
                response = "CON Please Enter Your new TPay Password:"
            else:
                response = "END Incorrect Password"

        elif user_replied(f"3*1*{tkey}", text) == True:
            reply = get_user_reply(f"3*1*{tkey}*", text)
            client.query(q.update(q.ref(q.collection("userData"), mobile), {"data": {"hold_reply": reply}}))
            response = "CON Please Re-Enter Your new TPay Password to confirm:"

        elif user_replied(f"3*1*{tkey}*{hold_reply}*", text) == True:
            reply = get_user_reply(f"3*1*{tkey}*{hold_reply}*", text)
            if hold_reply == reply:
                response = "CON Congrats you have Successfully Updated your Password"
            else:
                response = "END Incorrect Password"
        

        elif text == "3*2":
            response = "CON Please Enter your Date of birth:"
        
        elif user_replied("3*2*", text) == True:
            reply = get_user_reply("3*2*", text)
            if reply == birth:
                response = """END Your PIN has been reset to 0000
Please Update it to a more secure password"""
            else:
                response = "END Incorrect Password"


    return response