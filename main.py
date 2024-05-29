from pymongo import MongoClient

# Step 1: Connect to the MongoDB server
client = MongoClient('mongodb://localhost:12345/')

# Step 2: Create or switch to a database
db = client['test_database']

# Step 3: Create or switch to a collection
collection = db['test_collection']

# Step 4: Insert a document into the collection
document = {"name": "John Doe", "age": 30, "city": "New York"}
result = collection.insert_one(document)
print(f"Inserted document ID: {result.inserted_id}")

# Step 5: Retrieve the document from the collection
retrieved_document = collection.find_one({"name": "John Doe"})
print("Retrieved document:", retrieved_document)

# Close the connection
client.close()
