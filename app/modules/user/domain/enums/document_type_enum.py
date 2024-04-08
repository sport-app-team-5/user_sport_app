from enum import Enum


class DocumentTypeEnum(str, Enum):
    CC = ("CC", "Cédula de ciudadanía")
    NIT = ("NIT", "Número de identificación tributaria")
    CE = ("CE", "Cédula de extranjería")
    PP = ("PP", "Pasaporte")

    def __new__(cls, code, desc):
        obj = str.__new__(cls)
        obj._value_ = code
        obj.desc = desc
        return obj
