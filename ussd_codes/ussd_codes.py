from admin_controls.admin_codes import client
def replies(mobile, text) -> str:

    using = client.query(q.get(q.ref(q.collection("userData"), mobile)))
    trans_acc = using["data"]["trans_acc"]
    tkey = using["data"]["tkey"]
    birth = using["data"]["birth"]
    amount = using["data"]["amount"]
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
            response = "CON Please Enter the amount you would like to transfer, \n"

        elif text == "2":
            response = "CON Please enter your TPay transaction PIN to complete this transaction \n"
            
        elif text == "3":
            response = "CON Account Options\n"
            response += "1. Change Password \n"
            response += "2. Retrive Password \n"
            response += "3. Change email \n"
            response += "4. Retrieve email"

        elif text == "3*1":
            response = "CON Please Enter your old TPay Password:"

        elif text == "3*2":
            response = "CON Please Enter your Date of birth:"
        
        elif text == "3*3":
            response = "CON Please enter your old TPay email\n"
        
        elif text == "3*4":
            response = "CON Please enter your Tpay password\n"


    return response