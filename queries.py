from app import db

laptops_ref = db.collection('laptops')

query1 = laptops_ref.where('tags', 'array_contains', '2023')
query2 = laptops_ref.where('tags', 'array_contains', '2023')
query1.get()
query2.get()


laptops_ref = db.collection('laptops').document('1')
laptops_ref.update({"tags": ["lenovo", "2023", "ultrabook", "intel"]})


laptops_ref = db.collection('laptops').document('1')
access1_ref = laptops_ref.collection('accessories').document("1")
access1_ref.set({"name": "mouse"})
access2_ref = laptops_ref.collection('accessories').document("1")
access2_ref.set({"name": "keyboard"})