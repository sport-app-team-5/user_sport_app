from app.seedwork.domain.exceptions import FactoryException


class ImplementationNotExistForFabricTypeException(FactoryException):
    def __init__(self, message='There is no implementation for the repository with the given type'):
        self.__message = message

    def __str__(self):
        return str(self.__message)
