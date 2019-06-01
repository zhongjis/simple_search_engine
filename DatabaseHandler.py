import pymongo

# this class handles all actions about the database
# database used here is Mongodb
class DatabaseHandler:

    def __init__(self):
        try:
            self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            print('[Success] MongoDB connected')
        except:
            print('[Fail] Cannot connect to MongoDB')


    def connect(self, dbname, colname):
        # connect to db instance
        self.mydb = self.myclient[dbname]

        # create table
        collist = self.mydb.list_collection_names()
        if colname in collist:
            print("[Warning] The collection exists. dropping the old collection")
            try:
                self.mydb.drop_collection(colname)
                print("[Success] Old collection dropped")
            except:
                print("[Fail] Cannot drop old collection")
        
        self.mycol = self.mydb['inverted_index_table']
        print("[Success] Created new collection .." + colname + ".. under " + dbname)


    def insert(self, item):
        result = self.mycol.insert_one(item)
        return result

    # this method will seach the database for the documents including the query term
    def search(self, query):
        good_records = set() # files that includes query
        col_items = self.mycol.find()
        for col_item in col_items:
            for k, v in col_item.items():
                if query in k or query == k: 
                    good_records.add((k, v))
        return good_records