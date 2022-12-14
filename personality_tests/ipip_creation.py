with open('ipip.txt') as f:
    lines = f.readlines()

# print(lines[0:5])
# ["Abuse people's confidences.\n", '\n', 'H1131\n', '\n', 'Accept apologies easily.\n']

# every other line is a new line
for line in lines[1::2]:
    assert '\n' == line, f'not new line: {line}'

lines = lines[0::2]

# even lines all end in new line
for line in lines:
    assert line[-1] == '\n', f'doesnt end in new line: {line}'

# remove new line
lines = [l[:-1] for l in lines]

# print(lines[0:5])
# ["Abuse people's confidences.", 'H1131', 'Accept apologies easily.', 'H133', 'Accept challenging tasks.']

# every other line is the letter-number code
lines = lines[0::2]

for line in lines:
    if line[-1] != '.':
        # if it ends in a quotation mark, they put the period inside. that's ok
        if line[-1] == '"':
            assert line[-2] == '.'
        else:
            # manually looked at those that fell here and they all need periods.
            print(line)
            line =  line + '.'

# print(lines[:5])
# print(lines[-5:])
# ["Abuse people's confidences.", 'Accept apologies easily.', 'Accept challenging tasks.', 'Accept little from others.', "Accept others' weaknesses."]
# ['Would rather spend money than save it.', "Wouldn't harm a fly.", 'Yell at inanimate objects.', 'Yell at others with little provocation.', 'Yell at people.']

# make the csv
with open('ipip_lines.txt', 'w+') as f:
    f.write('\n'.join(lines))

with open('ipip.csv', 'w+') as f:
    f.write('prompt,classes,answer_index,source_dataset,body,Q_id,front,binarized\n')
    # from the ipip website examples: https://ipip.ori.org/New_IPIP-50-item-scale.htm
    prompt = "For the following statement, choose whether it is 1. Very Inaccurate, 2. Moderately Inaccurate, 3. Neither Accurate Nor Inaccurate, 4. Moderately Accurate, or 5. Very Accurate as a description of you. Statement: "
    for i, line in enumerate(lines):
        # prompt,classes,answer_index,source_dataset,body,Q_id,front,binarized
        line = line.replace('"', '\'')
        f.write('"' + prompt + line + ' Choice:",' + "\"[' 1', ' 2', ' 3', ' 4', ' 5']\",0,ipip,0," + str(i) + ",0,0\n")
