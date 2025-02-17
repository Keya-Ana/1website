from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactus')
def index1():
    return "feel free to hit me up anytime on snap @starr.mkb"

app.run(host='0.0.0.0' ,port=80 )

# from flask import Flask ,render_template

# app = Flask(__name__) 

# @app.route('/')
# def index(): 
#     return render_template('index.html')

# @app.route('/contactus')
# def index2(): 
#     return "my email address : eulalia@gmail.com"

# app.run(host='0.0.0.0' ,port=80 )