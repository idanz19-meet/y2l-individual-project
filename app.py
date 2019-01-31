from flask import Flask, render_template, request
from database import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/sign_up')
def sign_up():
	return render_template("sign_up.html")

@app.route('/messages')
def messages():
	return render_template("messages.html")

@app.route('/messaging', methods =['GET', 'POST'])
def messaging():
	if request.method == "GET" :
	    return render_template("message.html")
	else:
		sender = "John_123"
		receiver = request.form['receiver_name']
		message = request.form['user_message']
		send_message(sender,receiver,message)
		return render_template("message.html")

@app.route('/thanks', methods = ['GET', 'POST'])
def thanks():
	if request.method == "GET" :
	    return render_template("thanks.html")
	else:
		user_name = request.form['user_name']
		user_password = request.form['user_password']
		user_email = request.form['user_email']

		check_user = session.query(User).filter_by(email=user_email).first()
		if check_user:
			return render_template("sorry.html")
		else:
			signup_now(user_name, user_password, user_email)
			return render_template("thanks.html")

if __name__ == '__main__':
    app.run(debug=True)

