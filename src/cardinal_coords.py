import sys
 
def stripCountyName(str):
    for i in range(len(str)):
        if str[i] == ',':
            return str[(i+1):]
 
def getCounty(lst):
    county = ""
    for string in lst:
        for char in string:
            if char != ',':
                county += char
            else:
                return county
        county += " "

def dictifyLongLats(filename):
    """This parses the file for a state, takes each county's coordinates, and splits them into lats and longs.
    It places them in a dictionary for each county and then returns that dictionary.
    """
    file = open("../input/stateCountyCoords/"+filename+".csv", "r")

    first_line = file.readline()
    allCounties = file.readlines()

    countyDict = {}

    for countyData in allCounties:
        coords = countyData.split(' ')
        county = getCounty(coords)
        
        # handles county names with spaces
        countySplit = county.split(' ')
        coords = coords[(len(countySplit)-1):]

        coords[0] = stripCountyName(coords[0])

        countyDict[county] = {}
        countyDict[county]['long'] = []
        countyDict[county]['lat'] = []

        for coord in coords:
            if coord != None:
                coord = coord.strip('\n')
                coord = coord.split(',')

                if len(coord) == 2:
                    countyDict[county]['long'].append(coord[0])
                    countyDict[county]['lat'].append(coord[1])
    return countyDict

def read_file_commas(filename):
    """This function is deprecated.  It was used for a specific file format
    while we were taking the class.
    """
    file = open(filename+".csv", 'r')
    first_line = file.readline()
    all_lines = file.readlines()

    county_dict = {}

    for line in all_lines:
        split_line = line.split(',')
        new_line = []

        ## for sam specifically
        for item in split_line:
            el = []
            if ' ' not in item:
                new_line.append(item)
            else:
                el = item.split(' ')
                new_line.append(el[0])
                new_line.append(el[1])

        key = ""
        for item in range(len(new_line)):

            value = new_line[item].strip('"')

            if item == 0:
                key = value
                county_dict[key] = {}
                county_dict[key]["long"] = []
                county_dict[key]["lat"] = []
            else:
                try:
                    value = float(value)
                except:
                    value = "Bad"

                if (value != "Bad" ):
                    if (item % 2 == 0):             # even number in list, indicates latitudes
                        county_dict[key]['lat'].append(value)
                    else:                           # odd number in list, indicates longitudes
                        county_dict[key]["long"].append(value)
    return county_dict

def read_file_spaces(filename):
    """This function is deprecated.  It was used for a specific file format
    while we were taking the class.
    """
    file = open(filename+".csv", 'r')
    first_line = file.readline()
    all_lines = file.readlines()

    county_dict = {}

    for line in all_lines:
        split_line = line.split(',')

        key = ""
        for item in range(len(split_line)):
            lat_val = ''
            long_val = ''

            value = split_line[item].strip('"')

            if item == 0:
                key = value
                county_dict[key] = {}
                county_dict[key]["long"] = []
                county_dict[key]["lat"] = []
            else:
                value_list = value.split(' ')
                if len(value_list) > 1:
                    lat_val = value_list[0]
                    long_val = value_list[1]
                elif len(value_list) == 1:
                    lat_val = value_list[0]

                try:
                    lat_val = float(lat_val)
                except:
                    lat_val = "Bad"
                try:
                    long_val = float(long_val)
                except:
                    long_val = "Bad"

                if (lat_val != 'Bad'):
                    county_dict[key]['lat'].append(lat_val)
                if (long_val != 'Bad'):
                    county_dict[key]['long'].append(long_val)
    return county_dict

def calcMinMaxLong(longLst):
    farWest = 200.0
    farEast = -200.0
    for coord in longLst:
        new_coord = float(coord)
        if (new_coord > farEast):
            farEast = new_coord
        if (new_coord < farWest):
            farWest = new_coord
    return farWest, farEast

def calcMinMaxLat(latLst):
    farNorth = 0.0
    farSouth = 200.0
    for coord in latLst:
        new_coord = float(coord)
        if (new_coord < farSouth):
            farSouth = new_coord
        if (new_coord > farNorth):
            farNorth = new_coord
    return farNorth, farSouth

def calcCardDirections(data):
    """This takes a dictionary and calculates the highest and lowest
    latitude and longitude for each county in the dictionary
    
    Dictionary format:
    Keys --> county names
    Values --> {"lat":coordinates, "long":coordinates}
    """
    final_result = {}

    for county in data:
        final_result[county] = {}
        final_result[county]["North"] = 0
        final_result[county]["South"] = 0
        final_result[county]["East"] = 0
        final_result[county]["West"] = 0

        farWest, farEast = calcMinMaxLong(data[county]['long'])

        final_result[county]["West"] = farWest
        final_result[county]["East"] = farEast

        farNorth, farSouth = calcMinMaxLat(data[county]["lat"])

        final_result[county]["North"] = farNorth
        final_result[county]["South"] = farSouth

    return final_result

def write_csv(data, filename):
    file = open(filename+".csv", "w")
    file.write("County, North, East, South, West\n")
    for county in data:
        file.write(county+','+str(data[county]['North'])+','+
                   str(data[county]['East'])+','
                   +str(data[county]['South'])+','
                   +str(data[county]['West'])+'\n')

def write_txt(data, filename):
    file = open(filename+".txt", "w")
    file.write("County, North, East, South, West\n")
    for county in data:
        file.write(county + ':' + str(data[county]['North']) + ',' +
                   str(data[county]['East']) + ','
                   + str(data[county]['South']) + ','
                   + str(data[county]['West']) + '\n')

def main():
    """This is not being used currently to call anything.  Previously
    was used for the now deprecated version of this program.
    """
    print(sys.argv)
    if (len(sys.argv) > 9):
        print("Too many arguments! Try again")
        return

    input_file = sys.argv[sys.argv.index('-i')+1]
    output_file = sys.argv[sys.argv.index('-o')+1]
    spaces = sys.argv[sys.argv.index('-s')+1]
    output_file_type = sys.argv[sys.argv.index('-oft')+1]

    print("input_file = "+input_file)
    print("output file = "+output_file)
    print("spaces = "+spaces)
    print("output_file_type = "+output_file_type+'\n')

    if (int(spaces) == 1 and output_file_type == 'csv'):
        print("spaces and csv")
        counties = read_file_spaces(input_file)
        data = calcCardDirections(counties)
        write_csv(data, output_file)
    elif (int(spaces) == 1 and output_file_type == 'txt'):
        print("spaces and txt")
        counties = read_file_spaces(input_file)
        data = calcCardDirections(counties)
        write_txt(data, output_file)
    elif (int(spaces) == 0 and output_file_type == 'csv'):
        print("no spaces and csv")
        counties = read_file_commas(input_file)
        data = calcCardDirections(counties)
        write_csv(data, output_file)
    elif (int(spaces) == 0 and output_file_type == 'txt'):
        print("no spaces and txt")
        counties = read_file_commas(input_file)
        data = calcCardDirections(counties)
        write_txt(data, output_file)