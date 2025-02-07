from flask import Flask, render_template, request, session, redirect, flash, jsonify, current_app, url_for
app = Flask(__name__)

@app.route('/')
def choose_option():
    

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)