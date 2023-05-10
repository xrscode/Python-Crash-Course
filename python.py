menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22,}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

empty_dict = {}

menu["cheesecake"] = 8

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

>>> building_heights["Burj Khalifa"]
828
>>> building_heights["Ping An"]
599

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])

print(building_heights["Landmark 81"])

key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])