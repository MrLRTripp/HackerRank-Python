# Azure Cosmos database using MongoDB API.
# https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/
#
# Azure Cosmos is a multi-model database. You can choose several NoSQL models as well as PostgreSQL relational DB. 
# For this example, we will use the MongoDB API to create a document database.
#
# Read photo from local drive, create thumbnail, write thumbnail to photos Collection.
# Query the photos Collection to get photo data and display it

# Currently, PyMongo is the most popular MongoDB driver for the Python language. https://www.mongodb.com/docs/drivers/pymongo/
# Use Anaconda to install pymongo.
#

from PIL import Image
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.binary import Binary
from bson.objectid import ObjectId
import yaml
from pathlib import Path

def db_conn():
    # Example yaml file format
    # mongodb:
    #     connection_string:

    with open("cosmos_mongodb_connect.yaml", mode="r", encoding="utf-8") as file:
        d = yaml.safe_load(file)['mongodb']

    try: 
        client = pymongo.MongoClient(d['connection_string'])
    except pymongo.error.PyMongoError as err:
        client = None
        print(err)
    finally:
        return client

def create_db(client):
    DB_NAME = 'digital_assets'
    # Create database if it doesn't exist
    db = client[DB_NAME]
    if DB_NAME not in client.list_database_names():
        # Use Azure Cosmos MongoDB API extension to create a database 
        db.command({"customAction": "CreateDatabase"})
        print(f"Created db {DB_NAME}.\n")
    else:
        print(f"Using database: {DB_NAME}.\n")

    return db

def create_collection(db):
    COLLECTION_NAME = 'photos'
    # Create collection if it doesn't exist
    collection = db[COLLECTION_NAME]
    if COLLECTION_NAME not in db.list_collection_names():
        # Use Azure Cosmos MongoDB API extension to create a collection 
        db.command(
            {"customAction": "CreateCollection", "collection": COLLECTION_NAME}
        )
        print(f"Created collection {COLLECTION_NAME}.\n")
    else:
        print(f"Using collection: {COLLECTION_NAME}.\n")

    return collection

def create_thumbnail_image(img_file):
    try:
        img = Image.open(img_file)
        img = img.rotate(-90) # Need to rotate photo to get it vertical
        size = 128,128
        img.thumbnail(size) # In place transformation


    except FileNotFoundError:
        img = None

    finally:
        return img

def insert_into_photo_collection(collection, img, photo_name):
    img_bytes = img.tobytes()
    mode = img.mode
    t_size = img.size

    photo_doc = {'name': photo_name,
            'mode': mode,
            'x_size': t_size[0],
            'y_size': t_size[1],
            'photo_data': Binary(img_bytes)}

    result = collection.insert_one(photo_doc)
    return result.inserted_id

def get_photo_from_collection(collection, photo_name):
    find_result = collection.find_one({'name': photo_name})
    im_size = find_result['x_size'],find_result['y_size']

    img2 = Image.frombytes(mode=find_result['mode'], size=im_size, data=find_result['photo_data'])

    return img2
    


if __name__ == '__main__':
    try:
        # Connect to db
        client = db_conn()

        # Create or use existing db
        db = create_db(client)

        # Create or use existing collection
        collection = create_collection(db)

        # Load local image file and create thumbnail
        test_image_file = r'E:\Pictures\Passport raw.JPG'
        thumb = create_thumbnail_image(test_image_file)
        
        # Insert thumbnail into photos db
        photo_name = Path(test_image_file).stem
        insert_into_photo_collection(collection, thumb, photo_name)

        # Close source image
        thumb.close()

        # Query photos db and show thumbnail
        img2 = get_photo_from_collection(collection, photo_name)
        img2.show()

        # Close thumbnail image
        img2.close()

    except (Exception) as error:
        print(error)

    finally:
        if client is not None:
            client.close()
            print('Database connection closed.')

