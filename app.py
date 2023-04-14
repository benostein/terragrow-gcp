import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import secretmanager
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Retrieve the secret from the Secret Manager
client = secretmanager.SecretManagerServiceClient()
name = "projects/405630183099/secrets/terragrow-key/versions/latest"
response = client.access_secret_version(name=name)
key_data = response.payload.data.decode('UTF-8')
# Assuming `secret` contains the JSON formatted string
secret_dict = json.loads(key_data)
# Initialize Firestore DB
cred = credentials.Certificate(secret_dict)
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
