from flask import Flask
app = Flask(__name__)

@app.route("/forward")
def forward():
  return "forward"

@app.route("/back")
def back():
  return "back"

@app.route("/turnleft")
def turnleft():
  return "turnleft"

@app.route("/turnright")
def turnright():
  return "turnright"

@app.route("/walk")
def walk():
  return "walk"

@app.route("/rotate")
def rotate():
  return "rotate"

@app.route("/lieflat")
def lieflat():
  return "lieflat"

@app.route("/getup")
def getup():
  return "getup"

@app.route("/shakehead")
def shakehead():
  return "shakehead"

@app.route("/wave")
def wave():
  return "wave"

@app.route("/point")
def point():
  return "point"

@app.route("/typestuff")
def typestuff():
  return "typestuff"

@app.route("/liedown")
def liedown():
  return "liedown"

@app.route("/nightfever")
def nightfever():
  return "nightfever"

@app.route("/dancetilt")
def dancetilt():
   return "dancetilt"

@app.route("/squat")
def squat():
  return "squat"

@app.route("/thriller")
def thriller():
  return "thriller"

@app.route("/curlup")
def curlup():
  return "curlup"

app.run(host='0.0.0.0')
