from flask import render_template, request
from app import app
from models.event import events
from models.event import Event
from models.event import add_new_event
import datetime as dt



@app.route("/events")
def show_task():
	return render_template("index.html", events = events)


@app.route("/events", methods=["post"])
def add_event():
	name = request.form['name']
	num = request.form['num_guests']
	room = request.form['room']
	desc = request.form['description']
	date = dt.datetime.strptime(request.form['date'], "%Y-%m-%d")
	datestring = date.strftime("%d/%m/%Y")
	
	if "recurring" in request.form:
		recurring = True
	else:
		recurring = False

	new_event = Event(datestring, name, num, room, desc, recurring)
	add_new_event(new_event)
	return render_template("index.html", events = events)
