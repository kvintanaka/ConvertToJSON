#
# Convert To JSON
# Convert table formatted file (csv) to JSON
#
# Copyright (c) KvinTanaka. (MIT License)
# https://www.kvintanaka.com
#

import sys
import re
import JSON_factory


# --- Convert To JSON - Main ---


def main():
    """Start point"""

    filename = str(sys.argv[1])
    input_format = re.sub(".*\\.", "", filename)

    if input_format.casefold() == "JSON".casefold():
        print("Input file must be other than json")
    else:
        # Begin the main task to convert
        task = JSON_factory.make(filename)
        if task is not None:
            task.read()
            task.write()


if __name__ == "__main__":
    main()
