from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from models import Country as DBCountry, Continent as DBContinent
from schemas import CountryCreate, CountryUpdate, ContinentCreate, ContinentUpdate


async def get_countries(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(DBCountry).offset(skip).limit(limit))
    return result.scalars().all()

async def get_country_by_name(db: AsyncSession, country_name: str):
    result = await db.execute(select(DBCountry).filter(DBCountry.name == country_name).options(joinedload(DBCountry.continent)))
    return result.scalar()

async def create_country(db: AsyncSession, country: CountryCreate):
    db_country = DBCountry(**country.dict())
    db.add(db_country)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def update_country(db: AsyncSession, country_code: str, country: CountryUpdate):
    result = await db.execute(select(DBCountry).filter(DBCountry.code == country_code))
    db_country = result.scalar()
    if db_country is None:
        return None
    for key, value in country.dict(exclude_unset=True).items():
        setattr(db_country, key, value)
    await db.commit()
    await db.refresh(db_country)
    return db_country

async def delete_country(db: AsyncSession, country_code: str):
    result = await db.execute(select(DBCountry).filter(DBCountry.code == country_code))
    country = result.scalar()
    if country is None:
        return None
    await db.delete(country)
    await db.commit()
    return country


async def get_continents(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(DBContinent).offset(skip).limit(limit))
    return result.scalars().all()

async def get_continent_by_name(db: AsyncSession, continent_name: str):
    result = await db.execute(select(DBContinent).filter(DBContinent.name == continent_name))
    return result.scalar()

async def create_continent(db: AsyncSession, continent: ContinentCreate):
    db_continent = DBContinent(**continent.dict())
    db.add(db_continent)
    await db.commit()
    await db.refresh(db_continent)
    return db_continent

async def update_continent(db: AsyncSession, continent_name: str, continent: ContinentUpdate):
    result = await db.execute(select(DBContinent).filter(DBContinent.name == continent_name))
    db_continent = result.scalar()
    if db_continent is None:
        return None
    for key, value in continent.dict(exclude_unset=True).items():
        setattr(db_continent, key, value)
    await db.commit()
    await db.refresh(db_continent)
    return db_continent

async def delete_continent(db: AsyncSession, continent_name: str):
    result = await db.execute(select(DBContinent).filter(DBContinent.name == continent_name))
    continent = result.scalar()
    if continent is None:
        return None
    await db.delete(continent)
    await db.commit()
    return continent
