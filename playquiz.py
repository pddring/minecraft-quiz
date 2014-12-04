import letters

l = letters.letters

text = raw_input("What would you like to display?")
x_offset = int(raw_input("x coordinate:"))
y_offset = int(raw_input("y coordinate:"))
z_offset = int(raw_input("z coordinate:"))
words = text.split(" ")

# discover width: length of longest word * 9

# discover height: number of words * 8
height = len(words) * 8

complete_string = []
for i in range(len(words)):
    word_string = ["","","","","","","",""]

    # i is word number
    word = words[i]

    first_time = True
    for letter in word:
        rows = l[letter.upper()].split('\n')[1:-1]
        for j in range(len(rows)):
            word_string[j] += rows[j]

    # add this word on to the end of the complete message
    complete_string += word_string
# display combined result
for j in range(len(complete_string)):
    complete_string[j] = complete_string[j].replace(".","")
    print complete_string[j]

output = open("message.csv", "w")
for y in range(len(complete_string)):
    row = complete_string[y]
    for x in range(len(row)):
        bit = row[x]
        if bit =="1":
            output.write(str(x_offset + x) + "," + str(y_offset - y)+ "," + str(z_offset) + "\n")
output.close()
"""
for letter in word:
    print l[letter.upper()]"""
