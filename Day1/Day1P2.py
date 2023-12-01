# Get input file
infile = open("input.txt",'r')

n = infile.readline()
s = 0
# Create dict to map strings to numbers
# Should I use a prefix tree?

numbers = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
max_len = 5 # Longest length a number can be, therefore  our window cannot be larger

while n:
    # Lets try to find the first number
    curr_sum = ''
    first_index = 0 
    while first_index < len(n) and not n[first_index].isnumeric():
        first_index += 1
    
    # Now we have the first index of a number, now lets slowly build from the start to first_index
    # And try every possible way to make a word
    left = 0
    did_find = 0
    while left < first_index:
        right = left
        while right < first_index and (right-left)<=4:
            splice = n[left:right+1]
            if splice in numbers:
                did_find = 1
                curr_sum += numbers[splice]
                break
            right += 1
        if did_find:
            break
        left += 1
    if not did_find:
        curr_sum += n[first_index]
    
    # Now we do a similar thing but from the back
    last_num = len(n)-1
    while last_num > 0 and not n[last_num].isnumeric():
        last_num -= 1
    
    left = len(n)-1
    did_find = 0
    while left > last_num:
        start = left
        while start < len(n):
            splice = n[left:start+1]
            if splice in numbers:
                curr_sum += numbers[splice]
                did_find = 1
                break
            start += 1
        if did_find:
            break
        left -= 1
    if not did_find:
        curr_sum += n[last_num]
    print(curr_sum)
    s += int(curr_sum)
    n = infile.readline()
print("Output below")
print(s)
            
