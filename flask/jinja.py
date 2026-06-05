from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}"
    return render_template("form.html")
@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res="PASSed"
    else:
        res="FAILed"
    return render_template("result.html", result=res)
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSed"
    else:
        res="FAILed"
    exp={"score":score, "res":res}
    return render_template("result1.html", result=exp)
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result.html", result=score)
@app.route('/fail/<int:score>')
def fail(score):

    return render_template("result.html", result=score)
@app.route('/submitres', methods=['GET', 'POST'])
def submitres():
    total=0
    if request.method=="POST":
        sci=float(request.form["science"])
        mth=float(request.form["maths"])
        c=float(request.form['c'])
        ds=float(request.form['ds'])

        total=(sci+mth+c+ds)/4
    else:
        return render_template("getresults.html")
    return redirect(url_for("successres", score=total))

if __name__=="__main__":
    app.run(debug=True)
