
from flask import Blueprint,request,make_response,flash, current_app, redirect, send_from_directory, url_for,send_file, render_template, render_template_string
import uuid
import os
import io
import random
from flask_mail import Message
from app import mail

app = Blueprint('views',__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.get('/resume')
def resume():
    return render_template('resume.html')

@app.route('/skills')
def skills():
    # pass
    return render_template('skills.html')

@app.route('/internship-experience')
def intern_experience():
    return render_template('intern_experience.html')

@app.get('/education')
def education():
    return render_template('education.html')


@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/seminars')
def seminars():
    return render_template('seminars.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def projects():
    return render_template('projects.html')

@app.get('/certificate-capstone')
def certificate_capstone():
    return send_from_directory('static', 'capstone_certificate.jpg', mimetype='image/jpeg')


@app.get('/certificate-appreciation-first')
def certificate_appreciation_first():
    return send_from_directory('static', 'certificate1.jpg', mimetype='image/jpeg')

@app.get('/certificate-appreciation-second')
def certificate_appreciation_second():
    return send_from_directory('static', 'certificate2.png', mimetype='image/jpeg')

@app.route('/certificate-ojt')
def certificate_ojt():
    return send_from_directory('static', 'ojt_certificate.jpg', mimetype='image/jpeg')

@app.get('/download-pdf')
def download_pdf():
   return send_from_directory('static', 'cv.pdf', as_attachment=True)


# send mail 
@app.route('/send-mail', methods=['POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('message')
        new_msg = Message(
            subject=name,
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=["roleplay@example.com"] #change email as needed!

        )
        new_msg.body = f'{name} {msg} {email}'
        mail.send(new_msg)
        flash('Message has been sent', category='success')
    return redirect(url_for('views.contact'))


