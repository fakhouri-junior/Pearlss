from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def homePage():
    return render_template('index1.html')


@app.route('/test')
def showTest():
    return render_template('test.html')

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
