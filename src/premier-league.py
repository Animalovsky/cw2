from  flask  import  Flask , render_template, jsonify, json, url_for, redirect, request
app = Flask(__name__)

# This is an index route.
@app.route('/')
def index():
    return render_template("index.html")
	
if __name__  == "__main__":
	app.run(host='0.0.0.0 ', debug=True)