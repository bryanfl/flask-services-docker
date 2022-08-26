from flask import jsonify

def response(code, data):

    return jsonify({
        "code_result": code,
        "resopnse_result": data
    })

