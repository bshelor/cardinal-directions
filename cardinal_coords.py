import sys

def read_file_commas(filename):
    file = open(filename+".csv", 'r')
    first_line = file.readline()
    all_lines = file.readlines()

    county_dict = {}

    for line in all_lines:
        split_line = line.split(',')
        # split_line = split_line.split(' ')
        print(split_line)
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
            # split_line[item].split(' ')

        # print(new_line)
        key = ""
        for item in range(len(new_line)):

            # print(split_line[item])
            value = new_line[item].strip('"')
            # print(value)

            if item == 0:
                key = value
                county_dict[key] = {}
                county_dict[key]["long"] = []
                county_dict[key]["lat"] = []
            else:
                # value_list = value.split(' ')
                # print(value_list);
                try:
                    value = float(value)
                except:
                    value = "Bad"

                if (value != "Bad" ):
                    if (item % 2 == 0):             # even number in list, indicates latitudes
                        county_dict[key]['lat'].append(value)
                    else:                           # odd number in list, indicates longitudes
                        county_dict[key]["long"].append(value)
    # print(county_dict)
    return county_dict

def read_file_spaces(filename):
    file = open(filename+".csv", 'r')
    first_line = file.readline()
    all_lines = file.readlines()

    county_dict = {}

    for line in all_lines:
        split_line = line.split(',')
        # print(split_line)

        key = ""
        for item in range(len(split_line)):
            lat_val = ''
            long_val = ''

            # print(split_line[item])
            value = split_line[item].strip('"')
            # print(value)

            if item == 0:
                key = value
                county_dict[key] = {}
                county_dict[key]["long"] = []
                county_dict[key]["lat"] = []
            else:
                value_list = value.split(' ')
                # print(value_list)
                if len(value_list) > 1:
                    lat_val = value_list[0]
                    long_val = value_list[1]
                elif len(value_list) == 1:
                    lat_val = value_list[0]
                # print(lat_val, long_val)

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

    # print(county_dict)
    return county_dict

def calcCardDirections(data):
    final_result = {}

    for county in data:
        final_result[county] = {}
        final_result[county]["North"] = 0
        final_result[county]["South"] = 0
        final_result[county]["East"] = 0
        final_result[county]["West"] = 0

        max_long = 100.0
        min_long = -100.0
        # print(data[county]['long'])
        for coord in data[county]['long']:
            new_coord = float(coord)
            # print(new_coord)
            if (new_coord > min_long):
                min_long = new_coord
            if (new_coord < max_long):
                max_long = new_coord
            # print("max_long", max_long)
            # print("min_long", min_long)

        final_result[county]["West"] = max_long
        final_result[county]["East"] = min_long

        max_lat = 0.0
        min_lat = 100.0
        for coord in data[county]["lat"]:
            new_coord = float(coord)
            if (new_coord < min_lat):
                min_lat = new_coord
            if (new_coord > max_lat):
                max_lat = new_coord

        final_result[county]["North"] = max_lat
        final_result[county]["South"] = min_lat

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

main()
