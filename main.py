from flask import Flask, render_template, request, session, redirect, flash, jsonify, current_app, url_for
import shutil
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

GIFS = {
    "annoyed": "static/images/annoyed.gif",
    "drink": "static/images/drink.gif"
}
EXECUTE_FILE = "static/images/execute.gif"

def update_gif(gif_name):
    """Deletes execute.gif and copies the new gif as execute.gif"""
    if os.path.exists(EXECUTE_FILE):
        os.remove(EXECUTE_FILE)
    shutil.copy(GIFS[gif_name], EXECUTE_FILE)


@app.route("/<action>")
def change_gif(action):
    print(action)
    if action in GIFS:
        update_gif(action)
        return render_template('index.html')
    return "Invalid action", 404

if __name__ == '__main__':
    app.run()