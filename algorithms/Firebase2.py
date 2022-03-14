import threading
from google.cloud import firestore
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./algorithms/jaynakum-experiments-88cc723f2db9.json"

processes = {}

db = firestore.Client()
doc_ref = db.collection(u'CPU Scheduling').document(u'First Come First Serve')


# Create an Event for notifying main thread.
callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(doc.to_dict())
        processes.clear()
        processes.update(doc.to_dict())
    # for change in changes:
    #     print(change.to_dict())
    callback_done.set()

# Watch the document
# for i in range(1, 10):
doc_watch = doc_ref.on_snapshot(on_snapshot)

callback_done.wait(timeout=10000)
doc_watch.unsubscribe()
# [END firestore_listen_detach]