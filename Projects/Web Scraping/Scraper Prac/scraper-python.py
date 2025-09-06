
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import json

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

def scrape():
  url = "https://www.scrapethissite.com/pages/simple/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  # Getting all the h3 and i tags which holds the country info
  country_name = soup.find_all("h3", class_="country-name")
  country_capital = soup.find_all("span", class_="country-capital")
  country_population = soup.find_all("span", class_="country-population")
  country_area = soup.find_all("span", class_="country-area")

  names = [country.get_text(strip=True) for country in country_name]
  capitals = [capital.get_text(strip=True) for capital in country_capital]
  populations = [pop.get_text(strip=True) for pop in country_population]
  areas = [area.get_text(strip=True) for area in country_area]

  countries = []
  
  for name, capital, pop, area in zip(names, capitals, populations, areas):
    countries.append({
      "name": name,
      "capital": capital,
      "population": pop,
      "area": area
    })
  
  return countries

@app.get("/get_countries")
async def get_countries():
  return scrape()
