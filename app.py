from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data2.db"
db=SQLAlchemy(app)
app.app_context().push()
class Data(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    phone=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    password=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self)->str:
        return f"{self.name}-{self.password}"
    
@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='POST':
        name=request.form["name"]
        mob=request.form["phone"]
        email=request.form["email"]
        password=request.form["password"]
        data=Data(name=name,phone=mob,email=email,password=password)
        db.session.add(data)
        db.session.commit()
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
    