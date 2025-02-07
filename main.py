from flask import Flask, render_template, request, session, redirect, flash, jsonify, current_app, url_for, send_file, make_response
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
    timestamp = int(time.time())  # Generate a new timestamp
    return redirect(f'https://osu.ppy.sh/users/19921620?t={timestamp}')

@app.route('/dynamic_execute.gif')
def serve_gif():
    """Serve execute.gif with cache prevention."""
    update_gif()  # Update GIF before serving

    response = make_response(send_file(EXECUTE_FILE, mimetype='image/gif'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Timestamp'] = str(int(time.time()))  # Add timestamp header for tracking
    
    return response
if __name__ == '__main__':
    app.run()