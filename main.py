from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="template")

todos = [{"task": "WC schoonmaken","last_done": 0, "interval": 7}]



@app.route("/")
def index():
    return render_template("base.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['task']
    interval = request.form['interval']
    todos.append({"task": todo,"last_done": interval, "interval": interval})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["task"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

@app.route("/done/<int:index>", methods=["GET","POST"])
def done(index):
    if request.method == "POST":
        todos[index]['last_done'] = 0
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug="True")