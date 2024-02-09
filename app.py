from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)

gt = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
gsum = 0
grade_average = 0
groups = 0
exam = None

@app.route("/", methods=["GET", "POST"])
def index():
    global grade_average
    global groups
    global exam
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Check which radio buttons and input fields were selected/submitted
        try:
            groups = float(request.form.get('groups'))
            exam = request.form.get('exam')
            grade_average = float((request.form.get('grade_average')))
        except ValueError:
            return render_template("inputs.html")
        if groups == 4 and exam == "no": #"impossible scenario"
            return render_template("impossible.html")
        elif grade_average < 0 or grade_average > 100:
            return render_template("impossibleg.html")

        if groups == 4 and exam == "yes":
            return render_template("four_y.html")
        elif groups == 3 and exam == "yes":
            return render_template("three_y.html")
        elif groups == 3 and exam == "no":
            return render_template("three_n.html")
        elif groups == 2 and exam == "yes":
            return render_template("two_y.html")
        elif groups == 2 and exam == "no":
            return render_template("two_n.html")
        elif groups == 1 and exam == "yes":
            return render_template("one_y.html")
        elif groups == 1 and exam == "no":
            return render_template("one_n.html")

@app.route("/four_y", methods=["GET", "POST"])
def four_y():
    global gt
    global g2
    global g3
    global g4
    global gsum
    if request.method == "GET":
        return render_template("4_y.html")
    else:
        try:
            gt = float(request.form.get("exam_grade"))
            g2 = float(request.form.get("2_cat"))
            g3 = float(request.form.get("3_cat"))
            g4 = float(request.form.get("4_cat"))
            if gt > 100 or gt < 0 or g2 > 100 or g2 < 0 or g3 > 100 or g3 < 0 or g4 > 100 or g4 < 0:
                return render_template("impossibleg.html")
            gsum = (g2 + g3 + g4)
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")

@app.route("/three_y", methods=["GET", "POST"])
def three_y():
    global gt
    global g2
    global g3
    global gsum
    if request.method == "GET":
        return render_template("three_y.html")
    else:
        try:
            gt = float(request.form.get("exam_grade"))
            g2 = float(request.form.get("2_cat"))
            g3 = float(request.form.get("3_cat"))
            if gt > 100 or gt < 0 or g2 > 100 or g2 < 0 or g3 > 100 or g3 < 0:
                return render_template("impossibleg.html")
            gsum = (g2 + g3)
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")

@app.route("/three_n", methods=["GET", "POST"])
def three_n():
    global g1
    global g2
    global g3
    global gsum
    if request.method == "GET":
        return render_template("three_n.html")
    else:
        try:
            g1 = float(request.form.get("1_cat"))
            g2 = float(request.form.get("2_cat"))
            g3 = float(request.form.get("3_cat"))
            if g1 > 100 or g1 < 0 or g2 > 100 or g2 < 0 or g3 > 100 or g3 < 0:
                return render_template("impossibleg.html")
            gsum = (g2 + g3 + g1)
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")


@app.route("/two_y", methods=["GET", "POST"])
def two_y():
    global gt
    global g2
    global gsum
    if request.method == "GET":
        return render_template("two_y.html")
    else:
        try:
            gt = float(request.form.get("exam_grade"))
            g2 = float(request.form.get("2_cat"))
            if gt > 100 or gt < 0 or g2 > 100 or g2 < 0:
                return render_template("impossibleg.html")
            gsum = g2
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")

@app.route("/two_n", methods=["GET", "POST"])
def two_n():
    global g1
    global g2
    global gsum
    if request.method == "GET":
        return render_template("two_n.html")
    else:
        try:
            g1 = float(request.form.get("1_cat"))
            g2 = float(request.form.get("2_cat"))
            if g1 > 100 or g1 < 0 or g1 > 100 or g2 < 0:
                return render_template("impossibleg.html")
            gsum = (g2  + g1)
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")


@app.route("/one_y", methods=["GET", "POST"])
def one_y():
    global gt
    global gsum
    if request.method == "GET":
        return render_template("one_y.html")
    else:
        try:
            gt = float(request.form.get("exam_grade"))
            gsum = 0
            if gt > 100 or gt < 0:
                return render_template("impossibleg.html")
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")

@app.route("/one_n", methods=["GET", "POST"])
def one_n():
    global g1
    global gsum
    if request.method == "GET":
        return render_template("one_n.html")
    else:
        try:
            g1 = float(request.form.get("1_cat"))
            gsum = g1
            if g1 > 100 or g1 < 0:
                return render_template("impossibleg.html")
            grade, text = calculate()
            return render_template("result.html", grade=grade, text=text)
        except ValueError:
            return render_template("inputs.html")






def calculate():
    if exam == "yes" and ((grade_average * groups - gsum) * 2 - gt) <= 100:
        grade = round(((grade_average * groups - gsum) * 2 - gt),1)
        text = ("The term exam grade you need to get is")
    elif exam == "yes" and ((grade_average * groups - gsum) * 2 - gt) > 100:
        text = ("It is impossible to achieve your wanted average ! The term exam grade you need to get is ")
        grade = round(((grade_average * groups - gsum) * 2 - gt), 1)
    elif exam == "no" and (grade_average * (groups + 1) - gsum) <= 100:
        grade = round((grade_average * (groups + 1) - gsum), 1)
        text = ("The term exam grade you need to get is")
    elif exam == "no" and (grade_average * (groups + 1) - gsum) > 100:
        text = ("It is impossible to achieve your wanted average ! The term exam grade you need to get is ")
        grade = round((grade_average * (groups + 1) - gsum), 1)
    return grade, text






