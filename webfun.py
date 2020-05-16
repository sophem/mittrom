#!/usr/bin/python3

import sys, os, configparser

import requests
from flask import Flask, request, render_template

from lights import Light
  
cf = configparser.ConfigParser()
cf.read('porc')

app = Flask(__name__)

def tell_sophie(message):
    d = {'token': cf.get('pushover', 'apikey'),
         'user': cf.get('pushover', 'userkey'),
         'message': message }
    requests.post('https://api.pushover.net/1/messages.json', json=d)

def access(url, secret, message=None):
    people_secrets = []
    with open('secrets', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line:
                code, user = line.split(':')
                people_secrets.append([code, user.strip()])
    
    for code, user in people_secrets:
        if code == secret:
            if message: tell_sophie(f"{user}: {message}")
            return user

    return None

@app.route("/")
def root():
    return "No."

@app.route("/<secret>/")
def index(secret):
    if not access(request.url, secret, "Besøkte siden"): return "No."
    
    lights = Light.get_lights()
    sophie_lights = []
    for light in lights:
       if 'Sophie' in light.name and not 'Panel' in light.name:
           sophie_lights.append(light)
    return render_template("index.html", lights=sophie_lights, prefix=secret)
           

@app.route("/<secret>/lights/status")
def light_status(secret):
    if not access(request.url, secret, "Sjekket status"): return "No."

    Light.refresh()
    target_light = request.args.get("target_light")
    light = Light.find_light(target_light)
    if light:
        # hvis vi kommer hit, så vet vi at vi har funnet lyset
        if light.on:
            return "Lyset er på. :-)"

        return "Lyset er av."
           
    return "Fant ikke lyset."

@app.route("/<secret>/lights/set", methods=["POST"])
def light_set(secret):
    if not access(request.url, secret): return "No."

    Light.refresh()
    user = access(request.url, secret)
    if not user: return "No."
    tell_sophie(f"{user} så status på lys")

    target_light = request.args.get("target_light")
    target_status = str(request.args.get("target_status")).lower() in ["on", "true"]
    light = Light.find_light(target_light)

    if light:
        tell_sophie(f"{user}: satt {target_light} til {target_status}")
        light.set_state(target_status)
        
        return "Skrudde lyset på" if target_status else "Skrudde lyset av"
    
    return "Fant ikke lyset."

if __name__ == "__main__":
    app.run(debug=True)
