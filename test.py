import requests
import concurrent.futures
import json
import os


# URL of the D&D 5e API for spells
api_url = "https://www.dnd5eapi.co/api/spells/"

spell_lvl = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

spell_class = {"barbarian": [], "bard": [], "cleric": [], "druid": [], "fighter": [], "monk": [], "paladin": [], "ranger": [], "rogue": [], "sorcerer": [], "warlock": [], "wizard": []}

def fetch_spell(url):
    response = requests.get("https://www.dnd5eapi.co" + url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def getAIP():
    response = requests.get(api_url)
    if response.status_code == 200:
        spell_list = response.json()["results"]
        urls = [spell["url"] for spell in spell_list]

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_url = {executor.submit(fetch_spell, url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                spell = future.result()
                if spell:
                    name = spell["name"]
                    lvl = spell["level"]
                    classes = spell["classes"]
                    class_lis = []
                    for c in classes:
                        spell_class[c["index"]].append({"name":name, "url":future_to_url[future]})
                        print(c)
                    
                    #spell_lvl[lvl].append({"name":name, "url":future_to_url[future]})

    with open('spells_class_data.txt', 'w') as file:
        json.dump(spell_class, file)
 
#getAIP()   
def dispFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            data = json.load(file)
            for i in data:
                print(i["name"])
            print(len(data))

dispFile('src/Spells.json')