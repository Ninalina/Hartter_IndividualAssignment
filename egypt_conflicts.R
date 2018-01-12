library('tidyverse')
egypt_2011 <- read.csv('data_egypt_2011.csv')
egypt_2015 <- read.csv('data_egypt_2015.csv')

# Calculate the sum of deaths
total_deaths_2011 = sum(egypt_2011$best)
total_deaths_2015 = sum(egypt_2015$best)

# Changing the non-descriptive name "best" (total number of deaths) to "number_of_deaths"
names(egypt_2011)[names(egypt_2011)=="best"] <- "deaths"
names(egypt_2015)[names(egypt_2015)=="best"] <- "deaths"

install.packages(c("maps", "mapdata"))
library('ggmap')
library('maps')
library('mapdata')
map.us <- map_data('usa')
map_data('world2Hires')
map.egypt <- map.globe %>%
  filter(region=="Egypt") 

# This merges the two data sets
conflicts <- rbind(egypt_2011, egypt_2015)

# Plots a map of Egypt with the colour blue representing the year 2011 blue and the colour red representing the year 2015
# The size of the dots represents the number of deaths
ggplot() +
  geom_polygon(data=map.egypt, mapping=aes(x=long, y=lat, group=group)) +
  geom_point(data = conflicts, mapping = aes(x = longitude, y = latitude, colour=as.factor(year), size=deaths)) +
  labs(title = "Deaths in Egypt", x = "Longitude", y = "Latitude")

# Creates a bargraph with each bar representing the number of deaths in each year respectively
element <- rep("egypt_2011")
qty <- c(total_deaths_2011, total_deaths_2015)
category <- c('2011', '2015')
d <- data.frame(element=element, qty=qty, category=category)
ggplot(d, aes(x=category, y=qty)) + geom_bar(stat="identity") + labs(title = "Deaths in Egypt", x = "Year", y = "Number of deaths")
