#This is the initial file for this project - Date: 6/27/25

import random

game_state = {
    "starting_ location" : "The Tavern", #Come up with a cool name later
    "inventory" : ["Sword", "Shield", "2 Potion of Healing"],
    "health" : 100,
    "gold" : 15,
    "found_map" : False
}

dm_responses = {
    "action" : {

    }
}

global_actions = {}

# Main Game Actions
tavern_actions = {
    "look" : "The tavern is dimly lit, filled with the smell of ale and woodsmoke. A burly bartender polishes glasses behind the bar. In the corner, a hooded figure sits alone. Stairs lead up to the inn rooms to the right of the bar counter. Your trusty old traveling pack rests against your chair, worn from years of use. Various hunting trophies line the walls of the tavern, and a faded painting of a castle on the coastline hangs crooked near the door.",

    "talk to the bartender" : "The bartender sets down the glass he's been polishing and leans forward on the bar, eyeing you with interest. 'New face, eh? Haven't seen many travelers lately. Most folk are spooked by the old Moorwall Castle up on the cliffs - been abandoned for decades now.' He lowers his voice conspiratorially, 'Though between you and me, I've heard tell of treasures still hidden in those halls. Family heirlooms and such, left behind when the last lord fled. If you're feeling brave, just follow the north road out of town. Can't miss it - big imposing thing perched right on the cliff's edge. Just watch yourself... strange things been happening to those who venture too close after dark.'",

    "check the traveling pack" : "You pull your trusty traveling pack closer and unfasten the worn leather straps. Inside, you find your usual supplies - some dried rations, a water flask, flint and steel, and 50 feet of rope. Tucked into the side pocket, your fingers brush against an old piece of parchment. Ah yes, your father's map - the one he pressed into your hands on his deathbed, marked with the location of your family's ancestral home. 'When the time is right,' he'd said, 'what was lost can be found again.' You've carried it for years, never quite finding the courage to follow its path. The map shows a castle on the cliffs, with annotations in your father's careful handwriting marking various entrances and... something else written in the old tongue.",

    "inspect the map" : "You carefully unfold the aged parchment, studying your father's meticulous work. The map shows Moorwall Castle perched on the eastern cliffs, with three distinct approaches marked in fading ink. The main road leads to the front gate - 'Sealed by order of the Lord' notes your father's hand. A winding path between the cliff rocks is marked with a small symbol of a rat - below it reads 'Cellar access - beware the dwellers.' The third route shows a side entrance through what appears to be a courtyard, marked with warnings: 'Guards patrol at dusk.' The most intriguing is a phrase written in the old tongue at the bottom of the map: 'Mor'thak vel'uun.' Your father taught you enough to know it means 'Shadow's bane.' Below that, in common script: 'Speak this at the heart, when darkness rises.' Whatever that means... The map is clearly old, but the castle's location is unmistakable - north of town, where the land meets the sea.",

    "go upstairs" : "You start toward the wooden stairs, but two red-faced patrons are completely blocking the way, deep in what might be the most ridiculous argument you've ever heard. 'The dice CLEARLY showed a one!' the shorter one insists. 'But it hit your tankard!' the taller one shoots back. 'That makes it a physics roll, not a dice roll! The universe decided!' 'THE UNIVERSE DOESN'T PLAY DICE!' 'THAT'S LITERALLY WHAT DICE ARE FOR!' The bartender catches your eye and shrugs apologetically. 'They've been at this for twenty minutes. Last week it was whether a chicken could be a familiar. I'm letting them tire themselves out.' A small crowd has gathered, taking bets on who'll win the argument. One particularly enterprising halfling is selling snacks. The stairs are completely inaccessible behind this philosophical dice disaster. Perhaps the inn rooms will have to wait for another time.",
}


castle_front_actions = {}
castle_cellar_actions = {}
castle_courtyard_actions = {}
castle_interior_actions = {}
final_confrontation_actions = {}

# Transition Actions
cliff_path_actions = {}
castle_gate_actions = {}

