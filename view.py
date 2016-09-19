from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

from flask_mail import Mail, Message

app = Flask(__name__)


mail = Mail(app)



@app.route('/')
@app.route('/index')
def homePage():
    return render_template('index1.html')


@app.route('/test')
def showTest():
    return render_template('test.html')


@app.route('/email', methods=['POST'])
def sendEmail():
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']
        if request.form['email']:
            email = request.form['email']
        if request.form['subject']:
            subject = request.form['subject']
        if request.form['message']:
            message = request.form['message']
        '''

        msg = Message(sender=email,
                      recipients=['ceaserfs3@gmail.com'],
                      body=message,
                      subject=subject)
        mail.send(msg)
        '''
        print "got it"
        return redirect(url_for('homePage'))
    else:
        return "REJECTED"

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
