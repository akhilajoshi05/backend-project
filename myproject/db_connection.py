import pymongo

url = 'mongodb://localhost:27017'

client = pymongo.MongoClient(url)

 
    # creating database in mongodb by writing code in pyhton
db = client['test_mongo']

#     # cretaing collection
# collection = db['user']