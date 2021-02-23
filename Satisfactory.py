import math
import pandas as pd
import json

parts = []
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
                parts[counter][self.building] += self.build
                parts[counter]['Leftover'] = self.leftOver
                parts[counter]['Amount'] += self.numberOf
                break

            elif counter == len(parts) - 1:
                parts.append({'Product': self.product, 'Amount': self.numberOf ,'Leftover': self.leftOver, 'Building': self.building, self.building: self.build})
                break
            
            else:
                counter += 1

def main():
    with open("Items.json", "r") as itemsList:
        data = json.load(itemsList)

    product = input("What item do you want to produce? ")

    if product not in data:
        print ("No product matching that name")
        return

    amount = int(input("\nHow many of the product do you want? "))

    def recursiveProduce(material, amountMaterial):
        Item(
            data[material]["product"],
            data[material]["perMin"],
            data[material]["itemPer"][0],
            data[material]["itemPer"][1],
            amountMaterial,
            data[material]["building"]
        ).produce()

        subComponent1 = data[material]["materials"][0]
        if subComponent1:
            recursiveProduce(subComponent1, data[material]["itemPer"][0] * amountMaterial)

        subComponent2 = data[material]["materials"][1]
        if subComponent2:
            recursiveProduce(subComponent2, data[material]["itemPer"][1] * amountMaterial)

    recursiveProduce(product, amount)

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
