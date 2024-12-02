#Jessica Long-Heinicke Assignment 7.2
#city functions

def format_city_country(city, country, population=None, language=None):
    #returns a string in the format city, country, population if provided, language
    result = f"{city}, {country}"
    if population and language:
        result += f" - population {population}, {language}"
    elif population:
        result += f" - population {population}"
    elif language:
        result += f", {language}"
    return result

#test city countries
print(format_city_country("San Francisco", "US",))
print(format_city_country("Santiago", "Chile", 5000000))
print(format_city_country("London", "UK", 8866000, "English"))