from dataclasses import dataclass
from pydantic import ConfigDict, EmailStr, BaseModel
from app.modules.user.domain.enums.document_type_enum import DocumentTypeEnum


@dataclass(frozen=True)
class UserRequestDTO(BaseModel):
    country_id: int
    role_id: int
    city: str
    password: str
    email: EmailStr
    name: str
    lastname: str
    document_type: DocumentTypeEnum
    document_number: str

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "country_id": 1,
            "role_id": 3,
            "city": "Bello",
            "password": "secret",
            "email": "deportista@sport.app",
            "name": 'deportista',
            "lastname": "no profesional",
            "document_type": "CC",
            "document_number": "123456789"
        }
    })


@dataclass(frozen=True)
class UserResponseDTO(BaseModel):
    id: int
    email: str
    lastname: str
    name: str
    model_config = ConfigDict(from_attributes=True)
