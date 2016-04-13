from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
	return "<h1>test page<h1>"

@app.route("/<username>")
def show_user_profile(username):
	return '<h1>use %s</h1>' %username

@app.route("/<int:post_id>")
def show_post(post_id):
	return "<h1>post %d</h1>" %post_id

app.debug=True
app.run(host="0.0.0.0",port=80)