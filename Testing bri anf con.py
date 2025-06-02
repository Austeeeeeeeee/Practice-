LIST_OF_PALLETES = ["HotBlack", "HotWhite",'Green','HotRed','RedMonochrom','Rainbow','Ultramarine','Violet','Sepia']
LIST_OF_AMPLIFICATION_LEVELS = ['Normal','High','Ultra']

def merge_lists(list_one, list_two) -> list:
    resulting_list = []
    for val in list_one:
        for second_value in list_two:
            resulting_list.append([val, second_value])
    return resulting_list

full_list = merge_lists(LIST_OF_PALLETES, LIST_OF_AMPLIFICATION_LEVELS)

dictionarty_with_req = {}

for pallete in LIST_OF_PALLETES:
    for amplification in LIST_OF_AMPLIFICATION_LEVELS:
        if not pallete in dictionarty_with_req:
            dictionarty_with_req[pallete] = {}

        if not amplification in dictionarty_with_req[pallete]:
            dictionarty_with_req[pallete][amplification] = {}

        dictionarty_with_req[pallete][amplification]['brigthes'] = 12
        dictionarty_with_req[pallete][amplification]['contrast'] = 12

# print(dictionarty_with_req)

# print(dictionarty_with_req['Green']['Normal'])

# print(full_list)

for combination in full_list:
	# Create combos
	# Set device params
	# Get device params
	# Get requirements
     print(dictionarty_with_req[combination[0]][combination[1]].get('brigthes'))
#     print(dictionarty_with_req[combination[0]][combination[1]].get('co'))
# #     # print(combination[0])
# #     # print(combination[1])
