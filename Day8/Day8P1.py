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
        if char.isalpha():
            left += char
    
    for char in n[3]:
        if char.isalpha():
            right += char
    
    print(f"{node} maps to L: {left} and R: {right}")
    network[node] = [left,right]
    n = infile.readline()
    
    
curr = 'AAA'
count = 0
while curr != 'ZZZ':
    count += 1
    l_r = pattern.pop(0) # Pop the leftmost thing
    # But also append it right back to the back
    pattern.append(l_r)

    if l_r == 'R':
        # We go right'
        curr = network[curr][1]
    else:
        # We go left
        curr = network[curr][0]
print(count)
