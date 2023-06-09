import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore client
cred = credentials.Certificate('firebase_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/')
def get_data():
    # Get a reference to a Firestore collection
    collection_ref = db.collection('laptops')

    # Query documents in the collection
    docs = collection_ref.get()

    # Process and display the data
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    
    return {'data': data}  # Return data as JSON response
