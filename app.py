from flask import Flask, redirect, request, render_template
app = Flask(__name__)

to_do_list = [["run", False], ["do homework", False], ["practice code", False], ["go to work", False]]

@app.route("/")
def home():
    return render_template('home_page.html', todos=to_do_list)

@app.route("/new_item")
def newitem():
    return render_template('new_item.html') 

@app.route("/new_item", methods=["POST"])
def post_newitem():
    latest_item = request.form["newitem"]
    to_do_list.append(latest_item)
    return redirect("/")

@app.route('/done', methods=["POST"])
def done():
    index = int(request.form["listnumber"])
    to_do_list[index][1] = not to_do_list[index][1]
    return redirect('/')

@app.route('/delete', methods=['POST'])
def post_delete():
    list_index = int(request.form['listindex'])
    if list_index < len(to_do_list):
        to_do_list.pop(list_index)
    return redirect('/')
