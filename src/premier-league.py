from  flask  import  Flask , render_template, jsonify, json, url_for, redirect, request
import urllib
import urlparse
app = Flask(__name__)

# This is an index route.
@app.route('/')
def index():
    return render_template("index.html")

# This is a teams route.
@app.route('/teams/')
def teams():
    json_data=open('static/data.json').read()
    data= json.loads(json_data)
    return render_template("teams.html", results=data)
	
# This is as single team route.
@app.route('/<team_name>/')
def team(team_name):
    json_data=open('static/data.json').read()
    team= json.loads(json_data)
    return render_template("team.html", team=team, team_name=team_name)	
	
# This is a stadiums route.
@app.route('/stadiums/')
def stadiums():
    json_data=open('static/stadiums.json').read()
    stadium= json.loads(json_data)
    return render_template("stadiums.html", results=stadium)
	
# This is a single stadium route.
@app.route('/<team_name>/<stadium_name>/')
def stadium(team_name, stadium_name):
    json_data=open('static/data.json').read()
    team= json.loads(json_data)
    json_data=open('static/stadiums.json').read()
    stadium= json.loads(json_data)
    return render_template("stadium.html", stadium=stadium, stadium_name=stadium_name, team=team, team_name=team_name)
		


# This is a rankings route.
@app.route('/rankings/')
def rankings():
    return render_template("rankings.html")
	
# This is a table route.
@app.route('/table/')
def table():
    json_data=open('static/table.json').read()
    data= json.loads(json_data)
    return render_template("table.html", results=data)
		
if __name__  == "__main__":
	app.run(host='0.0.0.0 ', debug=True)
	
