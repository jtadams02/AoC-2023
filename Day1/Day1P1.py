# Get out file
infile = open("input.txt",'r')

n = infile.readline()
s = 0
while n:
    curr_num = ''
    found_first = 0
    last_num = ''
    for char in n:
        if char.isnumeric():
            if not found_first:
                found_first = 1
                curr_num += char
                last_num = char
            else:
                # If the first num has been found
                last_num = char
                
            
    curr_num += last_num
    print(curr_num)
    s += int(curr_num)
    n = infile.readline()

print(s)
            