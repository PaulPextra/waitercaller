import pymongo
from config import MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
c = client['waitercaller']
print(c.users.create_index("email", unique=True))
print(c.requests.create_index("table_id", unique=True))