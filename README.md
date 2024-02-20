# Spreadsheet Analysis

## By Maya Nesen

A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.

### Dataset details

This dataset comes from the [New York City Open Data site](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data) and is composed of data regarding arrests in New York City, across its various boroughs. Columns and data include descriptions of the crime committed, the borrough where the arrest occurred, age, race, gender, etc. The original format of the dataset was a CSV / Excel file.

Data set details:
Display some of the raw data from the original data file (the first 20 rows is enough). Use Markdown's ability to display tables - see the examples in the Markdown guide linked above.

The dataset that I chose was surprisingly pretty clean already. The column that caused the most trouble was of the police descriptions of the crimes because there were commas in them which made splitting up the data in the CSV by commas using the `.split()` function into a list challenging. I had to replace any commas in that column with dashes so that I could proceed with the scrubbing.

There were also a few missing values, usually noted as "null" or with a 0 in my dataset. I replaced them all with the string "NaN" for consistency. Even then, there were not many missing values present in my data.

To further clean and organize my data, I deleted and added several columns. I deleted columns such as "PD_CD", "LAW CODE", etc which contained codes that are most likely useful to police departments but not so much to the general public. I also deleted a column called "PD_DESC" with the police's descriptions of the arrests since there was also a "OFSC_DESC" column with an additional categorization of the crime type, likely done by the police department. But even then, there were 63 different categories of crimes. While useful surely to the police, I decided to re-organize these crime types into 8 broader categories instead: violent, property, sexual, financial, weapon-related, drug-related, vehicle-related, and miscellaneous crimes. I also added a column with the season in which the arrest occurred to categorize the column with the exact dates of arrest in each row.

Below are the links to my data files:

[Original Raw Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/NYPD_Arrest_Data__Year_to_Date__20240213.csv)

[Munged Data](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/clean_data.csv)

[Spreadsheet File](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-mayanesen/blob/main/data/nypd_arrest_data.xls)

### Analysis

Describe each of the aggregate statistic you have calculated - include a description of each and describe any insights the statistic shows that may not be obvious to someone just viewing the raw data.
If using a chart for visualization, include the chart image in the report, with a short description of what the image shows and any insights it offers. See the Markdown guide linked above for details of showing an image.
