from flask import jsonify, Response

def response_helper(message: str, code: int = 200) -> Response:
  return jsonify({
    'code': code,
    'message': message,
  }), code