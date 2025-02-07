from flask import Flask, render_template, request, session, redirect, flash, jsonify, current_app, url_for, send_file
import shutil
import os
import random
import time

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
    update_gif()
    return redirect('https://osu.ppy.sh/users/19921620')

@app.route('/dynamic_execute.gif')
def serve_gif():
    """Serve execute.gif with a timestamp-based cache buster."""
    update_gif()  # Ensure GIF updates
    timestamp = int(time.time())  # Get current timestamp
    return send_file(EXECUTE_FILE, mimetype='image/gif', cache_timeout=0), {'Cache-Control': f'no-cache, max-age=0, t={timestamp}'}

if __name__ == '__main__':
    app.run()