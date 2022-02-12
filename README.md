# surfs_up

## Overview:

The attached analysis is a continuation for the climate research portion of our Surf/Ice Cream shop feasibility study.  Initial analysis conculded that Oahu, in general, is an ideal location for this sort of venture due to its mix of warm weather and ideal surfing.  The analysis below continues to evaluate the Oahu climate by comparing and contrasting temperature conditions for June and December.  A stable warm climate through all seasons is ideal for ensuring that this venture would be sustainable at any time of year.  In short, neither Ice Cream or surfing are popular activities in 40 degree weather.

Two additional querries were performed (June and December), to evaluate station locations to see if an ideal store location could be found.  In this case station locations were compared to their average temperatures and precipitation to find an area that is both consistantly warm and dry.  Lastly, the data was limitted to stations close to the water (i.e. elevations less than 50 ft).

## Resources:

### Data:
  
  1. ***hawaii.sqlite*** - Contains climate data for Oahu.  Two Table Tables:
    a.  **mesurements** - tempertaure obsereved (tob), Precipitation obserevs (precip), Date, and Station ID
    b.  **station** - station id (station), station name (name), elevation, latitude, and longitude.

### Software:

  1. Jupyter Notebook - ***SurfsUp_Challenge.ipynb*** accesses and querries qllite data, changes data into dataframes, and performs statistics and sorting.

## Procedure:

### Deliverable 1 and 2:

For analysis, the ***hawaii.sqlite*** database was used to extract data from both ***measurement and station*** tables.  For the first analysis, the average Oahu temperature for June was found by querring the measurment table and with the *extract* function, limit the imported data temerature data for the month of June.  The data was stored in a "results" variable.

![image](https://user-images.githubusercontent.com/91850824/153722565-ae6611d1-b384-45a4-9d76-e0ac1feb0722.png)

The data was then transfromed into a list using the *np.ravel* function on the results variable and stored as *june_temps*.  The *june_temps* list is then converted into a 
a data frame and statistics were ran on the temperature columns.

![image](https://user-images.githubusercontent.com/91850824/153722846-ebcaa177-0d99-4072-891c-d76958e32abf.png)

![image](https://user-images.githubusercontent.com/91850824/153722853-efc1e375-8e9c-4171-8296-bbcf0511bf77.png)

![image](https://user-images.githubusercontent.com/91850824/153722865-a0fe90b9-a92d-4579-9c08-a09d118586fe.png)

The process was repeated for the Month of December.

### Deliverable 3 additional querries:

Two additonal querries were made for Decmeber and June.  These querries used both the **station and measurement** tables and extract and calculate average temp and average precipitaion then group them (*group_by* function) by station id.  A dataframe is initial constructed using the station id, station name, and elevation from the **station** table.

![image](https://user-images.githubusercontent.com/91850824/153723162-ca2e2ed5-c91f-4164-b724-d019e1764b7e.png)

Turning to the **measurement** table.  The average temperature and precipitation data were extracted for the month of December and grouped by their station id's.  The querry is stored in a **dec_reults** variable and then transformed into a dataframe.

![image](https://user-images.githubusercontent.com/91850824/153723216-fdbb0c0e-8461-4214-99fc-78279bca4bab.png)

The 2 dataframes (dec_station_weather_df and station_df) are then merged so that the average temperature and precipitation data is show alongside the station name and elevation. Because surf shops in the mountains are not as successful as those actually on the water; all stations with elevations greater than 50 ft were dropped out.

![image](https://user-images.githubusercontent.com/91850824/153723332-240470df-4bf8-4199-9c4d-af506996e2f0.png)

![image](https://user-images.githubusercontent.com/91850824/153723363-a7ceea21-79d7-4487-9590-80c222834883.png)

This process was repeated for June.

## Results:

The desriptive statistics for June and December can be see below:

![image](https://user-images.githubusercontent.com/91850824/153723608-27843265-7983-4ebf-9ac8-10d462cd686d.png)

![image](https://user-images.githubusercontent.com/91850824/153723615-d63bd9e0-441c-4273-9a0c-50e622101366.png)

The three main observations can be said from the tables above:

1.  The mean temperature between June and December is only 4 degrees diffent between the months.  This certainly indicates a consistant temperature and is favorable for our shops success.  Likewise the max temps are only 3 degrees different.

2.  Minimum temperatures are more disparate, June's minimum temperature of 64 degrees is 8 degrees higher than December (56 degrees).  This makes sense given the less hours of sunshine during the winter season. 

3.  Since the winter seasons potential low temeratures are a potential loss of business during the colder months.  The potential for these lower temperatures must be examined.  Using the inter quartile range approach for finding outliers, December's IQR (75%tile - 25%tile)   is equal to 5.  This means that the the temerpature trends 5 degrees + or - from the mode of 71 degrees.  An outlier can be presumed if it lies beyond the 25%tile -(1.5 x the IQR), in this case 7.5 degrees minus 69 degrees (the 25%tile).  So our lowest temperature of 56 degrees is still less than 61.5 degrees and; although much more data is required to confirm it's anomalous, temperatures lower than 61.5 degrees are not typical.

## Summary:

Looking at Oahu in general, ratings on consistant temperatures appear to be perfect.  The mean temperatures between Summer and Winter only trend downward 4 degrees.  Likewise, the highs only trend 2 degrees lower.  As seen in observation 2 above, the biggest risk is the potential for the lows in December.  Although the mode, 25% percentile, and 75% percentile between the 2 analysis trend on 4-3 degrees lower, temperatures as low as 56 (8 degrees lower than June) have been obserevd.  It's hard to say that 56 degrees is cold, but to bolster the point, the low temperature does lie beyond the 25 percentile minus (1.5 X IQR).  This can be an indication of an outlier, but it can be assumed that it does not get that cold that often.  For consistant temperatures, Oahu is an excellet spot.

Temperature is a large factor in the enjoyability of water sports and ice cream; however, so is precipitation.  To explore this further and narrow our range for potential shop locations on the island; two querries were ran for June and December that find the average temperature and precipitation by station.  The station table was used to merge the station name to the measurement data.  Also, beacause surf shops intuitively will perform better by the water, all stations above 50 feet in elevation were dropped.

The results of teh querries are below:

![image](https://user-images.githubusercontent.com/91850824/153724658-383d708b-3ac5-485d-a33e-6c7b53778ec0.png)

![image](https://user-images.githubusercontent.com/91850824/153724664-ebe15e65-fd59-4eb8-b0f6-7b19e847c431.png)

Beginning with June, to meet our goal of high temperatures and low precipitation.  Waikiki and Honolulu appear to be ideal spots.  Average temperatuers between the 2 only differ by 3.5 degrees and Waikiki is teh warmest station for teh month.  Likewise, each area is only feet from the water and are also teh two driest spots measured.

Looking at December, Honolulu is the coldest average spot at 69.7 degrees; however, this is only 4 degrees from the highest observed average temperature for December.  Waikiki is within 2 degrees of the highest temperature and has the lowest reported rainfall at 0.075 inches.  Honolulu's rainfall is teh second lowest.  If temperature and low precipitation are our only critieria, the either Waikiki or Honolulu fit the bill, but due to the higher temps I feel Waikiki would have an edge.
