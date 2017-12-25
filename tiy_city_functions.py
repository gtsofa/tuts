#11-1:City,Country
def get_city_country(city, country, population=''):
    """Returns a single string of the form City, Country eg Santiago, Chile."""
    if population != '':
        city_country_population = city + ',' + ' ' + country + ' - population ' + str(population) + '.'
    else:
        city_country_population = city + ',' + ' ' + country

    return city_country_population.title()

#get_city_country('nairobi', 'kenya')
#get_city_country('lagos', 'nigeria', 600000)

