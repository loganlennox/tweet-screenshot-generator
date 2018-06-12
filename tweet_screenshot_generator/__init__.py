import os
import imgkit

BASEDIR = os.path.dirname(os.path.realpath(__file__))
USERDIR = os.getcwd()

def generate_tweet():
    imgkit.from_url(BASEDIR + "/tweet_template/template.html",
                    USERDIR + "/tweet.png",
                    options = {"format": "png", "width": 640})
