from flask import render_template
from app import app
from .request import get_sources

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its page
    '''

    # getting newa articles from different sources.
    business_news = get_sources('business')
    print(business_news)

    title = 'Home - Welcome to the Best News Online Site.'
    return render_template('index.html', title=title, business=business_news)

@app.route('/source/<source>')
def source(source):
    '''
    view movie page function that returns the new movie details page
    '''

    return render_template('index.html')