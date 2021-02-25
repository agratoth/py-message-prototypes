class MissingModelException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Missing "_model" field')
