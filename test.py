import math
from tabulate import tabulate
import numpy
import json

def main():
    items_json = open('Items.json')
    items_str = items_json.read()
    items = numpy.array(json.loads(items_str))[0]
    print(items["Iron Ingot"])
    myItem = items["Iron Ingot"]
    for material in myItem["materials"]:
        print(items[material])
if __name__ == '__main__': 
    main()
