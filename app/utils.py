# app/utils.py
import pycountry

# Placeholder for an in-memory list to store the countries
allowed_countries = []

def extract_country_list():
    countries = [country.name for country in pycountry.countries]
    countries_list = sorted(countries)
    return countries_list

def extract_allowed_country_list():
    global allowed_countries
    return allowed_countries

def update_geo(mode, selected_countries):
    global allowed_countries

    countries_list = extract_country_list()

    # Perform actions to update the countries list
    if mode == 'whitelist':
        allowed_countries = selected_countries
    elif mode == 'blacklist':
        allowed_countries = [country for country in countries_list if country not in selected_countries]

    return allowed_countries
