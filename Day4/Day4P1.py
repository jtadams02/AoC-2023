from collections import defaultdict
infile = open("input.txt",'r')

total = 0

n = infile.readline()
card_map
while n:
    # First we need to do some input parsing
    sets = n.split(" | ")
    
    # So we need to get card number
    game_num = ''
    for i in range(sets[0].find(":")):
        if sets[0][i].isnumeric():
            game_num += sets[0][i]
    
    print(game_num)
        
    sets[0] = sets[0][sets[0].find(":")+2:]
    sets[0] = sets[0].split(' ')
    sets[1] = sets[1].rstrip('\n')
    sets[1] = sets[1].split(' ')
    
    game = 0
    # Build set

    nums = set()
    for num in sets[0]:
        if num:
            nums.add(num)
    for num in sets[1]:
        if num and num in nums:
            if game == 0:
                game = 1
            else:
                game = game * 2
    
    n = infile.readline()

print(total)