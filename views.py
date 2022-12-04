from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")



#@views.route("/json")
#def get_json():
    #return jsonify({'name': 'ben', "coolness":10})

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/socials")
def socials():
    return render_template("socials.html")

@views.route('/cats')
def about_hope():
    args = request.args
    cat = args.get('name')
    if cat=='hope':
        return render_template("about_hope.html", cat=cat)
    if cat=='cuddles':
        return render_template("about_cuddles.html", cat=cat)

@views.route('')
def home():
    return render_template("index.html")