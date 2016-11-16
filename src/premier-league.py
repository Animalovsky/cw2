from  flask  import  Flask , render_template, jsonify, json, url_for, redirect, request
app = Flask(__name__)

# This is an index route.
@app.route('/')
def index():
    return render_template("index.html")

# This is a teams route.
@app.route('/teams/')
def teams():
    return render_template("teams.html")
	
# This is a stadiums route.
@app.route('/stadiums/')
def stadiums():
    return render_template("stadiums.html")
	
# This is a rankings route.
@app.route('/rankings/')
def rankings():
    return render_template("rankings.html")
	
# This is a table route.
@app.route('/table/')
def table():
    return render_template("table.html")
		
if __name__  == "__main__":
	app.run(host='0.0.0.0 ', debug=True)