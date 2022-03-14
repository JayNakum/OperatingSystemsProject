import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import exceptions

cred = credentials.Certificate('algorithms/jaynakum-experiments-88cc723f2db9.json')
default_app = firebase_admin.initialize_app(cred, {'storageBucket': 'jaynakum-experiments.appspot.com'})

db = firestore.client()
doc_ref = db.collection(u'CPU Scheduling').document(u'First Come First Serve')

try:
    doc = doc_ref.get()
    while(True):
        if(doc != doc_ref.get()):
            doc = doc_ref.get()
            processes = doc.to_dict()
        else:
            pass
except exceptions.NotFound:
    print('No processes found')