from faunadb.client import FaunaClient

############### Admin Codes ###############
##DataBase
fauna_secret = "fnAFAZYyLKAAUY3-ZL5ntrRfZBPfifwOvF-EUD8v"
client = FaunaClient(secret=fauna_secret, domain="db.us.fauna.com")