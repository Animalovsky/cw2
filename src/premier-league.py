from  flask  import  Flask , render_template, jsonify, json, url_for, redirect, request
from logging.handlers import RotatingFileHandler
import ConfigParser
import logging

app = Flask(__name__)

# This is an index route.
@app.route('/')
def index():
    this_route = url_for('.index')
    app.logger.info("Logging a test message from " + this_route)
    return render_template("index.html")
	
# This is a teams route.
@app.route('/teams/')
def teams():
    this_route = url_for('.teams')
    app.logger.info("Logging a test message from " + this_route)
    json_data=open('static/data.json').read()
    data= json.loads(json_data)
    return render_template("teams.html", results=data)
	
# This is as single team route.
@app.route('/Team/<team_name>/')
def team(team_name):
    json_data=open('static/data.json').read()
    team= json.loads(json_data)
    return render_template("team.html", team=team, team_name=team_name)	
	
# This is a stadiums route.
@app.route('/stadiums/')
def stadiums():
    this_route = url_for('.stadiums')
    app.logger.info("Logging a test message from " + this_route)
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
    this_route = url_for('.rankings')
    app.logger.info("Logging a test message from " + this_route)
    return render_template("rankings.html")
	
# This is a table route.
@app.route('/table/')
def table():
    this_route = url_for('.table')
    app.logger.info("Logging a test message from " + this_route)
    json_data=open('static/table.json').read()
    data= json.loads(json_data)
    return render_template("table.html", results=data)
	
# 404 - Error handling.	
@app.errorhandler(404)
def page_not_found(error):
    this_route = url_for('.page_not_found')
    app.logger.info("Logging a test message from " + this_route)
    return render_template('404.html'), 404
	
# Logging application	
def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024 * 1024 * 10 , backupCount=1024)
    file_handler.setLevel(app.config['log_level'])
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel(app.config['log_level'])
    app.logger.addHandler(file_handler)		
		
# Config for the app		
@app.route('/config/')
def config():
  str = []
  str.append('Debug:'+app.config['DEBUG'])
  str.append('port:'+app.config['port'])
  str.append('url:'+app.config['url'])
  str.append('ip_address:'+app.config['ip_address'])
  return '\t'.join(str)

def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/logging.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
		
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")

        app.config['log_file'] = config.get("logging", "name")
        app.config['log_location'] = config.get("logging", "location")
        app.config['log_level'] = config.get("logging", "level")
    except:
        print "Could not read configs from: ", config_location

if __name__ == '__main__':
    init(app)
    logs(app)
    app.run(
        host=app.config['ip_address'],
        port=int (app.config['port']))

	
	
