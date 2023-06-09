import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the private key file of the service account directly.
cred = credentials.Certificate('firebase_key.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("laptops").document("1")
doc_ref.set(
    {
        "name": "HP EliteBook Model 1",
        "brand": "HP",
    }
)

col_ref = db.collection("laptops")
col_ref.add(
    {
        "name": "Lenovo ThinkPad Model 1",
        "brand": "Lenovo",
    }
)
