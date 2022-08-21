"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def family_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def member(member_id):
    member = jackson_family.get_member(member_id)
    if member != None:
        response_body = jackson_family._serializated_member(member)
        
    if response_body != None:
        return jsonify(response_body), 200
    else:
        return jsonify("Error"), 400


@app.route('/member', methods=['POST'])
def add_member():
    
    member = {
    "id": request.json.get("id"),
    "first_name":request.json.get("first_name"),
    "age": request.json.get("age"),
    "lucky_number": request.json.get("lucky_number")
    }

    response_body = jackson_family.add_member(member)

    if response_body != None:
        return jsonify(response_body), 200
    else:
        return jsonify("Error"), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    
    response_body = jackson_family.delete_member(member_id)
    if response_body != None:
        return jsonify(response_body), 200
    else:
        return jsonify("Error"), 400
       
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
