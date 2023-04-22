import requests
######

class qrios():
    def __init__(self, client_id, client_secret) -> None:
        self.headers = {
            "X-Client-Id": client_id,
            "X-Client-Secret": client_secret,
    }
        
    def get_new_conversation(self, request)-> dict:
        session = request.values.get('sessionId')
        clientId = request.values.get('clientId')
        mobile = request.values.get('msisdn')
        data = {
            "client": clientId,
            "session": session,
            "mobile": mobile
        }
        requests.Response
        return data
    
    def get_continued_conversation(self, request) -> dict:
        session = request.values.get('sessionId')
        clientId = request.values.get('clientId')
        result = request.values.get('result')
        reply = result['value']
        data = {
            "client": clientId,
            "session": session,
            "reply": reply
        }
        return data
    
    def get_closed_message(self, request) -> dict:
        session = request.values.get('sessionId')
        clientId = request.values.get('clientId')
        data = {
            "client": clientId,
            "session": session,
        }
        return data
    
    def get_aborted_message(self, request) -> dict:
        session = request.values.get('sessionId')
        clientId = request.values.get('clientId')
        reason = request.values.get('result')
        type = reason['type']
        data = {
            "client": clientId,
            "session": session,
            "type": type
        }
        return data

    def reply_user(self, message):
        data = {
            "action": {
                "type": "ShowView",
                "view": {
                    "type": "InputView",
                    "message": message
                }
            },
            "contextData": "devCorrelationId:12345"
        }
        response = ("HTTP 200 (OK)", data)
        return response
    
    def end_conversation(self, message) -> dict:
        data = {
            "action": {
                "type": "ShowView",
                "view": {
                    "type": "InfoView",
                    "message": message
                }
            },
            "contextData": "devCorrelationId:12345"
        }
