## clip_to_county.py
## 20180704a

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
  
    with open('iron.json', 'w') as out_file:
        # Replace output file name as needed
        
        out_file.write(head)
        
        for line in in_file:
            lon = False
            lat = False

            for i in range(-907, -897):
                # Range is in tenths of a degree
                
                if str(i/10.0) in line:
                    lon = True
                    break

            for i in range(458, 467):
                # Range is in tenths of a degree
                
                if str(i/10.0) in line:
                    lat = True
                    break

            if lon and lat:
                out_file.write(line)

        out_file.write(tail)
