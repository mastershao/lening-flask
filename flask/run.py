#--*--coding:utf-8--*--
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask.ext.script import Manager   #python-srcipy
from flask.ext.bootstrap import Bootstrap

app=Flask(__name__)

bootstrap=Bootstrap(app)

@app.route("/index")
@app.route("/")
def index():
	user={'nickname':'Migurel'}
	posts=[
	{
	'author':{'nickname':'Johe'},
	'body':'Beautiful day in Protland!'
	},
	{
	'author':{'nickname':'Susan'},
	'body':'The Avengers movie was so cool!'
	}
	]
	return render_template('index.html',
		title='Home',
		user=user,
		posts=posts)

@app.route("/hello/")
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)

# 返回用户的user_agent信息
@app.route("/useragent")
def useragent():
    user_agent=request.headers.get('User_Agent')
    return '<p>Your browser is %s</p>' %user_agent

# 设置cookie
@app.route("/cookie")
def cookie():
    response=make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

# 页面重定向
@app.route('/xilai')
def xilai():
    return redirect("http://www.xilaikd.com")
# 错误重定向
@app.route('/user/<id>')
def get_user(id):
    user=['jerry','tom','jack','marry']
    if id not in user:
        return '<h1>error:404</h1>'
    return '<h1>Hello,%s</h1>' %id



app.debug=True
app.run(host="0.0.0.0",port=80)