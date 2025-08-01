from flask import Blueprint, request, render_template, make_response, g
from uuid import uuid4
import json
from config import *
from helper import *

api = Blueprint("api", __name__)

@api.route("/", methods=["GET", "POST"])
def test():
	if "user" in request.cookies:
		user = request.cookies['user']
	else:
		user = str(uuid4())

	choice = request.cookies.get('choice')
	response_data = {"cat":0, "dog":0}
	if choice in response_data:
		response_data[choice] = -1
	if request.method == 'POST':
		choice = request.form.get("choice", "")
		response_data[choice] += 1

		# print(response_data)
		r = get_redis()
		r.setex(user, CACHE_EXPIRY, json.dumps(response_data))
		
	resp = make_response(render_template("index.html", choice=choice))
	resp.set_cookie("user", user)
	if choice:
		resp.set_cookie("choice", choice)
	return resp