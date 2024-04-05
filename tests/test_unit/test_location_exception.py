import pytest
from app.modules.location.aplication.service import LocationService
from app.modules.location.infrastructure.exceptions import ImplementationNotExistForFabricTypeException


class NonRepository:
    pass


class TestLocationException:
    def test_factory_location(self):
        location_service = LocationService()

        with pytest.raises(ImplementationNotExistForFabricTypeException) as exc_info:
            location_service.repository_factory.create_object(NonRepository)

        assert 'There is no implementation for the repository with the given type' in str(exc_info.value)
