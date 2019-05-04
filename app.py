# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates

from flask import Flask, render_template, request, url_for
import requests

# Initialize the Flask application
app = Flask(__name__)

camera=html = " "

@app.route('/liftoff/', methods=['GET'])
def begin():
    r = requests.get('http://10.68.54.45:5000/launch')	
    status=r.status_code
    return render_template('rocket.html')

@app.route('/arm/', methods=['GET'])
def arm():
    return render_template('main.html', camera="visibility: hidden", fueling=" ", counter="<h4>Fuel To Launch </h4>" , arm="disabled", unarm="active", fuel="active", launch="disabled" , abort="disabled")

@app.route('/fueled/<amount>', methods=['GET'])
def begin_fuel(amount):
    r = requests.get('http://10.68.54.45:5000/begin_fuel/'+ amount)	
    status=r.status_code
    ##camera_html= "visibility: hidden" 
    return render_template('main.html', camera=" ", fueling=" ", counter="<h4>Fueled        </h4>", arm="disabled", unarm="disabled", fuel="disabled", launch="active", abort="active")

@app.route('/launch/', methods=['GET'])
def launch():
    return render_template('main.html', camera=" ", fueling=" ", counter='<div class="lead", id="clock"></div>', arm="disabled", unarm="disabled", fuel="disabled", launch="disabled", abort="active")
	
@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', camera="visibility: hidden",fueling=" ", counter="<h4>Arm To Launch  </h4>", arm="active", unarm="disabled", fuel="disabled", launch="disabled", abort="disabled")


# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )

