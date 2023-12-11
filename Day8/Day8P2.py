import math
# YEOOO
infile = open("input.txt")

# Get the pattern 
pattern = [char for char in infile.readline().rstrip("\n")]

# Whatever, we are not going for the most efficient solution anyways ! 

network = {}

infile.readline() # Get rid of this ugly space  
n = infile.readline()
while n:
    n = n.rstrip("\n")
    n = n.split(" ") # Split by spaces
    node = n[0] # Our little node-sky
    
    # Thankfully, every node only has 2 places to go
    # So we can make this easy 
    right = ''
    left = ''
    for char in n[2]:
        if char.isalnum():
            left += char
    
    for char in n[3]:
        if char.isalnum():
            right += char
    
    print(f"{node} maps to L: {left} and R: {right}")
    network[node] = [left,right]
    n = infile.readline()

starting_points = []
for key in network:
    if key[-1] == 'A':
        starting_points.append(key)
    
end = 1
count = 0
print(starting_points)
# So this is an LCM prob
ends = []
for start in starting_points:
    pattern_copy = pattern.copy()
    curr = start
    curr_count = 0
    while curr[-1] != 'Z':
        curr_count += 1
        l_r = pattern_copy.pop(0) # Pop the leftmost thing
        # But also append it right back to the back
        pattern_copy.append(l_r)

        if l_r == 'R':
            # We go right'
            curr = network[curr][1]
        else:
            # We go left
            curr = network[curr][0]
    ends.append(curr_count)

print(ends)
print(math.lcm(*ends))