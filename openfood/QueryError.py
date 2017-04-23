
class QueryError(Exception):
        
    BAD_REQUEST = 0x01
    BAD_KEY = 0x02
    NO_MATCHING = 0x03
    NO_NAME = 0x04

    def __init__(self, id_error, message):
        self.id_error = id_error
        self.message = message
