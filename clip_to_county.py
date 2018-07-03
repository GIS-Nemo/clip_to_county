## clip_to_county.py

head = """{
  "type":"FeatureCollection",
  "features":
  [
"""

tail = """
  ]
}
"""


with open('Wisconsin.json', 'r') as i:
    with open('iron.json', 'w') as o:
        o.write(head)
        
        for line in i:
            lon = False
            lat = False
            for i in range(-907, -897): # Tenths of degree
                j = str(i/10.0)
                if j in line:
                    lon = True

            for i in range(458, 467): # Tenths of degree
                j = str(i/10.0)
                if j in line:
                    lat = True

            if lon and lat:
                o.write(line)
        o.write(tail)
