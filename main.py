import requests
import configparser
from flask import Flask, url_for, request, render_template
from app import views
from flask_ngrok import run_with_ngrok
import tensorflow as tf
# Warning
import warnings

app = Flask(__name__, 
                template_folder='templates/', 
                static_folder='static/'
            )

# app.add_url_rule('/predict', 'predict', views.predictpage, methods=['POST', 'GET'])

# app.add_url_rule('/base','base',views.base)
# app.add_url_rule('/','index',views.index)
# app.add_url_rule('/websiteapp','websiteapp',views.websiteapp)
# app.add_url_rule('/website','website',views.website,methods=['GET','POST'])

# if __name__ == "__main__":
#         warnings.filterwarnings("ignore", category=DeprecationWarning)
#         run_with_ngrok(app)
#         app.run()

@app.route('/base','base',views.base)
def base():
    return render_template('base.html')

@app.route('/','index',views.index)
def index():
    return render_template('index.html')
        
@app.route('/websiteapp','websiteapp',views.websiteapp)
def websiteapp():
    return render_template('websiteapp.html')


@app.route('/website','website',views.website,methods=['GET','POST'])
def website():
    return render_template('website.html')

if __name__ == "__main__":
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        run_with_ngrok(app)
        app.run()