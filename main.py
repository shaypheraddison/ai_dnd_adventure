#This is the initial file for this project - Date: 6/27/25
import random

game_state = {
    "starting location" : "The Tavern", #Come up with a cool name later
    "current location" : None,
    "inventory" : ["Sword", "Shield", "2 Potion of Healing"],
    "health" : 100,
    "gold" : 15,
    "found_map" : False
}

dm_responses = {
    "action" : {

    }
}

global_actions = {
    "show inventory" : print(game_state["inventory"]),
    "show health" : print(game_state["health"]),
    "show gold" : print(game_state["gold"]),
    "show location" : print(game_state["current location"])
}

tavern_actions = {
    "look" : "The tavern is dimly lit, filled with the smell of ale and woodsmoke. A burly bartender polishes glasses behind the bar. In the corner, a hooded figure sits alone. Stairs lead up to the inn rooms to the right of the bar counter. Your trusty old traveling pack rests against your chair, worn from years of use. Various hunting trophies line the walls of the tavern, and a faded painting of a castle on the coastline hangs crooked near the door.",

    "talk to the bartender" : "The bartender sets down the glass he's been polishing and leans forward on the bar, eyeing you with interest. 'New face, eh? Haven't seen many travelers lately. Most folk are spooked by the old Moorwall Castle up on the cliffs - been abandoned for decades now.' He lowers his voice conspiratorially, 'Though between you and me, I've heard tell of treasures still hidden in those halls. Family heirlooms and such, left behind when the last lord fled. If you're feeling brave, just follow the north road out of town. Can't miss it - big imposing thing perched right on the cliff's edge. Just watch yourself... strange things been happening to those who venture too close after dark.'",

    "check the pack" : "You pull your trusty traveling pack closer and unfasten the worn leather straps. Inside, you find your usual supplies - some dried rations, a water flask, flint and steel, and 50 feet of rope. Tucked into the side pocket, your fingers brush against an old piece of parchment. Ah yes, your father's map - the one he pressed into your hands on his deathbed, marked with the location of your family's ancestral home. 'When the time is right,' he'd said, 'what was lost can be found again.' You've carried it for years, never quite finding the courage to follow its path. The map shows a castle on the cliffs, with annotations in your father's careful handwriting marking various entrances and... something else written in the old tongue.",

    "inspect the map" : "You carefully unfold the aged parchment, studying your father's meticulous work. The map shows Moorwall Castle perched on the eastern cliffs, with three distinct approaches marked in fading ink. The main road leads to the front gate - 'Sealed by order of the Lord' notes your father's hand. A winding path between the cliff rocks is marked with a small symbol of a rat - below it reads 'Cellar access - beware the dwellers.' The third route shows a side entrance through what appears to be a courtyard, marked with warnings: 'Guards patrol at dusk.' The most intriguing is a phrase written in the old tongue at the bottom of the map: 'Mor'thak vel'uun.' Your father taught you enough to know it means 'Shadow's bane.' Below that, in common script: 'Speak this at the heart, when darkness rises.' Whatever that means... The map is clearly old, but the castle's location is unmistakable - north of town, where the land meets the sea.",

    "go upstairs" : "You start toward the wooden stairs, but two red-faced patrons are completely blocking the way, deep in what might be the most ridiculous argument you've ever heard. 'The dice CLEARLY showed a one!' the shorter one insists. 'But it hit your tankard!' the taller one shoots back. 'That makes it a physics roll, not a dice roll! The universe decided!' 'THE UNIVERSE DOESN'T PLAY DICE!' 'THAT'S LITERALLY WHAT DICE ARE FOR!' The bartender catches your eye and shrugs apologetically. 'They've been at this for twenty minutes. Last week it was whether a chicken could be a familiar. I'm letting them tire themselves out.' A small crowd has gathered, taking bets on who'll win the argument. One particularly enterprising halfling is selling snacks. The stairs are completely inaccessible behind this philosophical dice disaster. Perhaps the inn rooms will have to wait for another time.",

    "leave" : "You stand up from your table, considering heading back out into the night. But something stops you at the threshold. You came to this tavern for a reason, didn't you? The weight of your father's map in your pack seems heavier suddenly, like it's been waiting long enough. The familiar fear creeps in - the same one that's kept you from following his cryptic directions all these years. Outside, the cool night air carries the salt tang of the sea cliffs. You could leave, go back to your routine, keep wondering 'what if.' Or... you could finally see what your father wanted you to find. The choice has always been yours. You're still standing in the tavern doorway. Will you truly leave, or is tonight the night you finally seek your inheritance?",

    "order a drink" : "You wave the bartender over and request an ale. 'Coming right up!' He pulls a well-worn tankard from beneath the bar and fills it with a rich, amber brew from a large cask. The foam settles perfectly at the rim. 'That'll be 2 gold pieces. This here's my special brew - Dragon's Breath Ale. Don't worry, it's just a name. Mostly.' He winks. As you take your first sip, warmth spreads through your chest. It's surprisingly smooth with a slight honey aftertaste and just a hint of... is that cinnamon? Whatever secret ingredients he uses, you feel reinvigorated. The aches from your travels seem to fade a bit. 'First one always hits the spot, doesn't it?' the bartender grins. 'Let me know if you need anything else. You look like you've got the weight of the world on your shoulders. Or at least a heavy decision.'",

    "inspect the trophies" : "You wander over to examine the hunting trophies adorning the walls. There's an impressive variety - a massive boar's head with tusks like curved daggers, several mounted antlers from various deer, and what appears to be a stuffed badger locked in an eternal snarl. Pride of place goes to an enormous bear's head above the fireplace, its glass eyes seeming to follow patrons around the room. A small brass plaque beneath the bear reads: 'Killed by Hrolf the Bartender, Year of the Crimson Moon.' You glance back at the portly, balding bartender and try to imagine it. He catches your look and flexes one arm with a grin. 'I was younger then!'",

    "inspect the painting" : "You walk closer to the faded painting by the door, straightening it on its nail. The artist captured Moorwall Castle in what must have been its glory days - proud towers reaching skyward, pennants snapping in the coastal wind. The detail is remarkable despite the age. You can make out three distinct features: the main gatehouse facing the road, sturdy and imposing; the eastern wall where it meets the cliff face, with small cave openings visible in the rocks below; and oddly, a section of the western wall that appears to have been painted over, then sketched again with slightly different stonework. Squinting closer at that western section, you notice what might be a garden or courtyard, with tiny figures that could be patrols or... gardeners? It's hard to tell. But there's something deliberate about how the artist revised that area, like they were correcting a secret that shouldn't have been revealed. At the bottom corner, barely visible, is the artist's signature: 'R. Moorwall.' A family member, perhaps? Someone who knew the castle's secrets?",

    "approach hooded figure" : "You push back your chair and start walking toward the hooded figure in the corner. As your footsteps echo across the tavern floor, you notice their gloved hand tighten almost imperceptibly around their tankard. When you're halfway across the room, the figure suddenly stands in one fluid motion, keeping their face hidden in the depths of their hood. Before you can speak, they glide past you with unnatural grace, smelling faintly of rain and something else... something acrid, like old magic. You turn to follow, but in the brief moment it took to navigate around a drunk patron, they've vanished. The tavern door hasn't moved. The stairs remain blocked. Yet the corner where they sat is empty, only a full, untouched mug of ale proving they were ever there at all. The bartender, if he noticed anything, seems very focused on polishing that same glass. The other patrons continue their conversations as if nothing happened. But you know what you saw. Whoever that was, they definitely didn't want to chat."
}

