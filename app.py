

from flask import Flask, render_template, request
import type as m 



app = Flask(__name__)


@app.route("/",methods= ["GET","POST"])
def marks():
    if request.method == "POST":
        hrs = request.form['hrs']
        marks_pred =m.marks_prediction(hrs)
        msk = marks_pred
        return render_template("index.html",my_marks = msk)

    return render_template("index.html")

# @app.route("/submit",methods=['POST'])
# def submit():
#     if request.method=="POST":
#         name = request.form["username"]

#     return render_template("submit.html",name=name)

if __name__ == "__main__":
    app.run(debug=True)