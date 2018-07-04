## random_sample_data.py
## 20180704

import random

head = """{
  "type":"FeatureCollection",
  "features":
  [
"""

tail = """
  ]
}
"""


with open('Wisconsin.json', 'r') as in_file:
  # Replace input file name as needed
  
    with open('test_in.json', 'w') as out_file:
        # Replace output file name as needed
        
        out_file.write(head)

        for line in in_file:
            lon = False
            lat = False

            for i in range(-930, -870):
                # Range is in tenths of a degree
                # Wisconsin: -92.9 to -86.7
                
                if str(i/10.0) in line:
                    lon = True
                    break

            for i in range(447, 471):
                # Range is in tenths of a degree
                # Wisconsin: 42.5 to 47.0
                
                if str(i/10.0) in line:
                    lat = True
                    break

            if lon and lat:
                if random.random() < .01:
                    # Sample one one-hundredth of the data
                    
                    out_file.write(line)

        out_file.write(tail)
