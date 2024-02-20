# Spreadsheet Analysis

## By Maya Nesen

A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.

### Data set details

This dataset comes from the [New York City Open Data site](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data) and is composed of data regarding arrests in New York City, across its various boroughs. Columns and data include descriptions of the crime committed, the borrough where the arrest occurred, age, race, gender, etc. The original format of the dataset was a CSV / Excel file.

| ARREST_KEY | ARREST_DATE | PD_DESC                          | LAW_CAT_CD | ARREST_BORO | JURISDICTION_CODE | AGE_GROUP | PERP_SEX | PERP_RACE | X_COORD_CD,Y_COORD_CD | Latitude         | Longitude         | SEASON | CRIME_TYPE |
| ---------- | ----------- | -------------------------------- | ---------- | ----------- | ----------------- | --------- | -------- | --------- | --------------------- | ---------------- | ----------------- | ------ | ---------- |
| 261271301  | 01/03/2023  | STRANGULATION 1ST                | F          | S           | 0                 | 25-44     | M        | WHITE     | 962808,174275         | 40.644996        | -74.077263        | WINTER | VIOLENT    |
| 261336449  | 01/04/2023  | "ROBBERY-OPEN AREA UNCLASSIFIED" | F          | K           | 0                 | <18       | M        | BLACK     | 995118,155708         | 40.594054        | -73.960866        | WINTER | PROPERTY   |
| 261328047  | 01/04/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 18-24     | M        | BLACK     | 1007694,219656        | 40.769552        | -73.915361        | WINTER | VIOLENT    |
| 261417496  | 01/05/2023  | "BURGLARY-UNCLASSIFIED-UNKNOWN"  | F          | B           | 0                 | 25-44     | F        | BLACK     | 1007174,239542        | 40.824135        | -73.91717         | WINTER | PROPERTY   |
| 261583093  | 01/08/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | K           | 0                 | 25-44     | M        | BLACK     | 984110,188363         | 40.683691        | -74.000504        | WINTER | VIOLENT    |
| 261611504  | 01/09/2023  | "ARSON 2-3-4"                    | F          | B           | 71                | 25-44     | M        | WHITE     | 1028555,246897        | 40.84424         | -73.839868        | WINTER | PROPERTY   |
| 261892107  | 01/14/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | K           | 0                 | 25-44     | M        | BLACK     | 996541,199439         | 40.714082        | -73.955662        | WINTER | VIOLENT    |
| 261926460  | 01/14/2023  | "ARSON 2-3-4"                    | F          | K           | 0                 | 25-44     | M        | BLACK     | 1000520,168264        | 40.628508        | -73.941384        | WINTER | PROPERTY   |
| 262973934  | 02/03/2023  | STRANGULATION 1ST                | F          | M           | 0                 | 25-44     | M        | BLACK     | 1003818,253167        | 40.861538        | -73.929256        | WINTER | VIOLENT    |
| 263113943  | 02/06/2023  | "ASSAULT 2-1-UNCLASSIFIED"       | F          | B           | 0                 | 45-64     | F        | BLACK     | 1010036,246475        | 40.843155        | -73.906802        | WINTER | VIOLENT    |
| 264092077  | 02/23/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 25-44     | F        | BLACK     | 1057766,203992        | 40.726284        | -73.73476         | WINTER | VIOLENT    |
| 261635779  | 01/10/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 18-24     | M        | BLACK     | 1050620,157860        | 40.599718        | -73.760999        | WINTER | VIOLENT    |
| 261739896  | 01/11/2023  | "TRESPASS 2- CRIMINAL"           | M          | K           | 0                 | 18-24     | F        | BLACK     | 991150,192509         | 40.695068        | -73.975116        | WINTER | PROPERTY   |
| 264206386  | 02/25/2023  | STRANGULATION 1ST                | F          | K           | 0                 | 45-64     | M        | BLACK     | 1000520,168264        | 40.628508        | -73.941384        | WINTER | VIOLENT    |
| 261361209  | 01/04/2023  | ASSAULT 3                        | M          | B           | 0                 | 18-24     | F        | BLACK     | 1007528,234117        | 40.809243        | -73.915909        | WINTER | VIOLENT    |
| 264544903  | 03/04/2023  | STRANGULATION 1ST                | F          | Q           | 0                 | 25-44     | M        | BLACK     | 1007694,219656        | 40.769552        | -73.915361        | SPRING | VIOLENT    |
| 262362107  | 01/23/2023  | "ROBBERY-OPEN AREA UNCLASSIFIED" | F          | B           | 0                 | 25-44     | M        | BLACK     | 1026486,262591        | 40.887325        | -73.847247        | WINTER | PROPERTY   |
| 262497973  | 01/25/2023  | RAPE 3                           | F          | B           | 0                 | <18       | M        | BLACK     | 1017478,256069        | 40.8694704770483 | -73.8798608037303 | WINTER | SEXUAL     |

