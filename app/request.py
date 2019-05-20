from app import app
import urllib.request,json
from .models import sources

Source = sources.Source

# Getting the api key
api_key = app.config['NEWS_API_KEY']
# Getting the base url
# base_url = app.config["https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"]

def get_sources(category):
    '''
    functions that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

        return source_results

def process_results(source_list):
    '''
    functions that process the sources result and transforms them to a list of objects
    Args:
        source list:  A list of dictionaries that contain sources details

    returns:
        source results: A list of article objects
    '''
    source_results = []
    for article_item in source_list:
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')

    return source_results
