import pymongo

# connectiong string
# mongo_rul = "mongodb+srv://......"
# FREE SERVICE: mongodb.net
mongo_url = "mongodb://localhost:27017"


client = pymongo.MongoClient(mongo_url)
#
db = client.get_database("icaPlusDB")
