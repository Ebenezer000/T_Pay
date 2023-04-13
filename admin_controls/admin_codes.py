from faunadb.client import FaunaClient

############### Admin Codes ###############
##DataBase
fauna_secret = "fnAFBcikAvAAUNqSbbJ_8W17nA1lxzZHVLq1p6Gr"
client = FaunaClient(secret=fauna_secret, domain="db.us.fauna.com")