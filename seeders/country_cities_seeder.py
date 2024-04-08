from typing import List
from sqlalchemy.orm import Session

from app.seedwork.domain.entities import City, Country



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


def cities_seed(db: Session):
    cities_to_create = [
        # Argentina
        City(name="Buenos Aires", code="BA", country_id=1),
        City(name="Cordoba", code="CB", country_id=1),
        City(name="Rosario", code="RS", country_id=1),
        City(name="Mendoza", code="MDZ", country_id=1),
        City(name="Mar del Plata", code="MDP", country_id=1),

        # Bolivia
        City(name="La Paz", code="LP", country_id=2),
        City(name="Santa Cruz de la Sierra", code="SCZ", country_id=2),
        City(name="Cochabamba", code="CBBA", country_id=2),
        City(name="Sucre", code="SRE", country_id=2),
        City(name="Potosí", code="PTS", country_id=2),
        
        # Brazil
        City(name="Sao Paulo", code="SP", country_id=3),
        City(name="Rio de Janeiro", code="RJ", country_id=3),
        City(name="Brasilia", code="BSB", country_id=3),
        City(name="Salvador", code="SSA", country_id=3),
        City(name="Fortaleza", code="FOR", country_id=3),
        
        # Chile
        City(name="Santiago", code="SCL", country_id=4),
        City(name="Valparaiso", code="VAL", country_id=4),
        City(name="Concepcion", code="CCP", country_id=4),
        City(name="Antofagasta", code="ANT", country_id=4),
        City(name="Valdivia", code="VLD", country_id=4),
        
        # Colombia
        City(name="Bogota", code="BOG", country_id=5),
        City(name="Medellin", code="MDE", country_id=5),
        City(name="Cali", code="CLO", country_id=5),
        City(name="Barranquilla", code="BAQ", country_id=5),
        City(name="Cartagena", code="CTG", country_id=5),
        
        # Costa Rica
        City(name="San Jose", code="SJO", country_id=6),
        City(name="Limon", code="LIM", country_id=6),
        City(name="Alajuela", code="AJA", country_id=6),
        City(name="Heredia", code="HER", country_id=6),
        City(name="Puntarenas", code="PUN", country_id=6),
        
    ]
    create_or_update_cities(db, cities_to_create)
    db.commit()


def create_or_update_cities(db: Session, cities: List[City]):
    for city in cities:
        city_db = db.query(City).filter_by(name=city.name).first()

        if city_db:
            city_db.code = city.code
            city_db.name = city.name
            city_db.country_id = city.country_id
        else:
            db.add(city)
