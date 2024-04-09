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

        # Cuba
        City(name="Havana", code="HAV", country_id=7),
        City(name="Santiago de Cuba", code="SCU", country_id=7),
        City(name="Camagüey", code="CMW", country_id=7),
        City(name="Holguín", code="HOG", country_id=7),
        City(name="Santa Clara", code="SNU", country_id=7),

        # República Dominicana
        City(name="Santo Domingo", code="SDQ", country_id=8),
        City(name="Santiago de los Caballeros", code="STI", country_id=8),
        City(name="La Romana", code="LRM", country_id=8),
        City(name="San Pedro de Macorís", code="LRM", country_id=8),
        City(name="San Francisco de Macorís", code="SFMD", country_id=8),

        # Ecuador
        City(name="Quito", code="UIO", country_id=9),
        City(name="Guayaquil", code="GYE", country_id=9),
        City(name="Cuenca", code="CUE", country_id=9),
        City(name="Ambato", code="ATF", country_id=9),
        City(name="Manta", code="MEC", country_id=9),

        # El Salvador
        City(name="San Salvador", code="SAL", country_id=10),
        City(name="Santa Ana", code="SAA", country_id=10),
        City(name="San Miguel", code="SAL", country_id=10),
        City(name="Soyapango", code="SYP", country_id=10),
        City(name="Apopa", code="APO", country_id=10),

        # Guatemala
        City(name="Guatemala City", code="GUA", country_id=11),
        City(name="Quetzaltenango", code="QTC", country_id=11),
        City(name="Escuintla", code="ESC", country_id=11),
        City(name="Mixco", code="MIX", country_id=11),
        City(name="Villa Nueva", code="VNV", country_id=11),

        # Honduras
        City(name="Tegucigalpa", code="TGU", country_id=12),
        City(name="San Pedro Sula", code="SAP", country_id=12),
        City(name="Choloma", code="CHO", country_id=12),
        City(name="La Ceiba", code="LCE", country_id=12),
        City(name="El Progreso", code="EPA", country_id=12),

        # Mexico
        City(name="Mexico City", code="MEX", country_id=13),
        City(name="Guadalajara", code="GDL", country_id=13),
        City(name="Monterrey", code="MTY", country_id=13),
        City(name="Puebla", code="PBL", country_id=13),
        City(name="Tijuana", code="TIJ", country_id=13),

        # Nicaragua
        City(name="Managua", code="MGA", country_id=14),
        City(name="León", code="LEN", country_id=14),
        City(name="Matagalpa", code="MTG", country_id=14),
        City(name="Chinandega", code="CND", country_id=14),
        City(name="Masaya", code="MAS", country_id=14),

        # Panama
        City(name="Panama City", code="PTY", country_id=15),
        City(name="San Miguelito", code="SNG", country_id=15),
        City(name="Tocumen", code="TUM", country_id=15),
        City(name="David", code="DAV", country_id=15),
        City(name="Arraiján", code="ARR", country_id=15),

        # Paraguay
        City(name="Asunción", code="ASU", country_id=16),
        City(name="Ciudad del Este", code="AGT", country_id=16),
        City(name="San Lorenzo", code="SLZ", country_id=16),
        City(name="Luque", code="LUI", country_id=16),
        City(name="Capiatá", code="CPT", country_id=16),

        # Peru
        City(name="Lima", code="LIM", country_id=17),
        City(name="Arequipa", code="AQP", country_id=17),
        City(name="Trujillo", code="TRU", country_id=17),
        City(name="Chiclayo", code="CIX", country_id=17),
        City(name="Huancayo", code="HUU", country_id=17),

        # Puerto Rico
        City(name="San Juan", code="SJU", country_id=18),
        City(name="Bayamón", code="BAY", country_id=18),
        City(name="Carolina", code="CAP", country_id=18),
        City(name="Ponce", code="PON", country_id=18),
        City(name="Caguas", code="CGS", country_id=18),

        # Uruguay
        City(name="Montevideo", code="MVD", country_id=19),
        City(name="Salto", code="STY", country_id=19),
        City(name="Ciudad de la Costa", code="CYD", country_id=19),
        City(name="Paysandú", code="PDU", country_id=19),
        City(name="Las Piedras", code="LPD", country_id=19),

        # Venezuela
        City(name="Caracas", code="CCS", country_id=20),
        City(name="Maracaibo", code="MAR", country_id=20),
        City(name="Valencia", code="VLN", country_id=20),
        City(name="Barquisimeto", code="BRM", country_id=20),
        City(name="Maracay", code="MYC", country_id=20),

        
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
