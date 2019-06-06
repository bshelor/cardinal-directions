# cardinal-directions (Old info.  Will be updated soon)

This program will take in a CSV or Excel file of geographical coordinates and return the four cardinal directions from each row of data.

Each row of the input file needs to formatted as such (`|` representing a new cell in the file):
- `Title | Longitude,Latitude | Longitude,Latitude | etc.` 

Run `cardinal_coords.py` to open the command line interface for this program

## Next Steps
- Comprehensive testing
- Make `county_coords.py` the executable.  `cardinal_coords.py` should not get touched by user
- Allow user to specify input file, output file name, and file format (long-lat or lat-long)
- Autonomously determine how the file data (longs-lats) is separated (commas or spaces), then parse based on that

