from pymongo import MongoClient
from bson.objectid import ObjectId
#
# CRUD (Create, Read, Update, Delete) Module created by
#   Jeremy Reaban (based on provided template which was just init and read)
#   SNHU-340
#
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER is passed to object when instantized
        #PASS is passed to object when instantized
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32520
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection Successful")
        

# Method to implement the C(create) in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Method to implement the R(Read) in CRUD.
    def read(self, data):
        if data is not None:
            results = self.database.animals.find(data)  # data should be dictionary
            # results is a cursor object that contains a list
            # of documents in JSON format, I believe
            return results            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    
            
# Method to implement the U(Update) in CRUD.
    def update(self, data, replacementData):
        if data is not None:
            # We want to update the fields, not replace the whole
            # docuemtn, so we use $set
            repFields = {"$set": replacementData}
            # 
            # call the  update_many method
            results = self.database.animals.update_many(data,repFields)  # data should be dictionary
            # results here is a pymongo results object
            # which has the property .modified_count that tells
            # the number of documents modified. We want to return that
            numResults = results.modified_count
            return numResults   
                       
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Method to implement the D(Delete) in CRUD.
    def delete(self, data):
        if data is not None:
            results = self.database.animals.remove(data)  # data should be dictionary
            #We want to return the number of deleted documents
            # In this case results is a dictionary
            # where "n" has a value equal to the number of documents
            # deleted, so we use .get to get that and return it
            numResults = results.get("n")
            return numResults            
        else:
            raise Exception("Nothing to save, because data parameter is empty")