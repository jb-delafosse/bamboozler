class HttpException(Exception):
    """
    Base class for HttpExceptions
    """

    def __init__(self, message):
        """
        Init an HttpException with a message

        Args:
            message: the error message
        """
        self.message = message


class NotImplementedException(HttpException):
    code = 501


class BadRequestException(HttpException):
    code = 400


class NotFoundException(HttpException):
    code = 404


class InternalServerErrorException(HttpException):
    code = 500


class NotAuthorizedException(HttpException):
    code = 401


class ForbiddenException(HttpException):
    code = 403
