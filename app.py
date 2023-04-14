import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import json

app = Flask(__name__)

dict_key = {
        "type": "service_account",
        "project_id": "terragrow-1",
        "private_key_id": "{}".format(os.environ.get('PRIVATE_KEY_ID')),
        "private_key": "{}".format(os.environ.get('PRIVATE_KEY')),
        "client_email": "{}".format(os.environ.get('CLIENT_EMAIL')),
        "client_id": "{}".format(os.environ.get('CLIENT_ID')),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "{}".format(os.environ.get('CLIENT_X509_CERT_URL'))
    }

# Initialize Firestore DB
cred = credentials.Certificate(dict_key)
default_app = initialize_app(cred)
db = firestore.client()
plant_ref = db.collection('plants')


@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        plant_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        plant : Return document that matches query ID.
        all_plants : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        plant_id = request.args.get('id')
        if plant_id:
            plant = plant_ref.document(plant_id).get()
            return jsonify(plant.to_dict()), 200
        else:
            all_plants = [doc.to_dict() for doc in plant_ref.stream()]
            return jsonify(all_plants), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        plant_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        plant_id = request.args.get('id')
        plant_ref.document(plant_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
