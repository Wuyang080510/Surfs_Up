# Surfs_Up
Analyzing weather data with Python, SQLite, and SQLAlchemy. Building a webpage to present the analysis with Flask.

## Purpose 
- Use SQLite, a faster and small desktop database, to conduct data analysis
- Connect Python and SQLite with SQLAlchemy 
- Use statistics like mean, percentile, min, and max to analyze data

### Overview
In this project, an investor asked me to conduct a weather analysis before he opens a Surf n' Ice Cream Shop in Oahu, Hawaii. His main concern is that the precipitation will limit the days for surfing and the days the shop can open for business throughout the year. To check if open a surf store in Hawaii is feasible, I conducted a weather analysis with hawaii.sqlite database. I connected the SQLite to Python with the SQLAlchemy library, ran queries in Python, and created a statistic summary table for temperatures and precipitation in June and December. 

## Results 
In this analysis, I pulled all the temperature data for June and December. Two statistic summary tables were returned for temperatures in June and December, respectively. 

![img_June_Temp](https://github.com/Wuyang080510/Surfs_Up/blob/main/image/June%20Temp.png)  ![img_December_Temp](https://github.com/Wuyang080510/Surfs_Up/blob/main/image/December%20Temp.png)

- Temperatures in June and December kept stable 
    * The average temperature in June is 74.9 F, about 4 degrees higher than the average temperature in December. The difference between the lowest temperatures in June and December is no more than 10 degrees of Fahrenheit. And the highest temperature difference between June and December is only 2 degrees of Fahrenheit. As temperature in a year tends to go higher in June and goes lower in December, We can conclude that Oahu keeps a stable temperature all over the year. 

- Temperatures in June and December follow normal distribution
  * In the June Temperature statistic table, the average temperature in June (74.94 F) is about the same as the temperature at the 50th percentile (75.0 F). The same for December Temperature statistic table. The average temperature is 71.04 F, almost equals to the temperature at 50th percentile (71.0 F). The temperature distributions in June and December are symmetrical, non-skewed.
  
- Temperatures are clustered around the average temperature for both months.
    * The standard deviation oF June temperatures is 3.26, which indicates 68% of temperatures in June ranges from 71.64 F to 78.16 F.
    * The standard deviation oF December temperatures is 3.75, which indicates 68% of temperatures in December ranges from 67.29 F to 74.79 F.

![img_June_Temp_Hist]()  ![img_Dec_Temp_Hist]()

### Additional Tables and Graphs for Precipitation in Oahu, Hawaii
- Precipitation level is a significant factor that determines if the investor will open a surf store in Oahu. I also queried precipitation data for June and December from the database and plotted the data with matplotlib. From the histogram graphs, most of the days in June and December don't have any precipitation. 75% of the days in June and December rained less than 0.15 inches.

![img_June_prcp_Hist]()  ![img_Dec_prcp_Hist]()

![img_June_prcp_table]()  ![img_Dec_prcp_table]()

## Summary
Rain and temperature are the major concerns for the investor to invest in a Surf n' Ice Cream shop in Oahu, Hawaii. Based on the above analysis, the temperature in Oahu kept stable throughout the year. The average temperature was around 71 F to 75 F. The precipitation level kept low for most of the days. There were a couple of days with rain higher than 2 inches. The weather analysis supports opening a Surf n' Ice Cream shop on Oahu Island. 
    

