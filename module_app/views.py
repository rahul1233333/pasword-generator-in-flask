from module_app import app
from flask import render_template,url_for,request,redirect
import random

without_symbol_characters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
with_symbol_characters = "@#$&(){}{},."
combined_characters = without_symbol_characters + with_symbol_characters
        
eran = "".join(random.sample(without_symbol_characters , 4))
sran = "".join(random.sample(without_symbol_characters , 6))
wran = "".join(random.sample(combined_characters , 9))
oran = "".join(random.sample(without_symbol_characters , 9))

@app.route('/')
def home():
    return render_template("/base/home.html")

@app.route('/email password/emailput', methods=['POST', 'GET'])
def emailput():
    if request.method == "POST":
        e = request.form['eput']
        estrip = e.strip()
        if estrip.find("@") != -1:
            usernm = estrip[:estrip.index('@')] + eran
            return redirect(url_for('epass', eget = usernm))
    else:
        return render_template("/email password/emailput.html")

@app.route('/social password/socialput', methods=['POST', 'GET'])
def socialput():
    if request.method == "POST":
        s=request.form['sput']
        socialnm = s + sran
        return redirect(url_for('spass', sget = socialnm))
    else:
        return render_template("/social password/socialput.html")

@app.route('/other password/otherput')
def otherput():
    return render_template("/other password/otherput.html")

@app.route('/email password/<eget>')
def epass(eget):
    return render_template("/email password/epass.html",eval = eget)

@app.route('/social password/<sget>')
def spass(sget):
    return render_template("/social password/spass.html" , sval = sget)

@app.route('/other password/opass')
def opass():
    return render_template("/other password/opass.html", opval = oran)

@app.route('/other password/wpass')
def wpass():
    return render_template("/other password/wpass.html", wpval = wran)
