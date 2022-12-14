#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Nadia Barbo (nadia.barbo@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% less efficent way to bring in data

# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[5]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude

#%% Learning new stuff

#Connects Python to file
##fileObj = open('data/raw/sara.txt','r')

# Print information to the use
##print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#reading in a text file
##fileObj = open('data/raw/sara.txt','r')

#printing lines from the text file
##print(fileObj.readline())
#each time you rerun this, it will output the next line

#storing what is in a single 
##lineString = fileObj.readline(); print(lineString)

#resetting cursor to first line
##fileObj.seek(0)

#Here we point the variable “lineList” to the entire list of lines, and then print the last item in that list (saving all lines instead of just one)
##lineList = fileObj.readlines(); print(lineList[-1])

#closes connection to release Python's hold on the file
##fileObj.close()

#creating a new text file
##newFile = open('newfile.txt','w')

#writing string to the new file
##newFile.write("Hello world\nIt's me")

#closing new file
##newFile.close()

#adding to an existing file using append
##open('newfile.txt','a').write("\nSee what I did here")

#%% Implementing the new things I learned

#Create a variable pointing to the data file
##file_object = open(file=file_name,mode='r')

#Read contents of file into a list
##line_list = file_object.readlines()

#Close the file
##file_object.close()

#Pretend we read one line of data from the file
##lineString = line_list[100]

#Split the string into a list of data items
##lineData = lineString.split()

#Extract items in list into variables
##record_id = lineData[0]
##obs_date = lineData[2]
##obs_lc = lineData[4]
##obs_lat = lineData[6]
##obs_lon = lineData[7]

#Print the location of sara
##print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#%% Doing the above but using a for loop to get all lines of data

#Create a variable pointing to the data file
##file_name = 'data/raw/sara.txt'

#Create a file object from the file
##file_object = open(file=file_name,mode='r')

#Read contents of file into a list
##line_list = file_object.readlines()

#Close the file
##file_object.close()

#Pretend we read one line of data from the file
##for lineString in line_list[17:]:

    #Split the string into a list of data items
   ## lineData = lineString.split()
    
    #Extract items in list into variables
   ## record_id = lineData[0]
   ## obs_date = lineData[2]
   ## obs_lc = lineData[4]
   ## obs_lat = lineData[6]
   ## obs_lon = lineData[7]
    
    #Print the location of sara
   ## print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#%% Another way to do thing above

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

#Create a variable pointing to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the file
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#creating empty dictionaries
date_dict = {}
location_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list:
    
    #check to see if the linestring is a data line
    if lineString[0] in ('#','u'):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    
    #add items to dictionaries, if lc criteria is met
    if obs_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat,obs_lon)
    
    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#Create an empty key list
matching_keys = []

# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)
        
# Report whether no keys were found
if len(matching_keys) == 0:
    print(f"Sara was not located on {user_date}")
else:
    #Reveal locations for each key in matching_keys
    for matching_key in matching_keys:
        obs_lat, obs_lon = location_dict[matching_key]
        print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
#%% loading in all the data using a while loop - so it only saves one line at a time



#Create a variable pointing to the data file
##file_name = 'data/raw/sara.txt'

#Create a file object from the file
##file_object = open(file=file_name,mode='r')

#Read one line at a time of contents of file into a list
##lineString = file_object.readline()

#Extract one data line into a variable
##while lineString:
    
    #check to see if the linestring is a data line
   ## if lineString[0] in ('#','u'):
        ##lineString = file_object.readline()
       ## continue

    #Split the string into a list of data items
    ##lineData = lineString.split()
    
    #Extract items in list into variables
   ## record_id = lineData[0]
   ## obs_date = lineData[2]
   ## obs_lc = lineData[4]
   ## obs_lat = lineData[6]
   ## obs_lon = lineData[7]
    
    #Print the location of sara
   ## print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    
    #move to the next line in the file
    ##lineString = file_object.readline()
    
#close the file object
##file_object.close()