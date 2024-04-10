from dataclasses import dataclass
from typing import Optional
from pydantic import ConfigDict, EmailStr, BaseModel, validator
from app.modules.user.domain.enums.document_type_enum import DocumentTypeEnum


@dataclass(frozen=True)
class UserRequestDTO(BaseModel):
    residence_city_id: int
    role_id: int
    birth_city_id: Optional[int] = None
    password: str
    email: EmailStr
    name: str
    lastname: str
    document_type: DocumentTypeEnum
    document_number: str

    @validator('birth_city_id', pre=True)
    def check_birth_city_id(cls, v, values):
        if 'role_id' in values and values['role_id'] != 2:
            if v is None:
                raise ValueError("birth_city_id is required")
        return v

    model_config = ConfigDict(validate_default=True, json_schema_extra={
        "example": {
            "birth_city_id": 1,
            "residence_city_id": 1,
            "role_id": 3,
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
    birth_city_id: Optional[int] = None
    residence_city_id: int
    role_id: int
    email: str
    lastname: str
    name: str
    model_config = ConfigDict(from_attributes=True)
