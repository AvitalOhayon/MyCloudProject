from flask import Blueprint, jsonify, request
from app.service import UserService


main_blueprint = Blueprint('main', __name__)
service = UserService()


@main_blueprint.route('/')
def home():
    return "Welcome to My Store Web Application!"

@main_blueprint.route('/users', methods=['GET'])
def get_users():
    results = service.get_all_users()
    results.append("kkk")
    return jsonify(results)

@main_blueprint.route('/users', methods=['POST'])
def post_users():
    data = request.get_json()

    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid input, 'id' and 'name' are required"}), 400

    user_id = data['id']
    name = data['name']
    result = service.create(user_id=user_id, name=name)
    if result:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create user"}), 500

@main_blueprint.route('/users', methods=['DELETE'])
def delete_all_users():

    deleted_count = service.delete_all()
    return jsonify({"Deleted count" : deleted_count}), 200