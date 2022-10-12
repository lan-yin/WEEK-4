from flask import Flask  # 載入 Flask
from flask import request  # 載入 Request
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__, static_folder="public", static_url_path="/")  
app.secret_key = "noOneKnows"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        return redirect("/member")  # 要的是網址，就要傳網址重新導向，不是傳檔案
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error")
def error():
    mesg = request.args.get("message")
    return render_template("error.html", mseg = "帳號、或密碼輸入錯誤")


@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("/")

# 啟動網站伺服器
app.run(port=3000)