from requests.structures import CaseInsensitiveDict
from faunadb.client import FaunaClient

############### Admin Codes ###############
##DataBase
fauna_secret = "fnAFBcikAvAAUNqSbbJ_8W17nA1lxzZHVLq1p6Gr"
client = FaunaClient(secret=fauna_secret, domain="db.us.fauna.com")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
headers["X-Client-Id"] = "NAaQFC4P"
headers["X-Client-Secret"] = "WU68WYjCX92D1Tm8oHcEG48g"