# Transition scene to front gate of castle
no_map_front_transition = "You finish your ale, leaving a few coins on the scarred wooden table. The bartender gives you a knowing nod as you adjust your pack and head for the door. 'Good luck out there,' he calls. 'Remember - follow the north road. Can't miss it.' The cool night air hits you as you step outside, carrying the salt tang of the distant sea. The cobblestone streets of town quickly give way to a dirt road leading north, just as the bartender described. As you walk, the sounds of the tavern fade behind you, replaced by the whisper of wind through tall grass and the distant crash of waves against cliffs. After about an hour's trek, the road begins to climb. The moon breaks through the clouds, and there it is - Moorwall Castle, perched on the cliff's edge like a great stone bird of prey. Even in its abandoned state, it's imposing. Dark windows stare down at you like hollow eyes. You follow the road right up to the main gate - a massive wooden door reinforced with rusted iron bands. Heavy chains and an ancient padlock bar your way. But something feels off... the dust around the gate has been disturbed recently. You're not the first person to come here."

map_found_front_transition = "You finish your ale, leaving a few coins on the scarred wooden table. The bartender gives you a knowing nod as you adjust your pack and head for the door. 'Good luck out there,' he calls. 'Remember - follow the north road. Can't miss it.' The cool night air hits you as you step outside, carrying the salt tang of the distant sea. The cobblestone streets of town quickly give way to a dirt road leading north, just as the bartender described. As you walk, the sounds of the tavern fade behind you, replaced by the whisper of wind through tall grass and the distant crash of waves against cliffs. After about an hour's trek, the road begins to climb. The moon breaks through the clouds, and there it is - Moorwall Castle, perched on the cliff's edge like a great stone bird of prey. Even in its abandoned state, it's imposing. Dark windows stare down at you like hollow eyes. You follow the road right up to the main gate - a massive wooden door reinforced with rusted iron bands. It's exactly as your father's map described: 'Sealed by order of the Lord.' Indeed, heavy chains and an ancient padlock bar your way. But something feels off... the dust around the gate has been disturbed recently. You're not the first person to come here. Time to find that hidden switch the map mentioned. But where would someone hide such a mechanism?"

castle_front_actions = {

}

castle_cellar_actions = {}
castle_courtyard_actions = {}
castle_interior_actions = {}
final_confrontation_actions = {}

# Transition Actions
cliff_path_actions = {}
castle_gate_actions = {}

