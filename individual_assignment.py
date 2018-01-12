# Import the JSON and CSV packages
import json
import csv

# Load in the conflict JSON data
#with open('conflict_data_full_lined.json') as file:
#   data = json.load(file)
 
with open('conflict_data_full_lined.json') as file:
    data = json.load(file)
 
# Create a list with all the incidents in Egypt               
    data_egypt = []
    for item in data:
        if item["country"] == "Egypt":
          data_egypt.append(item)
# Create a list with all the incidents in Egypt in 2011          
          data_egypt_2011 = []
          for item in data_egypt:
             if item["year"] == 2011:
               data_egypt_2011.append(item)
# Create a list with all the incidents in Egypt in 2015              
          data_egypt_2015 = []
          for item in data_egypt:
              if item["year"] == 2015:
                  data_egypt_2015.append(item)
# This sums up all the deaths in 2011 in Egypt                                 
total_deaths_2011 = 0                 
for item in data_egypt_2011:
    total_deaths_2011 += item["best"]
# This sums up all the deaths in 2015 in Egypt
total_deaths_2015 = 0                 
for item in data_egypt_2015:
    total_deaths_2015 += item["best"]


#Open the output CSV file we want to write to
with open('data_egypt_2011.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'region', 'year', 'latitude', 'longitude', 'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown','best', 'high', 'low'])
    for item in data_egypt_2011:
         csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
         csvwriter.writerow([item['country'], item['region'], item['year'], item['latitude'], item['longitude'], item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['deaths_unknown'],item['best'], item['high'], item['low']])
        
with open('data_egypt_2015.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['country', 'region', 'year', 'latitude', 'longitude', 'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown','best', 'high', 'low'])
    for item in data_egypt_2015:
         csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
         csvwriter.writerow([item['country'], item['region'], item['year'], item['latitude'], item['longitude'], item['deaths_a'], item['deaths_b'], item['deaths_civilians'], item['deaths_unknown'],item['best'], item['high'], item['low']])    
    #Actually write the data to the CSV file here.
    # You can use the same csvwriter.writerow command to output the data 
     #  as is used above to output the headers.

        

