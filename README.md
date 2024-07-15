# FastAPI Country and Continent API

## Description

This FastAPI application provides a RESTful API for managing countries and continents.

## Features

- **Country Management**
  - List all countries with pagination
  - Retrieve a specific country by name
  - Create a new country
  - Update an existing country
  - Delete a country

- **Continent Management**
  - List all continents with pagination
  - Retrieve a specific continent by name
  - Create a new continent
  - Update an existing continent
  - Delete a continent

- **Country Update History**
  - Retrieve countries updated within a specified date range with pagination

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- 
### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Amits212/Continent-Finder-API.git


### Run the Containerized app
docker compose up --build

### API Endpoints
Countries
GET /countries: List all countries with pagination.
GET /country/{country_name}: Retrieve a specific country by name.
POST /country: Create a new country.
PUT /country/{country_code}: Update an existing country.
DELETE /country/{country_code}: Delete a country.

Continents
GET /continents: List all continents with pagination.
GET /continent/{continent_name}: Retrieve a specific continent by name.
POST /continent: Create a new continent.
PUT /continent/{continent_name}: Update an existing continent.
DELETE /continent/{continent_name}: Delete a continent.
Countries by Update Timestamp
GET /countries/updated_at: Retrieve countries updated within a specified date range with pagination.
