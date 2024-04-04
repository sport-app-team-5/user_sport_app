import pytest
from app.modules.user.aplication.service import UserService
from app.modules.user.infrastructure.exceptions import ImplementationNotExistForFabricTypeException


class NonRepository:
    pass


class TestUserException:
    def test_factory_user(self):
        user_service = UserService()

        with pytest.raises(ImplementationNotExistForFabricTypeException) as exc_info:
            user_service.repository_factory.create_object(NonRepository)

        assert 'There is no implementation for the repository with the given type' in str(exc_info.value)
