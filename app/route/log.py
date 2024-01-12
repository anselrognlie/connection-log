from flask import Blueprint, request, make_response
from pprint import pformat

bp = Blueprint("log", __name__)

@bp.get("/")
def index():
    print(f"request from: {request.remote_addr}")
    headers = pformat(request.headers)
    print(f"headers: {headers}")

    response = make_response("", 204)
    return response