import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://udacity-project2-flaskweb-mongodb:GBkBaf7AE5eIKV0OdpkiKobadaIhD2AYy388Py2kfx8PriE65E5FMbXF8GJNWUecby7d3SgPRMfVYEcOVRt6RQ==@udacity-project2-flaskweb-mongodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@udacity-project2-flaskweb-mongodb@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['flaskwebdatabase']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

