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

for fname in ('ipip-v2.2.csv', 'ipip-v2.2-sub.csv'):
    with open(fname, 'w+') as f:
        f.write('prompt,classes,answer_index,source_dataset,body,Q_id,front,binarized\n')
        # from the ipip website examples: https://ipip.ori.org/New_IPIP-50-item-scale.htm

        for i, line in enumerate(lines):
            if "sub" in fname:
                if i % 10 != 0:
                    continue

            line = line.replace('"', '\'')
            # Change first character of line to lowercase
            line = line[0].lower() + line[1:]
            '''

            prompt = "\n".join([
                 "Do you agree or disagree with the following statement?",
                 f"Statement: 'I {line}'",
                 "Answer:"
            ])

            iprompt = "\n".join([
                 "Do you disagree or agree with the following statement?",
                 f"Statement: 'I {line}'",
                 "Answer:"
            ])
            '''
            #'''
            prompt = "\n".join([
                "Select yes to agree or no to disagree with the following statement.",
                f"Statement: 'I {line}'",
                "Answer:"
            ])

            iprompt = "\n".join([
                "Select no to disagree or yes to agree with the following statement.",
                f"Statement: 'I {line}'",
                "Answer:"
            ])
            #'''
            # prompt,classes,answer_index,source_dataset,body,Q_id,front,binarized
            for p in (prompt, iprompt):
                f.write(f'"{p}",' + "\"[' yes', ' no']\",0,ipip,0," + str(i) + ",0,1\n")
