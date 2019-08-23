from flask import jsonify

def api_response(message, code, data_obj={}):
    return jsonify({
        'message': str(message),
        'status_code': int(code),
        'data': data_obj
    })