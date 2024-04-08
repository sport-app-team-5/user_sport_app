from sqlalchemy.orm import Session
from . import permission_roles_seed, countries_seed, cities_seed


def all_seeders(db: Session):
    countries_seed(db)
    cities_seed(db)
    permission_roles_seed(db)

