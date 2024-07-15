from datetime import datetime
from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from models import Country as DBCountry, Continent as DBContinent
from schemas import CountryCreate, CountryUpdate, ContinentCreate, ContinentUpdate

async def get_countries_query(db: AsyncSession, skip: int = 0, limit: int = 10):
    return select(DBCountry).offset(skip).limit(limit)

async def get_country_by_name_query(db: AsyncSession, country_name: str):
    return select(DBCountry).filter(DBCountry.name == country_name).options(joinedload(DBCountry.continent))

async def create_country(db: AsyncSession, country: CountryCreate):
    db_country = DBCountry(**country.dict())
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def update_country(db: AsyncSession, country_code: str, country: CountryUpdate):
    query = select(DBCountry).filter(DBCountry.code == country_code)
    result = await db.execute(query)
    db_country = result.scalar()
    if db_country is None:
        return None
    for key, value in country.dict(exclude_unset=True).items():
        setattr(db_country, key, value)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def delete_country(db: AsyncSession, country_code: str):
    query = select(DBCountry).filter(DBCountry.code == country_code)
    result = await db.execute(query)
    country = result.scalar()
    if country is None:
        return None
    await db.delete(country)
    await db.commit()
    return country

async def get_continents_query(db: AsyncSession, skip: int = 0, limit: int = 10):
    return select(DBContinent).offset(skip).limit(limit)

async def get_continent_by_name_query(db: AsyncSession, continent_name: str):
    return select(DBContinent).filter(DBContinent.name == continent_name)

async def create_continent(db: AsyncSession, continent: ContinentCreate):
    db_continent = DBContinent(**continent.dict())
    db.add(db_continent)
    await db.commit()
    await db.refresh(db_continent)
    return db_continent

async def update_continent(db: AsyncSession, continent_name: str, continent: ContinentUpdate):
    query = select(DBContinent).filter(DBContinent.name == continent_name)
    result = await db.execute(query)
    db_continent = result.scalar()
    if db_continent is None:
        return None
    for key, value in continent.dict(exclude_unset=True).items():
        setattr(db_continent, key, value)
    await db.commit()
    await db.refresh(db_continent)
    return db_continent

async def delete_continent(db: AsyncSession, continent_name: str):
    query = select(DBContinent).filter(DBContinent.name == continent_name)
    result = await db.execute(query)
    continent = result.scalar()
    if continent is None:
        return None
    await db.delete(continent)
    await db.commit()
    return continent

async def get_countries_by_updated_at_query(
        db: AsyncSession,
        start_date: Optional[datetime],
        end_date: Optional[datetime],
        skip: int = 0,
        limit: int = 10
):
    query = select(DBCountry).offset(skip).limit(limit)
    if start_date and end_date:
        query = query.filter(DBCountry.updated_at.between(start_date, end_date))
    elif start_date:
        query = query.filter(DBCountry.updated_at >= start_date)
    elif end_date:
        query = query.filter(DBCountry.updated_at <= end_date)
    return query
