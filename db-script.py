import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the private key file of the service account directly.
cred = credentials.Certificate('firebase_key.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

model1_doc_ref = db.collection("models").document("1")
model1_doc_ref.set(
    {
        "name": "EliteBook",
    }
)

laptop1_doc_ref = db.collection("laptops").document("1")
laptop1_doc_ref.set(
    {
        "brand": "HP",
        "tags": ["hp", "2023", "notebook"],
        "model": model1_doc_ref
    }
)

laptop2_doc_ref = db.collection("laptops")
laptop2_doc_ref.add(
    {
        "name": "Lenovo",
        "tags": ["lenovo", "2023", "ultrabook"],
        "model": db.document("models/1")
    }
)
