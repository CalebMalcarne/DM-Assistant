import requests
import json
import random
import os

def getRandomItem():
    
    with open('dnd/items/Equipment-Categories.json', 'r') as file:
        eqpCat = json.load(file)
        index = random.randint(0, len(eqpCat) - 1)
        if len(eqpCat[index]['equipment']) - 1 > 0:
            item = eqpCat[index]['equipment'][random.randint(0, len(eqpCat[index]['equipment']) - 1)]
        itemIndex = item['index']
        print(itemIndex)
    
    with open('dnd/items/Equipment.json') as file:
        eqp = json.load(file)
        item = [x for x in eqp if x['index'] == itemIndex]
        if len(item) > 0:
            return item[0]
        else:
            with open('dnd/items/Magic-Items.json') as file:
                eqp_m = json.load(file)
                item = [x for x in eqp_m if x['index'] == itemIndex]
                return item[0]

def getRandomMagic():
    
    with open('dnd/items/Magic-Items.json') as file:
        items = json.load(file)
        item = items[random.randint(0, len(items))]
        return item

def getRandomWeapon():
    with open('dnd/items/Equipment-Categories.json', 'r') as file:
        eqpCat = json.load(file)
        itemIndex = eqpCat[0]['equipment'][random.randint(0, len(eqpCat[0]['equipment']) - 1)]['index']
        
    with open('dnd/items/Equipment.json') as file:
        eqp = json.load(file)
        item = [x for x in eqp if x['index'] == itemIndex]
        if len(item) > 0:
            return item[0]
        else:
            with open('dnd/items/Magic-Items.json') as file:
                eqp_m = json.load(file)
                item = [x for x in eqp_m if x['index'] == itemIndex]
                return item[0]

def getRandomArmor():
    
    with open('dnd/items/Equipment-Categories.json', 'r') as file:
        eqpCat = json.load(file)
        itemIndex = eqpCat[1]['equipment'][random.randint(0, len(eqpCat[1]['equipment']) - 1)]['index']
        
    with open('dnd/items/Equipment.json') as file:
        eqp = json.load(file)
        item = [x for x in eqp if x['index'] == itemIndex]
        if len(item) > 0:
            return item[0]
        else:
            with open('dnd/items/Magic-Items.json') as file:
                eqp_m = json.load(file)
                item = [x for x in eqp_m if x['index'] == itemIndex]
                return item[0]    

def getRandomMonster(DC_low, DC_high):
    
    with open('dnd/Monsters.json') as file:
        mons = json.load(file)
        filteredMons = [x for x in mons if x['challenge_rating'] >= DC_low and x['challenge_rating'] <= DC_high]
        
        final = filteredMons[random.randint(0, len(filteredMons))]
        
        return final



