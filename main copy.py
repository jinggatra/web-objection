from flask import Flask, url_for
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

app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/websiteapp','websiteapp',views.websiteapp)
app.add_url_rule('/website','website',views.website,methods=['GET','POST'])

if __name__ == "__main__":
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        run_with_ngrok(app)
        app.run()

# @app.route('/base')
# @app.route('/')
# def index():
#     if __name__ == "__main__":
#         warnings.filterwarnings("ignore", category=DeprecationWarning)
#         run_with_ngrok(app)
#         app.run()
#     return 'Web Object Detection'
        
# @app.route('/websiteapp')
# def websiteapp():
#     return 'WebsiteApp'


# @app.route('/website')
# def website():
#     return 'Detection Process'