from app import db

laptops_ref = db.collection('laptops')

laptops_ref.where('tags', 'array_contains', '2023').get()
laptops_ref.where('tags', 'array_contains', '2023').limit(1).get()
laptops_ref.where('tags', 'array_contains_any', ["2020", "2023"]).get()

laptops_ref = db.collection('laptops').document('1')
laptops_ref.update({"tags": ["lenovo", "2023", "ultrabook", "intel"]})


laptops_ref = db.collection('laptops').document('1')
access1_ref = laptops_ref.collection('accessories').document("1")
access1_ref.set({"name": "mouse"})
access2_ref = laptops_ref.collection('accessories').document("1")
access2_ref.set({"name": "keyboard"})


laptops_ref = db.collection('laptops').document("1")
laptops_ref.get().get("brand")

laptops_ref = db.collection('laptops').where("brand", "==", "HP").get()


laptops_ref = db.collection('laptops').document("1")
laptops_ref.get().exists
laptops_ref.delete()
