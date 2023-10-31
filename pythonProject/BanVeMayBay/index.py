from flask import  render_template,request
from BanVeMayBay import app
from BanVeMayBay.admin import *
@app.route("/")
def index():
    giatrikeyword = request.args.get('keyword')

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)