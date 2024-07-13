from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Continent(Base):
    __tablename__ = 'continents'

    code = Column(String(2), primary_key=True, comment='Continent code')
    name = Column(String(255))

class Country(Base):
    __tablename__ = 'countries'

    code = Column(String(2), primary_key=True, comment='Two-letter country code (ISO 3166-1 alpha-2)')
    name = Column(String(255), nullable=False, comment='English country name')
    full_name = Column(String(255), nullable=False, comment='Full English country name')
    iso3 = Column(String(3), nullable=False, comment='Three-letter country code (ISO 3166-1 alpha-3)')
    number = Column(Integer, nullable=False, comment='Three-digit country number (ISO 3166-1 numeric)')
    continent_code = Column(String(2), ForeignKey('continents.code'), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    continent = relationship('Continent')
