from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to this flask course"
@app.route("/index")
def index():
    return "welcome to  flask course"

if __name__=="__main__":
    app.run(debug=True)
