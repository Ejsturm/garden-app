# Hardcoded values for the season and plant type
season = input("Specify season: ").strip().lower()
plant_type = input("Specify plant type (flower, vegetable): ").strip().lower()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season.
# Season dictionary with season name keys and advice values.
season_name = {
    "spring": "No advice for this season.\n",
    "summer": "Water your plants regularly and provide some shade.\n",
    "fall": "No advice for this season.\n",
    "winter": "Protect your plants from frost with covers.\n"
}
if season not in season_name:
    advice = "No advice for this season.\n"
else:
    advice = season_name[season]

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
