
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    response = jackson_family.get_member(member_id)
    return jsonify(response), 200

@app.route('/member', methods=['POST'])
def add_member_by_name():
    body = request.json
    response = jackson_family.add_member(body)
    return jsonify(response), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member_by_id(member_id):
    response = jackson_family.delete_member(member_id)
    return jsonify(response), 200



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
