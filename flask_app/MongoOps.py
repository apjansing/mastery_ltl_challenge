import pymongo as pm
from urllib.parse import quote_plus

class MongoOps():
  """
  docstring for MongoOps
  """
  def __init__(self, username="admin", 
                  password="admin", 
                  host="mongo:27017",
                  testing=False):
    self.username = username
    self.password = password
    self.host = host
    self.uri = "mongodb://%s:%s@%s" % (quote_plus(self.username), 
                                    quote_plus(self.password), self.host)

    self.connection = pm.MongoClient(self.uri)
    self.logistics_database = self.connection.logistics_database

    self.trucks_collection = self.logistics_database.trucks
    self.shipments_collection = self.logistics_database.shipments

  def drop_table(self, collection):
    collection.drop()

  ## Leftover code froma a project of mine that could be used to add indices for geospatial querying of trucks and shipments
  # def create_loc_index(self, collection, name = "geometry", location_type = "2dsphere"):
  #     collection.create_index([(name,  location_type)])

  def _insert_one(self, collection, data):
    return collection.insert_one(data)

  def insert_truck(self, data):
    cursor = self.search_truck({"ID": data["ID"]})
    if cursor.count() > 0 :
      return False, f'Truck with ID already in database. Database reference id: {cursor.next()["_id"]}.\n'
    inserted_id = self._insert_one(self.trucks_collection, data)
    return True, inserted_id.inserted_id

  def insert_shipment(self, data):
    cursor = self.search_shipment({"ID": data["ID"]})
    if cursor.count() > 0:
      return False, f'Shipment with ID already in database. Database reference id: {cursor.next()["_id"]}.\n'
    inserted_id = self._insert_one(self.shipments_collection, data)
    return True, inserted_id.inserted_id

  def _search_collection(self, collection, search_val = None, limit = 1):
    return collection.find(search_val).limit(limit)

  def search_truck(self, id):
    return self._search_collection(self.trucks_collection, id)
    
  def search_shipment(self, id):
    return self._search_collection(self.shipments_collection, id)