The dataset was surprisingly pretty clean already. The column that caused the most trouble was of the police descriptions of the crimes because there were commas in them which made splitting up the data in the CSV by commas using the `.split()` function into a list challenging. I had to replace any commas in that column with dashes so that I could proceed with the scrubbing.

There were also a few missing values, usually noted as `null` or `0` in my dataset. I replaced them all with the string "NaN" for consistency. Even then, there were not many missing values present in my data.

To further clean and organize my data, I deleted and added several columns. I deleted columns such as "PD_CD", "LAW CODE", etc which contained codes that are most likely useful to police departments but not so much to the general public. I also deleted a column called "OFSC_DESC" with categorizations of the crime types since there is also a "PD_DESC" column with the police's descriptions of the arrests, likely done by the police department. But even then, there were 63 different categories of crimes in the "OFSC_DESC" column. While useful surely to the police, I decided to re-organize these crime types into 8 broader categories instead: violent, property, sexual, financial, weapon-related, drug-related, vehicle-related, and miscellaneous crimes. I also added a column with the season in which the arrest occurred to categorize the column with the exact dates of arrest in each row.

Below are the links to my data files:

[Original Raw Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/NYPD_Arrest_Data__Year_to_Date__20240213.csv)

[Munged Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/clean_data.csv)

[Spreadsheet File](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/nypd_arrest_data.xls)

### Analysis

This was a bit challenging given that the data in my dataset is only categorical or descriptive and not numeric. Therefore, I primarily used the `COUNTIF` function since statistics with categorical data usually have to do with frequency. I also used `AVERAGE`, `SUM`, `MIN`, `MAX`, and `PRODUCT`. I wanted to explore a few aspects of my dataset, including using the columns I had made.

I firstly wanted to examine the age column. The dataset already organized ages categorically: `<18`, `18-24`, `25-44`, `45-64`, `65+`. I wanted to calculate the average age of crime but could not do so directly. So I first used the `COUNTIF` function to find the counts for each of these age ranges. I then split up the age ranges by the lower and upper bounds, taking 12 as the lower bound of `<18` since it is [the lowest age for juvenile delinquency in the state of New York](https://ocfs.ny.gov/programs/youth/raise-the-lower-age/#:~:text=Response%20and%20Supports-,Overview,of%20the%20Laws%20of%202022) and 80 as the upper bound since that is roughly around [the average age of death in New York](https://www.nyc.gov/site/doh/about/about-doh/healthynyc.page#:~:text=Life%20expectancy%20%E2%80%94%20the%20average%20number,in%20lifespan%20in%20a%20century). I then used `AVERAGE` to find the midpoint of the those bounds, followed by `PRODUCT` of the midpoint and the count from earlier to prepare to calculate the average age. I then used `SUM` to find the total counts, which I then divided from the product to get our average. The average age was thus about 36 years old. This outcome makes the most sense, not only because the `25-44` range had the highest count of crimes, but also because it logically would be around the age of an adult. With the counts, I also created a histogram to further visualize the counts. ![Histogram of Crimes by Age Range](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/Crime_histogram.png)

Similarly, I investigated the various categories of crime based on the column that I added. I once again used the `COUNTIF` function to determine the counts for the various categories. I thus created a pie chart below to visualize the proportions of these counts. I also used `MIN` to determine the category with the lowest count which was sexual crimes, and `MAX` to determine the category with the highest count which was property crimes, which includes various forms of theft. ![Pie Chart of Crime Types](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/pie_chart.png)

Lastly, I created another analysis of categories by the season in which the crimes occured using `COUNTIF` and found the `MIN` and `MAX` of the counts as well. The season with the highest amount of crime is spring and the one with the lowest is fall. These were what I expected as seasons of extreme weather like winter and summer cause more people to stay indoors.
