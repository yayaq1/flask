from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Select the database where the collections will be created
db = client['prolution_analysis']

# Insert a document into the 'imports' collection
db.imports.insert_one({
    "module_name": "os",
    "imported_elements": [{"name": "path", "alias": "path"}],
    "is_relative": False,
    "file_location": "/src/flask/app.py"
})

# Insert a document into the 'functions' collection
db.functions.insert_one({
    "name": "my_function",
    "parameters": [{"name": "param1", "type": "String"}],
    "return_type": "None",
    "body": "print(param1)",
    "comments": ["This is a sample function"],
    "file_location": "/src/flask/app.py"
})

# Insert a document into the 'classes' collection
db.classes.insert_one({
    "name": "MyClass",
    "methods": ["function_id_1", "function_id_2"],
    "attributes": [{"name": "attr1", "type": "String"}],
    "base_classes": ["BaseClass"],
    "comments": ["This is a sample class"],
    "file_location": "/src/flask/app.py"
})
