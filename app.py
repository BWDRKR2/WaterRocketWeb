# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import requests

# Initialize the Flask application
app = Flask(__name__)

@app.route('/liftoff/', methods=['GET'])
def begin():
    r = requests.get('http://10.68.54.45:5000/launch')	
    status=r.status_code
    return render_template('rocket.html')

@app.route('/arm/', methods=['GET'])
def arm():
    ##r = requests.get('http://10.68.54.45:5000/arm')	
    ##status=r.status_code
    return render_template('main.html', fueling=" ", counter="<h4>Fuel To Launch </h4>" , arm="disabled", unarm="active", fuel="active", launch="disabled" , abort="disabled")

@app.route('/abort/', methods=['GET'])
def abort():
    r = requests.get('http://10.68.54.45:5000/abort')	
    status=r.status_code
    return render_template('abort.html')

@app.route('/fueled/<amount>', methods=['GET'])
def begin_fuel(amount):
    r = requests.get('http://10.68.54.45:5000/begin_fuel/'+ amount)	
    status=r.status_code
    return render_template('main.html', fueling=" ", counter="<h4>Fueled        </h4>", arm="disabled", unarm="disabled", fuel="disabled", launch="active", abort="active")

@app.route('/end_fuel/', methods=['GET'])
def end_fuel():
    r = requests.get('http://10.68.54.45:5000/end_fuel')	
    status=r.status_code
    return render_template('dan.html')

@app.route('/count/', methods=['GET'])
def count():
    return render_template('count.html')

@app.route('/launch/', methods=['GET'])
def launch():
    #r = requests.get('http://10.68.54.45:5000/launch')	
    #status=r.status_code
    return render_template('main.html', fueling=" ", counter='<div class="lead", id="clock"></div>', arm="disabled", unarm="disabled", fuel="disabled", launch="disabled", abort="active")
	
@app.route('/unarm/', methods=['GET'])
def unarm():
    r = requests.get('http://10.68.54.45:5000/unarm')	
    status=r.status_code
    return render_template('unarm.html')

@app.route('/dan/', methods=['GET'])
def dan():
    return render_template('slider.html')

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', fueling=" ", counter="<h4>Arm To Launch  </h4>", arm="active", unarm="disabled", fuel="disabled", launch="disabled", abort="disabled")


# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )

