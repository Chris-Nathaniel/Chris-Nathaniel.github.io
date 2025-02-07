from flask import Flask, render_template, request, session, redirect, flash, jsonify, current_app, url_for
import shutil
import os
import random


app = Flask(__name__)
GIFS = {
    "annoyed": "static/images/annoyed.gif",
    "drink": "static/images/drink.gif"
}
EXECUTE_FILE = "static/images/execute.gif"

last_gif = None

def get_gif():
    global last_gif
    """Deletes execute.gif and copies the new gif as execute.gif"""
    random_gif = random.choice(list(GIFS.values()))
    while random_gif == last_gif:
        random_gif = random.choice(list(GIFS.values()))
    last_gif = random_gif
    return random_gif

def update_gif():
    gif = get_gif()
    if os.path.exists(EXECUTE_FILE):
        os.remove(EXECUTE_FILE)
    shutil.copy(gif, EXECUTE_FILE)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/choices")
def change_gif():
    update_gif()
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()