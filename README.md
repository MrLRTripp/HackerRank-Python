# HackerRank-Python

Solutions to Python challenge questions on HackerRank.com

Challenge questions are a good way to think about and practice concepts that you don't run across very often.  
Maybe it is something in the built-in functions, types and exceptions. Maybe it is in one of the powerful standard libraries. There is always something new to learn!

**photos db.py**  
Use PostgreSQL to store and retrieve photo thumbnails. PostgreSQL can store the photo data as a byte array (bytea type).  
Use the psycopg2 module to connect to a PostgreSQL database hosted on Azure.  
Create table.  
Insert photo data into table.  
Query the table to retrieve the photo data and then show it.  

**photos Azure Cosmos MongoDB.py**  
Use MongoDB to store and retrieve photo thumbnails. MongoDB can store the photo data as BSON binary.  
Use the pymongo module to connect to an Azure Cosmos database using the MongoDB API.  
Create database.  
Create collection.  
Create a document with the photo data and insert it into the collection.  
Query the collection to retrieve the photo data and then show it.  

**photos mongo gridfs.py**  
Use MongoDB to store and retrieve photo thumbnails. MongoDB can store the photo data as BSON binary.  Use GridFS to store full-size photos.  
Use the pymongo module to connect to an Azure Cosmos database using the MongoDB API.  
Create database.  
Create collection.
Create gridfs.  
Put full-size photo into gridfs.  
Create a document with the photo data and gridfs _id and insert it into the collection.  
Query the collection to retrieve the thumbnail photo data and then show it.  
Get the full-size photo data from gridfs and then show it.  
