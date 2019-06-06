import county_coords

def test_getCoords():
    testStrings = ['Lamar,TX-Lamar,tx,TX,"<Polygon><outerBoundaryIs><LinearRing><coordinates>-95.5357,33.45308 -95.55425,33.46952</coordinates></LinearRing></outerBoundaryIs></Polygon>",396.5582204,05000US48277,48277,"Lamar County, Texas",48,277,48277.0,',
                    'Caledonia,VT-Caledonia,vt,VT,"<MultiGeometry><Polygon><outerBoundaryIs><LinearRing><coordinates>-72.04249,44.15645 -72.04306,44.1566</coordinates></LinearRing></outerBoundaryIs></Polygon><Polygon><outerBoundaryIs><LinearRing><coordinates>-72.43431,44.5061</coordinates></LinearRing></outerBoundaryIs></Polygon></MultiGeometry>",193.3935422,05000US50005,50005,"Caledonia County, Vermont",50,5,50005.0,']
    answerStrings = ['-95.5357,33.45308 -95.55425,33.46952 ','-72.04249,44.15645 -72.04306,44.1566 -72.43431,44.5061 ']
    
    for i in range(len(testStrings)):
        assert county_coords.getCoords(testStrings[i]) == answerStrings[i]

def isFloat(val):
    try:
        val = float(val)
        return True
    except:
        return False

def isWord(val):
    for char in val:
        if ord(char) > 47 and ord(char) < 58:
            return False
    return True

## This test assumes the files have already been written (program has already been run)
## Thus it can not be run independently
def test_writeStateData():
    stateCodes = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','GA','GU','HI',
                'IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MP','MS',
                'MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI',
                'SC','SD','TN','TX','UT','VA','VI','VT','WA','WI','WV','WY']
    correctLineFormat = ["Armada","-85.67981","34.5678 -83.23658"]
    good = True
    
    for stateCode in stateCodes:
        file = open("../input/stateCountyCoords/"+stateCode+".csv","r")
        headerLine = file.readline()
        allLines = file.readlines()

        for line in allLines:
            line = line.split(",")

            if isWord(line[0]) == False:
                good = False
            if isFloat(line[1]) == False:
                good = False
    assert good