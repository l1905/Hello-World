import os
from flask import Flask,request,redirect,url_for
from werkzeug import secure_filename
from flask import send_from_directory,render_template
from flask.ext.sqlalchemy import SQLAlchemy
UPLOAD_FOLDER='/home/work/upload'
ALLOWED_EXTENSIONS=set(['txt','pdf'])
import json

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:l1905@localhost/flask'
db=SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
class mem(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	swpd=db.Column(db.String(80),unique=True)
	free=db.Column(db.String(120),unique=True)
	buff=db.Column(db.String(12),unique=True)
	def __init__(self,swpd,free,buff):
		self.swpd=swpd
		self.free=free
		self.buff=buff
	def __repr__(self):
		return '<user mem>'
db.create_all()
@app.route('/',methods=['GET','POST'])
def upload_file():
	if request.method=='POST':
		db.drop_all()
		db.create_all()
		file1=request.files['file']
		source1=json.load(file1)
		qq=mem(source1['swpd'],source1['free'],source1['buff'])
		db.session.add(qq)
		db.session.commit()
@app.route('/show_data')
def show_data():
	mem_show=mem.query.filter_by(id=1).first()
	com1=mem_show.swpd
	com2=mem_show.free
	com3=mem_show.buff
	return render_template('show_data.html',com1=com1,com2=com2,com3=com3)

#		if file1 and allowed_file(file1.filename):
#			filename =secure_filename(file1.filename)
#			file1.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#
#			source1=json.load(file1)
#			db.create_all()
#			qq=mem(source1['swpd'],source1['free'],source1['buff'])
#			db.session.add(qq)
#			db.session.commit()
#			return redirect(url_for('uploaded_file',filename=filename))
#		else:
#			return "no exit"
#	return '''
#	<!doctype html>
#	<title> Upload new File</title>
#	<h1> Upload new File </h1>
#	<form action="" method=post enctype=multipart/form-data>
#	  	<p><input type=file name=file>
#	  		<input type=submit value=Upload>
#	</form>
#	'''
#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
#	return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
if __name__=='__main__':
	app.run()
