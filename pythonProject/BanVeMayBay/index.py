from flask import render_template, request, redirect, url_for
from pythonProject.BanVeMayBay import app,dao,login
from pythonProject.BanVeMayBay.admin import *
from pythonProject.BanVeMayBay.models import User

@app.route("/")
def index():
    giatrikeyword = request.args.get('keyword')

    return render_template("index.html")

@app.route('/admin/login', methods=['post'])
def admin_login():
    u = request.form.get('username')
    p = request.form.get('password')
    layTT = User.query.filter_by(username=u, password=p).first()
    if layTT:
            return redirect('congraview')
    else:
        return 'dang nhap that bai'




@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)
