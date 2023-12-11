# Lets get out input
infile = open("input.txt",'r')

# So however long you hold the button down,
# It moves at that speed per millisecond
# Ex: 4 ms = 4mm/ms

# We could just brute force this problem
# Lets get input first 
times = infile.readline().rstrip('\n')
# Now lets get to the starting index
for i in range(len(times)):
    if times[i].isnumeric():
        times = times[i:]
        break
# Now do the same for the distances
dists = infile.readline().rstrip('\n')
for i in range(len(dists)):
    if dists[i].isnumeric():
        dists = dists[i:]
        break

# Now do we want to sanitize inputs? I think so
races = []
records = []
for num in times.split(" "):
    if num:
        races.append(int(num))

for num in dists.split(' '):
    if num:
        records.append(int(num))
    
print(races)
print(records)
ways = 0
for i in range(len(races)): # They will be the same length guaranteed
    curr_ways = 0
    for j in range(races[i]):
        time_left = races[i]-j
        velocity = j
        if velocity * time_left > records[i]:
            curr_ways += 1
    if ways:
        ways *= curr_ways
    else:
        ways = curr_ways

print(ways) 
        