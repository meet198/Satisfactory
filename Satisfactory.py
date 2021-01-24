import math
import pandas as pd
import json
from json import JSONEncoder
from types import SimpleNamespace

parts = []

def main():
    class Item:
        leftOver = 0
        numberOf = 0
        def __init__(self, product, perMin, itemPer, itemPer2 ,numberOf, building):
            self.product = product
            self.perMin = perMin
            self.itemPer = itemPer 
            self.numberOf = round(numberOf, 1)
            self.building = building
            self.itemPer2 = itemPer2

        def produce(self):
            counter = 0
            build = 0
            self.build = math.ceil(self.numberOf / self.perMin)
            self.leftOver = round(self.build * self.perMin - self.numberOf)

            while counter < len(parts)+1:

                if not parts:
                    parts.append({'Product': self.product, 'Amount': self.numberOf, 'Leftover': self.leftOver, 'Building': self.building, self.building: self.build})
                    break  

                elif parts[counter]['Product'] == self.product:
                    parts[counter][self.building] = self.build
                    parts[counter]['Leftover'] = self.leftOver
                    parts[counter]['Amount'] += self.numberOf
                    break

                elif counter == len(parts) - 1:
                    parts.append({'Product': self.product, 'Amount': self.numberOf ,'Leftover': self.leftOver, 'Building': self.building, self.building: self.build})
                    break
                
                else:
                    counter += 1

    with open("Items.json", "r") as itemsList:
        data = json.load(itemsList)

    product = input("What item do you want to produce? ")
    amount = int(input("\nHow many of the product do you want? "))

    def recursiveProduce(material1, material2, amountMaterial1, amountMaterial2):
    
        if material1 in data:  
            makeMat1 = Item(data[material1]["product"], data[material1]["perMin"], data[material1]["itemPer"][0], data[material1]["itemPer"][1], amountMaterial1, data[material1]["building"])
            makeMat1.produce()
            recursiveProduce(data[material1]["materials"][0], data[material1]["materials"][1], data[material1]["itemPer"][0] * amountMaterial1, data[material1]["itemPer"][1] * amountMaterial1)

        if material2 in data:
            makeMat2 = Item(data[material2]["product"], data[material2]["perMin"], data[material2]["itemPer"][0], data[material2]["itemPer"][1], amountMaterial2, data[material2]["building"])
            makeMat2.produce()
            recursiveProduce(data[material2]["materials"][0], data[material2]["materials"][1], data[material2]["itemPer"][0] * amountMaterial2, data[material2]["itemPer"][1] * amountMaterial2)
    
    i = len(data)
    for x in data:

        if product == data[x]["product"]:
            makeItem = Item(data[x]["product"], data[x]["perMin"], data[x]["itemPer"][0], data[x]["itemPer"][1], amount, data[x]["building"])
            makeItem.produce()
            recursiveProduce(data[x]["materials"][0], data[x]["materials"][1], data[x]["itemPer"][0] * amount, data[x]["itemPer"][1] * amount)
            break

        elif i == 1: print ("No product matching that name")
        i -= 1

    if parts:
        miner = []
        foundry = []
        smelter = []
        constructor = []
        assembler = []

        for i in range(0, len(parts)):
            if parts[i]['Building'] == 'miner':
                miner.append(parts[i])
            elif parts[i]['Building'] == 'smelter':
                smelter.append(parts[i])
            elif parts[i]['Building'] == 'foundry':
                foundry.append(parts[i])
            elif parts[i]['Building'] == 'constructor':
                constructor.append(parts[i])
            elif parts[i]['Building'] == 'assembler':
                assembler.append(parts[i])

        partsDisplay = miner + smelter + foundry + constructor + assembler 
        keys = []
        vals = []
        for data in partsDisplay:
            val = []

            for k,v in data.items():
                keys.append(k)
                val.append(v)
            vals.append(val)

        print(pd.DataFrame([v for v in vals], columns=['Product', 'Amount' ,'Leftover', 'Building', 'Needed']))

if __name__ == '__main__': 
    main()
