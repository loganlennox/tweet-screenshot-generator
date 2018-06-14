import os
import imgkit

BASEDIR = os.path.dirname(os.path.realpath(__file__))
USERDIR = os.getcwd()

def generate_tweet(name, username, body):
    with open(BASEDIR + "/tweet_template/template.html", "r") as file:
        data = file.read()
        data = data.replace("_BASEDIR_", BASEDIR)
        data = data.replace("_name_", name)
        data = data.replace("_username_", username)
        data = data.replace("_body_", body)

    options = {"format": "png", "width": 640}

    imgkit.from_string(data, USERDIR + "/tweet.png", options = options)
