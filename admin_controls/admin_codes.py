from faunadb.client import FaunaClient
from Qrios_Wrapper import qrios
############### Admin Codes ###############
##DataBase
fauna_secret = "fnAFBcikAvAAUNqSbbJ_8W17nA1lxzZHVLq1p6Gr"
client = FaunaClient(secret=fauna_secret, domain="db.us.fauna.com")

ussd_sender = qrios(client_id= "NAaQFC4P", client_secret= "WU68WYjCX92D1Tm8oHcEG48g")