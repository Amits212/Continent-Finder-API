from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContinentBase(BaseModel):
    code: str
    name: Optional[str] = None

class ContinentCreate(ContinentBase):
    pass

class ContinentUpdate(BaseModel):
    name: Optional[str] = None

class Continent(ContinentBase):
    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    code: str
    name: str
    full_name: str
    iso3: str
    number: int
    continent_code: str

class CountryCreate(CountryBase):
    pass

class CountryUpdate(BaseModel):
    name: Optional[str] = None
    full_name: Optional[str] = None
    iso3: Optional[str] = None
    number: Optional[int] = None
    continent_code: Optional[str] = None

class Country(CountryBase):
    updated_at: datetime
    continent: Optional[Continent] = None

    class Config:
        orm_mode = True
