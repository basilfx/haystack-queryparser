class QueryParserException(Exception):
    pass


class UnhandledException(QueryParserException):
    pass


class NoMatchingBracketsFound(QueryParserException):

    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return "Matching brackets were not found: " + self.value
