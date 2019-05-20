class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self, name, author, title, description, category):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.category = category
        self.urlToImage = urlToImage
