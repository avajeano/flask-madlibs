from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/prompts')
def prompts_page():
    prompts = story.prompts
    return render_template('prompts.html', prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('story.html', text=text)