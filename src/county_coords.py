import cardinal_coords

def getCoords(str):
    """Takes in a string representing each line of the input file
    and returns only the coordinates.

    Example Input: "King,TX-King,tx,TX,"<Polygon><outerBoundaryIs><LinearRing>
                    <coordinates>-100.51818,33.70092 -100.51825,33.719 -100.51835,33.73967"
    Returns: "-100.51818,33.70092 -100.51825,33.719 -100.51835,33.73967"
    """
    element = ""
    atCoords = False
    coords = ""

    for i in str:
        if atCoords:
            if i == "<":
                atCoords = False
                element = i
                coords += " "
            else:
                coords += i
        else:
            if i == ">":
                if element == "<coordinates":       # <coordinates> precedes all coordinate data in this file
                    atCoords = True
                element = ""
            if i == "<":
                element = i
            elif element != "":
                element += i
    return coords

def readFile(filename):
    """Reads a file from input/ and then begins data processing."""
    file = open("../input/"+filename+".csv", 'r')

    headers = file.readline()
    allLines = file.readlines()
    processData(allLines)
    file.close()

def writeStateData(stateCode, countyData):
    """Takes in a dataset and writes that to the indicated file in CSV format.
    
    Format of each line: "County,-86.41182,32.4757 -86.41177,32.46599. . ."
    """
    writeFile = open("../input/stateCountyCoords/"+stateCode+".csv", "w")
    writeFile.write("County,Coordinates"+'\n')
    for item in countyData:
        writeFile.write(item+','+countyData[item]+'\n')
    writeFile.close()

def processData(fileData):
    """This is the main function of the program.  It processes the stripped
    file data and then goes line by line through this stripped file data to 
    write the proper data (county and coordinates) to each state's CSV file. 
    This CSV file is then interpreted later in another function and sorted 
    into the cardinal points for each county.
    """
    currentState = ""
    allStates = []
    data = {}

    # goes through each line of United States Counties.csv file
    for line in fileData:
        splitLine = line.split(",")

        county = splitLine[0]
        stateCode = splitLine[3]
    
        if currentState == "":
            currentState = stateCode

        # the state has switched and we need to write the dict's data to that state's file
        elif stateCode != currentState and currentState != "":
            if currentState != '05000US45003':                # prevents writing data for '05000US45003' state
                writeStateData(currentState, data)

                # handles all cardinal coords computation and writing to final file
                processState(currentState)
            data = {}
            currentState = stateCode

        coords = getCoords(line)
        data[county] = coords

def processState(filename):
    """This processes all the necessary info for each state and writes to the
    appropriate text file.
    """
    dict = cardinal_coords.dictifyLongLats(filename)
    dict = cardinal_coords.calcCardDirections(dict)
    cardinal_coords.write_txt(dict, "../output/stateCardCoords/"+filename+"_cardDirs")

def main(): 
    readFile("United States Counties")

main()