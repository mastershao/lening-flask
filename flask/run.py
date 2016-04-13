#--*--coding:utf-8--*--
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from flask import url_for

app=Flask(__name__)

@app.route("/")
def index():
	return "<h1>test page<h1>"

@app.route("/login", methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

@app.route("/<username>")
def show_user_profile(username):
	return '<h1>use %s</h1>' %username

@app.route("/<int:post_id>")
def show_post(post_id):
	return "<h1>post %d</h1>" %post_id

# url构建
with app.test_request_context():
	print url_for('index')
	print url_for('show_user_profile',username='John Doe')
	print url_for('login',next='/')


app.debug=True
app.run(host="0.0.0.0",port=80)