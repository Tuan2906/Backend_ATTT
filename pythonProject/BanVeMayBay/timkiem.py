from flask import render_template, request
import os
from pythonProject.BanVeMayBay import app


@app.route("/")
# ben html thi name la thuoc tinh de nhan thong tin trong ham ma chua ten name do minh dat
# nhung python vao html thi phai co dau {{% viet lenh python%}}
# get dung cho thong tin public
# post dung cho thong tin private. Vd; password
# push lay het doi tuong
def home():
    users = [{
        "name": 'Nguyen chau A',
        "phone": '12311'
    }, {
        "name": 'Nguyen chau B',
        "phone": '1311',
    }, {
        "name": 'Nguyen duong C',
        "phone": '2311'
    }]
    ketqua = request.args.get("keyword")
    if ketqua:
        users = [u for u in users if u['name'].lower().find(ketqua.lower()) >= 0]
    return render_template("index.html", users=users)


@app.route("/thongtin")
def thongTinKH():
    return "Chuc mung ban da thanh cong!!!"


# lay duong dan + ten  de xuar
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", message="Xin chao ban %s!!!" % name)


# dung phuong thuc get de client gui yeu cau cho server phai cho dau ? truoc
@app.route("/hello")
def hello2():
    ho = request.args.get('ho', 'Ho')
    ten = request.args.get('ten', 'none')
    return render_template('index.html', message='Xin chao ban %s %s' % (ho, ten))


@app.route("/login", methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'tuan' and password == '1':
        return 'server dang bao tri'
    else:
        return 'dang nhap that bai'


@app.route("/uploadFile", methods=['post'])
def uploadFile():
    f = request.files['image']
    f.save(os.path.join(app.root_path, 'static/upload file/', f.filename))
    return 'Thanh Cong'


if __name__ == "__main__":
    app.run(debug=True)
