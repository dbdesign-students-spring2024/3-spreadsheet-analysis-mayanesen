# place your code to clean up the data file below.
f = open("data/NYPD_Arrest_Data__Year_to_Date__20240213.csv", "r")
f_new = open("data/clean_data.csv", "w")

# HEADER LINE
header = f.readline()
# split to get rid of spaces between names of columns + replace with commas
column_names = header.split(",") # split on commas
# note: ARREST_BORO = Borough of arrest. B(Bronx), S(Staten Island), K(Brooklyn), M(Manhattan), Q(Queens)
# adding columns
column_names.append("SEASON")
column_names.append("CRIME_TYPE")
# deleting columns
column_names.pop(2) # delete PD_CD
column_names.pop(3) # delete KY_CD
column_names.pop(3) # delete OFSC_DESC
column_names.pop(3) # delete LAW_CODE
column_names.pop(5) # delete ARREST_PRECINCT
column_names.pop(13) # delete New Georeferenced Column

# back to csv format + write to csv
column_names_str = ','.join(column_names)
f_new.write(column_names_str + "\n")

#unique_vals = []

all_lines = f.readlines()
# filter to turn into csv
for i in range(len(all_lines)):
    #l_list = all_lines[i].split()
    l_str = all_lines[i].strip()

    # PD_DESC column has commas IN IT so the .split() function will not work correctly
    # the ones that DO have commas in it are within " " quotation marks
    # we clean the lines here to replace commas with dashes "-"
    quotes = False
    l_clean = ""
    for char in l_str:
        if char == '"':
            quotes = not quotes
        elif char == ',' and (quotes == True):
            char = "-"
        l_clean += char

    l_list = l_clean.split(",")

    # prints out the dates of arrest for just a particular month (ex: jan "01/")
    # categorizing winter as Dec, Jan, Feb. spring as Mar, Apr, May, etc etc
    if l_list[1][:3] in ["12/", "01/", "02/"]:
        l_list.append("WINTER")
    elif l_list[1][:3] in ["03/", "04/", "05/"]:
        l_list.append("SPRING")
    elif l_list[1][:3] in ["06/", "07/", "08/"]:
        l_list.append("SUMMER")
    elif l_list[1][:3] in ["09/", "10/", "11/"]:
        l_list.append("FALL")
    else:
        l_list.append("NaN")

    # treating null values to instead write "NaN" and repeated values
    if l_list[3] == "(null)":
        l_list[3] = "NaN"
    if l_list[5] == "(null)":
        l_list[5] = "NaN"
    if l_list[5] == "INTOXICATED & IMPAIRED DRIVING":
        l_list[5] = 'INTOXICATED/IMPAIRED DRIVING'
    if (l_list[7] == "") or (l_list[7] == "(null)"):
        l_list[7] = "NaN"
    if (l_list[14] == "0"):
        l_list[14] = "NaN"
    if (l_list[15] == "0"):
        l_list[15] = "NaN"
    if (l_list[16] == "0"):
        l_list[16] = "NaN"
    if (l_list[17] == "0"):
        l_list[17] = "NaN"

    # 0 = ARREST_KEY,1 = ARREST_DATE,3 = PD_DESC,7 =LAW_CAT_CD,8 =ARREST_BORO,
    # 10 =JURISDICTION_CODE,11 = AGE_GROUP,12 =PERP_SEX, 13 =PERP_RACE
    # 14 =X_COORD_CD,15 =Y_COORD_CD,16 =Latitude,17 =Longitude
    # checking columns that I'm keeping for missing values / testing for unique values
    #if l_list[0] not in unique_vals:
        #unique_vals.append(l_list[0])
    
    # creating categories for type of crime instead of having 63 kinds, narrowing down to 8 types instead
    # these crimes could of course be organized in a variety of ways, but this is what i did
    if ("DRUG" in l_list[5]) or ("ALCOHOLIC BEVERAGE" in l_list[5]) or ("CANNABIS" in l_list[5]):
        l_list.append("DRUG-RELATED")
        l_list[5] = "DRUG-RELATED"
    elif ("SEX" in l_list[5]) or (l_list[5] == "RAPE") or ("PROSTITUTION" in l_list[5]):
        l_list.append("SEXUAL")
        l_list[5] = "SEXUAL"
    elif ("WEAPON" in l_list[5]) or ("WEAP" in l_list[5]):
        l_list.append("WEAPON")
        l_list[5] = "WEAPON"
    elif ("HOMICIDE" in l_list[5]) or ("MURDER" in l_list[5]) or ("KIDNAP" in l_list[5]) or ("ASSAULT" in l_list[5]) or ("HARRASS" in l_list[5]) or ("SAFETY" in l_list[5]) or ("THE PERSON" in l_list[5]):
        l_list.append("VIOLENT")
        l_list[5] = "VIOLENT"
    elif ("ROBBERY" in l_list[5]) or ("BURGLAR" in l_list[5]) or ("LARCENY" in l_list[5]) or ("THEF" in l_list[5]) or ("ARSON" in l_list[5]) or ("STOLEN" in l_list[5]) or ("TRESPASS" in l_list[5]):
        l_list.append("PROPERTY")
        l_list[5] = "PROPERTY"
    elif ("FRAUD" in l_list[5]) or ("GAMBLING" in l_list[5]) or ("FORGERY" in l_list[5]) or ("WELFARE" in l_list[5]):
        l_list.append("FINANCIAL")
        l_list[5] = "FINANCIAL"
    elif ("VEHICLE" in l_list[5]) or ("DRIVING" in l_list[5]) or ("TRAFFIC" in l_list[5]) or ("PARKING" in l_list[5]):
        l_list.append("VEHICLE-RELATED")
        l_list[5] = "VEHICLE-RELATED"
    else:
        l_list.append("MISC")
        l_list[5] = "MISC"
    
    # now deleting columns:
    l_list.pop(2) # delete PD_CD
    l_list.pop(3) # delete KY_CD
    l_list.pop(3) # delete OFSC_DESC
    l_list.pop(3) # delete LAW_CODE
    l_list.pop(5) # delete ARREST_PRECINCT
    l_list.pop(13) # delete New Georeferenced Column


    #l_str = ','.join(l_list) # convert back to csv format
    for j in range(len(l_list)):
        f_new.write(l_list[j])
        if j != (len(l_list) - 1):
            f_new.write(",")
    f_new.write("\n")

#print(unique_vals)

f_new.close()
f.close()