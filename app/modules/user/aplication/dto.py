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
            "role_id": 1,
            "city": "Bello",
            "password": "luis",
            "email": "luis@gmail.com",
            "name": 'luis',
            "lastname": "perez",
            "document_type": "CC",
            "document_number": "12234556677"
        }
    })


@dataclass(frozen=True)
class UserResponseDTO(BaseModel):
    id: int
    country_id: int
    role_id: int
    email: str
    name: str
    model_config = ConfigDict(from_attributes=True)
