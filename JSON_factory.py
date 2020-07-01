#
# Convert To JSON
# Convert table formatted file (csv) to JSON
#
# Copyright (c) KvinTanaka. (MIT License)
# https://www.kvintanaka.com
#

import re
import csv
import json


class JSONFromCSV:
    """Class to make JSON Format from CSV format
    Author: KvinTanaka"""

    def __init__(self, filename):
        """Initialise the class with:
        filename - The filename (without extension)
        data - The data contained in that file

        Author: KvinTanaka"""

        self.filename = filename
        self.data = None

    def read(self):
        """Read the source file formatted in csv
        Author: KvinTanaka"""

        self.data = []

        with open(self.filename + ".csv", mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data.append(row)

    def write(self):
        """Write the data to json formatted file
        Author: KvinTanaka"""

        with open(self.filename + ".json", mode='w') as json_file:
            json.dump(self.data, json_file, separators=(',', ':'))


def make(filename):
    """Factory Method Pattern for Creating JSON data from several different format
    Author: KvinTanaka"""

    # Source file is csv file
    extension = ".csv"
    if filename.endswith(extension):
        return JSONFromCSV(re.sub((extension + "$"), "", filename))

    return None
