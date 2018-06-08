"""
# Put here all exceptions that will be thrown by your application
# It is recommended that an Exception should be raise on every request that does NOT satisfy the requirement of endpoint
# eg:
# on /api/guestbook/create if the email address already exist. the endpoint will raise EmailAlreadyExistException()
# which will be converted automatically to json response
"""

class CustomException(Exception):
    status_code = 400
    message = 'An error has occured'


    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        cls = self.__class__

        self.message = message if message else cls.message
        self.status_code = status_code if status_code else cls.status_code
        self.payload = payload


    def __str__(self):
        return self.message


    def to_dict(self):
        return {
            'error': self.__class__.__name__,
            'message': self.message,
            'payload': self.payload
        }



class UnexpectedException(CustomException):
    status_code = 500
    message = 'An unexpected error has occured'



class EntityNotFoundException(CustomException):
    status_code = 404
    message = 'Entity does not exist'



class EntityAlreadyExistException(CustomException):
    status_code = 409
    message = 'Entity already exist'



class InvalidFormatException(CustomException):
    status_code = 400
    message = 'Does not follow the model format'



class EmailAlreadyExistException(CustomException):
    status_code = 404
    message = 'Email already exist'



class ResourceNotFoundException(CustomException):
    status_code = 404
    message = 'Resource not found'



class InvalidQueryParamsException(CustomException):
    status_code = 400
    message = 'Query cannot be done'



class ForbiddenException(CustomException):
    status_code = 403
    message = 'Forbidden action'