import math
import pandas as pd
parts = []
def main():
    class Item:
        leftOver = 0
        totalAmount = 0
        def __init__(self, Product, perMin, itemPer, itemPer2 ,numberOf, building):
            self.product = Product
            self.perMin = perMin
            self.itemPer = itemPer 
            self.numberOf = numberOf
            self.building = building
            self.itemPer2 = itemPer2

        def produce(self):
            global parts
            global build
            global counter
            if self.building != 'miner' and self.building != 'foundry' and self.numberOf < self.perMin :
                self.perMin = self.numberOf

            self.totalAmount += self.numberOf
            counter = 0
            build = 0
            self.build = math.ceil(self.totalAmount / self.perMin)
            self.leftOver = round(self.build * self.perMin - self.totalAmount)
            while counter < len(parts)+1:
                if not parts:
                    parts.append({'Product': self.product, 'Amount': self.totalAmount, 'Leftover': self.leftOver, 'Building': self.building, self.building: self.build})
                    break  
                elif parts[counter]['Product'] == self.product:
                    parts[counter][self.building] = self.build
                    parts[counter]['Leftover'] = self.leftOver
                    parts[counter]['Amount'] = self.totalAmount
                    break
                elif counter == len(parts) - 1:
                    parts.append({'Product': self.product, 'Amount': self.totalAmount ,'Leftover': self.leftOver, 'Building': self.building, self.building: self.build})
                    break
                else:
                    counter += 1
    ironOre = Item("Iron Ore", 60, 1, 0, 0, "miner")   
    ironIngot = Item("Iron Ingot", 30, 1, 0, 0, "smelter")      
    ironPlate = Item("Iron Plate", 20, 30/20, 0, 0, "constructor")
    ironRod = Item("Iron Rod", 15, 15/15, 0, 0, "constructor")
    screws = Item("Screws", 40, 10/40, 0, 0, "constructor")
    reinforcedPlate = Item("Reinforced Plate", 15, 90/15, 250/15, 0, "assembler")
    rotor = Item("Rotor", 4, 20/4, 100/4, 0, "assembler")
    modularFrame = Item("Modular Frame", 2, 3/2, 12/2, 0, "assembler")
    smartPlating = Item("Smart Plating", 2, 2/2, 2/2, 0, "assembler")
    coal = Item("Coal", 60, 1, 0, 0, "miner")
    steelIngot = Item("Steel Ingot", 45, 45/45, 45/45, 0, "foundry")
    steelBeam = Item("Steel Beam", 15, 60/15, 0, 0, "constructor")
    steelPipe = Item("Steel Pipe", 20, 30/20, 0, 0, "constructor")
    versatileFramework = Item("Versatile Framework", 5, 2.5/5, 30/5, 0, "assembler")
    copperOre = Item("Copper Ore", 60, 1, 0, 0, "miner")
    copperIngot = Item("Copper Ingot", 30, 1, 0, 0, "smelter")
    wire = Item("wire", 30, 15/30, 0, 0, "constructor")
    copperSheet = Item("Copper Sheet", 10, 20/10, 0, 0, "constructor")
    cable = Item("Cable", 30, 60/30, 0, 0, "constructor")
    stator = Item("Stator", 5, 15/5, 40/5, 0, "assembler")
    automatedWiring = Item("Automated Wiring", 2.5, 2.5/2.5, 50/2.5, 0, "assembler")
    def IronOre(numberOf):
        ironOre.numberOf = numberOf
        ironOre.produce()

    def IronIngot(numberOf):
        ironIngot.numberOf = numberOf
        ironIngot.produce()
        IronOre(numberOf)

    def IronPlate(numberOf):
        ironPlate.numberOf = numberOf
        ironPlate.produce()
        IronIngot(numberOf*ironPlate.itemPer)

    def IronRod(numberOf):
        ironRod.numberOf = numberOf
        ironRod.produce()
        IronIngot(numberOf*ironRod.itemPer)
    
    def Screws(numberOf):
        screws.numberOf = numberOf
        screws.produce()
        IronRod(numberOf*screws.itemPer)
    
    def ReinforcedPlate(numberOf):
        reinforcedPlate.numberOf = numberOf
        reinforcedPlate.produce()
        IronPlate(numberOf*reinforcedPlate.itemPer)
        Screws(numberOf*reinforcedPlate.itemPer2)
    
    def Rotor(numberOf):
        rotor.numberOf = numberOf
        rotor.produce()
        IronRod(numberOf*rotor.itemPer)
        Screws(numberOf*rotor.itemPer2) 

    def ModularFrame(numberOf):
        modularFrame.numberOf = numberOf
        modularFrame.produce()
        ReinforcedPlate(numberOf*modularFrame.itemPer)
        IronRod(numberOf*modularFrame.itemPer2)
    
    def SmartPlating(numberOf):
        smartPlating.numberOf = numberOf
        smartPlating.produce()
        ReinforcedPlate(numberOf*smartPlating.itemPer)
        Rotor(numberOf*smartPlating.itemPer2)

    def Coal(numberOf):
        coal.numberOf = numberOf
        coal.produce()
    
    def SteelIngot(numberOf):
        steelIngot.numberOf = numberOf
        steelIngot.produce()
        Coal(numberOf*steelIngot.itemPer)
        IronOre(numberOf*steelIngot.itemPer2)
    
    def SteelBeam(numberOf):
        steelBeam.numberOf = numberOf
        steelBeam.produce()
        SteelIngot(numberOf*steelBeam.itemPer)

    def SteelPipe(numberOf):
        steelPipe.numberOf = numberOf
        steelPipe.produce()
        SteelIngot(numberOf*steelPipe.itemPer)

    def VersatileFramework(numberOf):
        versatileFramework.numberOf = numberOf
        versatileFramework.produce()
        ModularFrame(numberOf*versatileFramework.itemPer)
        SteelBeam(numberOf*versatileFramework.itemPer2)

    def CopperOre(numberOf):
        copperOre.numberOf = numberOf
        copperOre.produce()
    
    def CopperIngot(numberOf):
        copperIngot.numberOf = numberOf
        copperIngot.produce()
        CopperOre(numberOf)
    
    def Wire(numberOf):
        wire.numberOf = numberOf
        wire.produce()
        CopperIngot(numberOf*wire.itemPer)

    def CopperSheet(numberOf):
        copperSheet.numberOf = numberOf
        copperSheet.produce()
        CopperIngot(numberOf*copperSheet.itemPer)
    
    def Cable(numberOf):
        cable.numberOf = numberOf
        cable.produce()
        Wire(numberOf*cable.itemPer)

    def Stator(numberOf):
        stator.numberOf = numberOf
        stator.produce()
        SteelPipe(numberOf*stator.itemPer)
        Wire(numberOf*stator.itemPer2)

    def AutomatedWiring(numberOf):
        automatedWiring.numberOf = numberOf
        automatedWiring.produce()
        Stator(numberOf*automatedWiring.itemPer)
        Cable(numberOf*automatedWiring.itemPer2)
    ReinforcedPlate(20)

    
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

