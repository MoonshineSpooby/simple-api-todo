from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__, url_prefix='/api/users')
USERS_DB = [{"id": 1, "name": "Alice"}]

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Fetch a user by ID with proper error handling."""
    try:
        user = next((u for u in USERS_DB if u["id"] == user_id), None)
        if not user:
            return jsonify({"error": "User not found", "code": 404}), 404
        return jsonify({"data": user, "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": "Internal server error", "code": 500}), 500
