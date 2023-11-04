from flask import render_template, request
from Backend_ATTT.pythonProject.BanVeMayBay import app
from Backend_ATTT.pythonProject.BanVeMayBay.admin import *


@app.route("/")
def index():
    giatrikeyword = request.args.get('keyword')

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
