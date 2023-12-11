# Thankfully, this input seems to follow the same format, or else I may quit
# This is really simple, just took a while to process all the data
# There are definitely better ways to do input parsing, however, I do not know how!
# It works thought!

infile = open("input.txt",'r')

# Begin parsing our input
input = []
n = infile.readline()
while n:
    n = n.rstrip("\n")
    if len(n) != 0:
        input.append(n)
    
    n = infile.readline()

# Now lets collect our seeds
# First strip the seeds
input[0] = input[0].lstrip("seeds: ")
# Then put every seed into a set
seeds = set()
for seed in input[0].split(" "):
    seeds.add(int(seed))
# Thank god space/time complexity does not matter
# cuz I am just going to make the space HUGE
i = 0
s_s = set() # Seed to soil
s_f = set() # Soil to fertilizer
f_w = set() # fertilizer to water
w_l = set() # water to light
l_t = set() # Light to temp
t_h = set() # Temp to humidity
h_l = set() # Humidity to Location

while i < len(input):
    if input[i] == "seed-to-soil map:":
        print(input[i])
        i += 1
        while input[i] != "soil-to-fertilizer map:":
            this_line = input[i].split(' ')
            s_s.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "soil-to-fertilizer map:":
        print(input[i])
        i += 1
        while input[i] != "fertilizer-to-water map:":
            this_line = input[i].split(' ')
            s_f.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "fertilizer-to-water map:":
        print(input[i])
        i += 1
        while input[i] != "water-to-light map:":
            this_line = input[i].split(' ')
            f_w.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "water-to-light map:":
        print(input[i])
        i += 1
        while input[i] != "light-to-temperature map:":
            this_line = input[i].split(' ')
            w_l.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "light-to-temperature map:":
        print(input[i])
        i += 1
        while input[i] != "temperature-to-humidity map:":
            this_line = input[i].split(' ')
            l_t.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "temperature-to-humidity map:":
        print(input[i])
        i += 1
        while input[i] != "humidity-to-location map:":
            this_line = input[i].split(' ')
            t_h.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1
    if input[i] == "humidity-to-location map:":
        print(input[i])
        i += 1
        while i < len(input):
            this_line = input[i].split(' ')
            h_l.add((int(this_line[0]),int(this_line[1]),int(this_line[2])))
            i += 1   
    i += 1
print(s_s)
print(s_f)
print(f_w)
print(w_l)
print(l_t)
print(t_h)
print(h_l)
# Once we have all the sets filled, kinda run a DFS for each seed
# Save lowest

lowest = float('inf')

# Will return lowest location for seed
def dfs(seed):
    low = float('inf')
    soils = []
    m_soil = 0
    # Mapping Seeds to Soils
    for soil in s_s: # Just need s[2]. seed - s[0] needs to be < s[2]
        if (seed-soil[1]) < soil[2] and (seed-soil[1]) >= 0:
            # Figure out the mapping?
            m_soil = seed-soil[1]+soil[0]
    if not m_soil:
        m_soil = seed
    
    # Mapping Soil to fertilizer
    m_fert = 0
    for fert in s_f:
        if (m_soil-fert[1]) < fert[2] and (m_soil-fert[1]) >= 0:
            m_fert = m_soil-fert[1] + fert[0]
    if not m_fert:
        m_fert = m_soil
        
    # Mapping Fert to water
    m_water = 0
    for water in f_w:
        if (m_fert-water[1]) < water[2] and (m_fert-water[1]) >= 0:
            m_water = m_fert-water[1] + water[0]
    if not m_water:
        m_water = m_fert
        
    # Mapping WATER to LIGHT
    m_light = 0
    for water in w_l:
        if (m_water-water[1]) < water[2] and (m_water-water[1]) >= 0:
            m_light = m_water-water[1] + water[0]
    if not m_light:
        m_light = m_water
        
    # Mapping LIGHT to TEMP
    m_temp = 0
    for water in l_t:
        if (m_light-water[1]) < water[2] and (m_light-water[1]) >= 0:
            m_temp = m_light-water[1] + water[0]
    if not m_temp:
        m_temp = m_light
        
    # Mapping TEMP to HUMID
    m_humid = 0
    for water in t_h:
        if (m_temp-water[1]) < water[2] and (m_temp-water[1]) >= 0:
            m_humid = m_temp-water[1] + water[0]
    if not m_humid:
        m_humid = m_temp
        
    # Mapping HUMID to LOCATION
    m_loc = 0
    for water in h_l:
        if (m_humid-water[1]) < water[2] and (m_humid-water[1]) >= 0:
            m_loc = m_humid-water[1] + water[0]
    if not m_loc:
        m_loc = m_humid
    
    return m_loc
print(seeds)

for seed in seeds:
    lowest = min(dfs(seed),lowest)

print(lowest)