# clip_to_county

On 2018.06.28, Microsoft released 125 million building outlines as Open Data...

-- https://blogs.bing.com/maps/2018-06/microsoft-releases-125-million-building-footprints-in-the-us-as-open-data?PC=EMMX01

The data is available on GitHub...

-- https://github.com/Microsoft/USBuildingFootprints

The data is distributed as JSON files, one per State.  I work in Wisconsin, and the State's file is 898MB.  I work in Iron County, so I wrote this quick script to clip the file down to a manageable size.

The script simply checks each entry in the JSON file to see if any of its points fall within a buffered range around the County.  All matching building outlines are written to a new JSON file.  Since Python's standard range is limited to integers...

-- https://docs.python.org/2/library/functions.html#range

...the ranges are tenths of a degree.
