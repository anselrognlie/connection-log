from flask import Blueprint, request, make_response

bp = Blueprint("log", __name__)

@bp.get("/")
def index():
    print(f"request from: {request.remote_addr}")

    response = make_response("", 204)
    return response