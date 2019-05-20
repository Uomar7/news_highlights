from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its page
    '''
    title = 'Home - Welcome to the Best News Online Site.'
    return render_template('index.html')

@app.route('/source/<source>')
def source(source):
    '''
    view movie page function that returns the new movie details page
    '''

    return render_template('index.html')