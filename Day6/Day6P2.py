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
races = ''
records = ''
for num in times.split(" "):
    if num:
        races += num

for num in dists.split(' '):
    if num:
        records += num
    
print(races)
print(records)

# Again lets just brute force it?
races = int(races)
records = int(records)
ways = 0
for i in range(races):
    time_left = races - i
    velocity = i
    if velocity * time_left > records:
        ways += 1

print(ways)

        