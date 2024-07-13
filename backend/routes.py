from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from crud import (
    get_countries, get_country_by_name, create_country, update_country, delete_country,
    get_continents, get_continent_by_name, create_continent, update_continent, delete_continent,
    get_countries_by_updated_at
)
from schemas import Country, CountryCreate, CountryUpdate, Continent, ContinentCreate, ContinentUpdate
from fastapi_pagination import Page, add_pagination, paginate

router = APIRouter()

async def get_db():
    async with SessionLocal() as db:
        yield db

@router.get("/countries", response_model=Page[Country])
async def read_countries(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    countries = await get_countries(db, skip=skip, limit=limit)
    return paginate(countries)

@router.get("/country/{country_name}", response_model=Country)
async def read_country_by_name(country_name: str, db: AsyncSession = Depends(get_db)):
    country = await get_country_by_name(db, country_name)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country

@router.post("/country", response_model=Country)
async def create_new_country(country: CountryCreate, db: AsyncSession = Depends(get_db)):
    return await create_country(db, country)

@router.put("/country/{country_code}", response_model=Country)
async def update_existing_country(country_code: str, country: CountryUpdate, db: AsyncSession = Depends(get_db)):
    updated_country = await update_country(db, country_code, country)
    if updated_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return updated_country

@router.delete("/country/{country_code}")
async def delete_existing_country(country_code: str, db: AsyncSession = Depends(get_db)):
    country = await delete_country(db, country_code)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"message": "Country deleted successfully"}

@router.get("/continents", response_model=Page[Continent])
async def read_continents(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    continents = await get_continents(db, skip=skip, limit=limit)
    return paginate(continents)

@router.get("/continent/{continent_name}", response_model=Continent)
async def read_continent_by_name(continent_name: str, db: AsyncSession = Depends(get_db)):
    continent = await get_continent_by_name(db, continent_name)
    if continent is None:
        raise HTTPException(status_code=404, detail="Continent not found")
    return continent

@router.post("/continent", response_model=Continent)
async def create_new_continent(continent: ContinentCreate, db: AsyncSession = Depends(get_db)):
    return await create_continent(db, continent)

@router.put("/continent/{continent_name}", response_model=Continent)
async def update_existing_continent(continent_name: str, continent: ContinentUpdate, db: AsyncSession = Depends(get_db)):
    updated_continent = await update_continent(db, continent_name, continent)
    if updated_continent is None:
        raise HTTPException(status_code=404, detail="Continent not found")
    return updated_continent

@router.delete("/continent/{continent_name}")
async def delete_existing_continent(continent_name: str, db: AsyncSession = Depends(get_db)):
    continent = await delete_continent(db, continent_name)
    if continent is None:
        raise HTTPException(status_code=404, detail="Continent not found")
    return {"message": "Continent deleted successfully"}

@router.get("/countries/updated_at", response_model=Page[Country])
async def read_countries_by_updated_at(
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    countries = await get_countries_by_updated_at(db, start_date, end_date,skip, limit)
    return paginate(countries)

add_pagination(router)
