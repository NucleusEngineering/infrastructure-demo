import os

from flask import Flask
from google.cloud import firestore

app = Flask(__name__)

@app.route('/')
def hello_world():
    '''Example Hello World route.'''
    name = os.environ.get('NAME', 'World')
    return f'Hello {name}!'

@app.route('/db')
def db_query():
    db = firestore.Client(project=os.environ.get('PROJECT_ID'))
    doc_ref = db.collection(os.environ.get('FS_COLLECTION', 'items')).document(os.environ.get('FS_DOCUMENT', 't-shirt'))
    doc = doc_ref.get()

    return doc.to_dict()[os.environ.get('FS_ATTRIBUTE', 'name')]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
