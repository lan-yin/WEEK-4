from flask import Flask, request, redirect, render_template, session, url_for


app = Flask(__name__, static_folder="public", static_url_path="/")  
app.secret_key = "noOneKnows"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods = ["POST", "GET"])
def signin():
    user = request.form["user"]
    password = request.form["password"]
    if user == "test" and password == "test":
        session["username"] = user
        return redirect("/member")  # 要的是網址，就要傳網址重新導向，不是傳檔案
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if "username" in session:
        usernsme = session["username"]
        if usernsme == "test":
            return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    mseg = request.args.get("message")
    return render_template("error.html", message = mseg)


@app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect("/")


@app.route("/input", methods = ["POST", "GET"])
def input():
    if request.method == "POST":
        return redirect(url_for("square", number = request.form.get("number")))

@app.route("/square/<number>")
def square(number):
    result = str(int(number) ** 2)
    return render_template("square.html", result = result, number = number)



# 啟動網站伺服器
app.run(port=3000)



