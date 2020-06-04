from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "guitar"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html',stories = stories)

@app.route('/play', methods=['POST'])
def play_redirect():
    value = request.form['stories']

    return redirect(f'/play/story{value}')

@app.route('/play/story<int:num>')
def madlibs(num):
    return render_template('play.html', story = stories[num-1], num = num, id_counter = 0)

@app.route('/story<int:num>/answer')
def answer(num):
    answers = dict(request.args)
    
        
    return render_template('answer.html', template = stories[num-1].generate(answers))