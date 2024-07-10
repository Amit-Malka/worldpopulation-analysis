import csv

### fun 1\7
def check_year(year):
    if year >= 1960 and year <= 2017:
        return True
    return False 
  
### fun 2\7
def check_years(year1,year2):
    if (check_year(year1) and check_year(year2)) == True and year2 >= year1:
        return True
    return False

### fun 3\7
def break_world_pop_line(line):
    world_population = []
    with open('world_population.csv','r') as myfile:
        myReader = csv.reader(myfile)
        world_population = list(myReader)
    
    return print(world_population[line])

### fun 4\7
def check_country(world_pop_file,country):
    countrycheck = ["Arab World", "Central Europe and the Baltics", "East Asia & Pacific (excluding high income)", "Early-demographic dividend","East Asia & Pacific", "Europe & Central Asia (excluding high income)" ,"Europe & Central Asia", "Euro area", 'European Union', 'Fragile and conflict affected situations', 'High income', 'Heavily indebted poor countries (HIPC)', 'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only', 'Not classified', 'Latin America & Caribbean (excluding high income)', 'Latin America & Caribbean', 'Least developed countries: UN classification', 'Low income', 'Lower middle income', 'Low & middle income', 'Late-demographic dividend', 'Middle East & North Africa', 'Middle income', 'Middle East & North Africa (excluding high income)', 'North America', 'OECD members', 'Other small states', 'Pre-demographic dividend', 'Post-demographic dividend', 'South Asia', 'Sub-Saharan Africa (excluding high income)', 'Sub-Saharan Africa', 'Small states', 'East Asia & Pacific (IDA & IBRD countries)', 'Europe & Central Asia (IDA & IBRD countries)', 'Latin America & the Caribbean (IDA & IBRD countries)', 'Middle East & North Africa (IDA & IBRD countries)', 'South Asia (IDA & IBRD)', 'Sub-Saharan Africa (IDA & IBRD countries)', 'Upper middle income', 'World']
    if country in countrycheck:
        return False
    try:
        with open(world_pop_file,'r') as myfile:
                myReader = csv.reader(myfile)
                next(myReader)
                countries = []
                i = 1
                for row in myReader:
                    row = list(row)
                    countries.append(row[0])
                    i += 1

                if country in countries:
                    return True
                else:
                    return False
    except:
        return print("file doesn't exsist, check your path.")

### fun 5\7
def country_pop(world_pop_file,country,year):
    if check_country(world_pop_file,country) == True and check_year(year):
        with open(world_pop_file,'r') as myfile:
            myReader = csv.reader(myfile)
            next(myReader)
            for row in myReader:
                row = list(row)
                if row[0] == country:
                    answer = row[year-1960+4]
                    if answer == "" or None:
                        return None
                    else:
                        answer = int(answer)
                        return answer
    else:
        return None

### fun 6\7
def pop_change(world_pop_file,country,year1,year2):
    if check_country(world_pop_file,country) and check_years(year1,year2) == True:
        if country_pop(world_pop_file,country,year2) == None or country_pop(world_pop_file,country,year1) == None:
            return None
        return (100*(country_pop(world_pop_file,country,year2))/(country_pop(world_pop_file,country,year1))-100)
    else:
        return None

### fun 7\7
def max_pop_change(world_pop_file,year1,year2):
    if check_years(year1,year2) == False:
        return None
    with open(world_pop_file,'r') as myfile:
        myReader = csv.reader(myfile)
        next(myReader)
        i = 1
        max_change = int(0)
        for row in myReader:
            row = list(row)
            country = row[0]
            popchange = pop_change(world_pop_file,country,year1,year2)
            if popchange != False and popchange != None:
                if popchange > max_change:
                    max_change = pop_change(world_pop_file,country,year1,year2)
                    max_country = country
            i += 1
            continue
    return max_country,max_change


#code
country,year1,year2 = input("Enter country, year1, year2:").split(",") 
if check_country("world_population.csv",country) == True:
    try:
        year1 = int(year1)
        year2 = int(year2)
    except:
        print(f"Error: year 1 ({year1}) and/or year2 ({year2}) are illegal, must be between 1960-2017 and year1 >= year2")
    
    if check_years(year1,year2) == True:
        print(f"Population in {year1}: ",country_pop("world_population.csv",country,year1))
        print(f"Population in {year2}: ",country_pop("world_population.csv",country,year2))
        print(f"Change of population (%): ",pop_change("world_population.csv",country,year1,year2))
        max_country, max_change = max_pop_change("world_population.csv",year1,year2)
        print(f"Highest change of population: {max_country}, {max_change}")
    else:
        print(f"Error: year 1 ({year1}) and/or year2 ({year2}) are illegal, must be between 1960-2017 and year1 >= year2")
else:
    print("Error:",country,"is an illegal country")

