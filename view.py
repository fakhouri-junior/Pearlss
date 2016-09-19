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

app.config['MAIL_SERVER']='smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'no-reply@pearlsgm.com'
app.config['MAIL_PASSWORD'] = 'noreply##!!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

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
        admin_message = 'Hello this is  Admin, A user has contacted you with the following information, please reply\n' \
                        'name: '+name+'\n' \
                        'email: '+email+'\n' \
                        'subject: '+subject+'\n'\
                        'message: '+message+'\n'



        msg = Message('Hello', sender = 'no-reply@pearlsgm.com', recipients = ['info@pearlsgm.com'])
        msg.body = admin_message
        mail.send(msg)

        new_msg = Message('Hello', sender='no-reply@pearlsgm.com', recipients = [email])
        new_msg.body = 'Please Do not Reply\n' \
        'This is an automatic response\n' \
        'The staff will contact you soon\n' \
        'Thank you'
        mail.send(new_msg)

        flash('Your message has been sent')
        return redirect(url_for('homePage'))
    else:
        return "REJECTED"

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
