# Azure Cosmos database using MongoDB API.
# https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/
#
# Azure Cosmos is a multi-model database. You can choose several NoSQL models as well as PostgreSQL relational DB. 
# For this example, we will use the MongoDB API to create a document database as well as a GridFS.
#
# Currently, PyMongo is the most popular MongoDB driver for the Python language. https://www.mongodb.com/docs/drivers/pymongo/
# Use Anaconda to install pymongo.
#
# Read photo from local drive
# Use the Mongo GridFS to store the full-size photos.
# Add the GridFS _id to the photos doc.
# Create thumbnail, write thumbnail to photos Collection.
# Query the photos Collection to get thumbnail photo data and display it.
# Use the GridFS _id to get the full-size photo data and metadata and display it.



from PIL import Image
import pymongo
import gridfs
from bson.binary import Binary
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

def create_db(client, db_name):
    # Create database if it doesn't exist
    db = client[db_name]
    if db_name not in client.list_database_names():
        # Use Azure Cosmos MongoDB API extension to create a database 
        db.command({"customAction": "CreateDatabase"})
        print(f"Created db {db_name}.\n")
    else:
        print(f"Using database: {db_name}.\n")

    return db

def create_collection(db, collection_name):
    collection_name = 'photos'
    # Create collection if it doesn't exist
    collection = db[collection_name]
    if collection_name not in db.list_collection_names():
        # Use Azure Cosmos MongoDB API extension to create a collection 
        db.command(
            {"customAction": "CreateCollection", "collection": collection_name}
        )
        print(f"Created collection {collection_name}.\n")
    else:
        print(f"Using collection: {collection_name}.\n")

    return collection

def rotate_image(img_file):
    try:
        img = Image.open(img_file)
        img = img.rotate(-90) # Need to rotate photo to get it vertical

    except FileNotFoundError as err:
        print(f'Count not find: {img_file}')
        img = None
        raise err

    finally:
        return img

def insert_into_gridfs(fs, img, photo_name):
    img_bytes = img.tobytes()
    metadata = {'mode':img.mode, 'x_size' : img.size[0], 'y_size' : img.size[1]}

    file_id = fs.put(img_bytes, metadata=metadata,filename=f'{photo_name}.bytes')

    return file_id

def create_thumbnail_image(img):
    size = 128,128
    img.thumbnail(size) # In place transformation

    return img

def insert_into_photo_collection(collection, thumb_img, photo_name, file_id):
    photo_doc_with_id = {'name': photo_name,
            'metadata' : {'mode':thumb_img.mode, 'x_size' : thumb_img.size[0], 'y_size' : thumb_img.size[1]},
            'thumbnail_photo_data': Binary(thumb_img.tobytes()),
            'file_id': file_id}

    result = collection.insert_one(photo_doc_with_id)
    return result.inserted_id

def get_thumbnail_from_collection(collection, photo_name):
    find_result = collection.find_one({'name': photo_name})
    m = find_result['metadata']
    img2 = Image.frombytes(mode=m['mode'], size=(m['x_size'],m['y_size']), data=find_result['thumbnail_photo_data'])

    return img2
    
def get_full_size_from_gridfs(collection, photo_name, fs):
    find_result = collection.find_one({'name': photo_name})
    grid_out = fs.get(find_result['file_id'])
    grid_out.metadata
    photo_data = grid_out.read()
    img = Image.frombytes(mode=grid_out.metadata['mode'], size=(grid_out.metadata['x_size'],grid_out.metadata['y_size']), data=photo_data)

    return img

if __name__ == '__main__':

    test_image_file = r'E:\Pictures\Passport raw.JPG'
    photo_name = Path(test_image_file).stem

    try:
        # Connect to db
        client = db_conn()

        # Create or use existing db
        db = create_db(client, db_name='digital_assets')

        # Create or use existing collection
        collection = create_collection(db, 'photos')

        # Open the local file and rotate it
        img = rotate_image(test_image_file)

        # Create gridfs
        gf_db = create_db(client, db_name='photo_files')
        fs = gridfs.GridFS(gf_db)

        # put data to gridfs
        gridfs_id = insert_into_gridfs(fs, img, photo_name)
        
        # Create thumbnail
        thumb = create_thumbnail_image(img)

        # Insert thumbnail into photos db
        insert_into_photo_collection(collection, thumb, photo_name, gridfs_id)

        # Close source images
        img.close()
        thumb.close()

        # Query photos db and show thumbnail
        thumb_img = get_thumbnail_from_collection(collection, photo_name)
        thumb_img.show()

        # Get full-size photo and show it
        full_size = get_full_size_from_gridfs(collection, photo_name, fs)
        full_size.show()

        # Close images
        thumb_img.close()
        full_size.close()

    except (Exception) as error:
        print(error)

    finally:
        if client is not None:
            client.close()
            print('Database connection closed.')

