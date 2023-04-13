from admin_controls.admin_codes import client, ussd_sender


#####
def replies(request):
    info = ussd_sender.get_closed_message(request)
    print (info)
    return "HTTP 204 (No content)"