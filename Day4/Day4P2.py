from collections import defaultdict
# My oh My does this ugly
# But guess what?? It works!!!
infile = open("input.txt",'r')

total = 0

n = infile.readline()
card_map = defaultdict(lambda: 1) # Map of integers
card_map[1] = 1
while n:
    # First we need to do some input parsing
    sets = n.split(" | ")
    
    # So we need to get card number
    game_num = ''
    for i in range(sets[0].find(":")):
        if sets[0][i].isnumeric():
            game_num += sets[0][i]
    
        
    sets[0] = sets[0][sets[0].find(":")+2:]
    sets[0] = sets[0].split(' ')
    sets[1] = sets[1].rstrip('\n')
    sets[1] = sets[1].split(' ')
    
    game = 0

    print(f'The current map for {game_num} is {card_map}')
    # Build set

    nums = set()
    for num in sets[0]:
        if num:
            nums.add(num)
    for num in sets[1]:
        if num and num in nums:
            game += 1
    
    for i in range(card_map[int(game_num)]):
        for i in range(int(game_num)+1,int(game_num)+game+1):
            card_map[i] += 1
        
    print(f"Wins for {game_num} : {game}")
    n = infile.readline()

for key in card_map:
    total += card_map[key]

print(total)