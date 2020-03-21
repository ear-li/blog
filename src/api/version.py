from flask import Blueprint, request
import json


version = Blueprint('version', __name__, url_prefix='/version')


VERSION = [
    {'v1.0.0': '第一版'},
]



@version.route('', methods=['GET'])
def get_version():
    return json.dumps(VERSION[-1], ensure_ascii=False)
