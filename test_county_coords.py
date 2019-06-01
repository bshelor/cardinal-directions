import county_coords

def test_getCoords():
    testStrings = ['Lamar,TX-Lamar,tx,TX,"<Polygon><outerBoundaryIs><LinearRing><coordinates>-95.5357,33.45308 -95.55425,33.46952</coordinates></LinearRing></outerBoundaryIs></Polygon>",396.5582204,05000US48277,48277,"Lamar County, Texas",48,277,48277.0,',
                    'Caledonia,VT-Caledonia,vt,VT,"<MultiGeometry><Polygon><outerBoundaryIs><LinearRing><coordinates>-72.04249,44.15645 -72.04306,44.1566</coordinates></LinearRing></outerBoundaryIs></Polygon><Polygon><outerBoundaryIs><LinearRing><coordinates>-72.43431,44.5061</coordinates></LinearRing></outerBoundaryIs></Polygon></MultiGeometry>",193.3935422,05000US50005,50005,"Caledonia County, Vermont",50,5,50005.0,']
    answerStrings = ['-95.5357,33.45308 -95.55425,33.46952 ','-72.04249,44.15645 -72.04306,44.1566 -72.43431,44.5061 ']
    
    for i in range(len(testStrings)):
        assert county_coords.getCoords(testStrings[i]) == answerStrings[i]

# def test_answer():
#     assert func(3) == 5