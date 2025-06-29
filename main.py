#This is the initial file for this project - Date: 6/27/25

import random


player_classes = {
    "Warrior" : {
        "inventory" : ["Short Sword", "Shield", "15 Gold", "2 Potions of Healing"],
        "health" : 125,
        "armor" : "heavy"
        # "speed" : 2
    },

    "Rogue" : {
        "inventory" : ["Dual Daggers", "15 Gold", "2 Potions of Sneaking", "1 Potion of Healing"],
        "health" : 85,
        "armor" : "light"
        # "speed" : 4
    },

    "Wizard" : {
        "inventory" : ["Wooden Staff", "Sir Larry's Wonderful Book of Spells", "15 Gold", "1 Potion of Healing", "1 Potion of Mana"],
        "health" : 100,
        "mana" : 150,
        "armor" : "light"
        # "speed" : 2
    },

    "Hunter" : {
        "inventory" : ["Sturdy Bow", "25 Iron Arrows", "15 Gold", "1 Potion of Healing", "1 Magical Trap"],
        "health" : 100,
        "armor" : "medium",
        # "speed" : 3
    }
}


# dm_responses = {
#     "action" : {

#     }
# }

player_choice = input(str("What class would you like to play as? Please select Warrior, Rogue, Wizard or Hunter:\n" )).lower()

game_state = {
    "location" : "The Tavern", #Come up with a cool name later
    "inventory" : player_classes[player_choice["inventory"]],
    "health" : player_classes[player_choice["health"]]
}

