from typing import List
from sqlalchemy.orm import Session
from app.modules.user.domain.entities import Country


def countries_seed(db: Session):
    countries_to_create = [
        Country(name="Argentina", code="AR"),
        Country(name="Bolivia", code="BO"),
        Country(name="Brazil", code="BR"),
        Country(name="Chile", code="CL"),
        Country(name="Colombia", code="CO"),
        Country(name="Costa Rica", code="CR"),
        Country(name="Cuba", code="CU"),
        Country(name="Dominican Republic", code="DO"),
        Country(name="Ecuador", code="EC"),
        Country(name="El Salvador", code="SV"),
        Country(name="Guatemala", code="GT"),
        Country(name="Honduras", code="HN"),
        Country(name="Mexico", code="MX"),
        Country(name="Nicaragua", code="NI"),
        Country(name="Panama", code="PA"),
        Country(name="Paraguay", code="PY"),
        Country(name="Peru", code="PE"),
        Country(name="Puerto Rico", code="PR"),
        Country(name="Uruguay", code="UY"),
        Country(name="Venezuela", code="VE")
    ]
    create_or_update(db, countries_to_create)
    db.commit()


def create_or_update(db: Session, countries: List[Country]):
    for country in countries:
        country_db = db.query(Country).filter_by(name=country.name).first()

        if country_db:
            country_db.code = country.code
            country_db.name = country.name
        else:
            db.add(country)
