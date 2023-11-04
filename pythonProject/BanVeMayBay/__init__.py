from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_admin import Admin

app = Flask(__name__)
app.secret_key = "@@@@@@@"  # khong bi loi cho add
# cau hinh ket noi voi mysql
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/flightweb' % quote('admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)

admin = Admin(app=app, name="QUẢN TRỊ HÀNG HÀNG KHÔNG", template_mode="bootstrap4")
