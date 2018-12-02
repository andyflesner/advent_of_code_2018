freq = [0]
mods = []
duplicate = False
dupeint = 0
part1 = 0

input = open('input')
for line in input:
    mods.append(line.rstrip())
input.close()

while duplicate == False:
    for mod in mods:
        if mod[:1] == '+':
            newfreq = freq[-1] + int(mod[1:])
        elif mod[:1] == '-':
            newfreq = freq[-1] - int(mod[1:])
        else:
            print('ERROR')
            exit

        freq.append(newfreq)

        if freq.count(newfreq) > 1:
            duplicate = True
            dupeint = freq[-1]
            break

        if len(freq) == (len(mods) + 1):
            part1 = freq[-1]
    
print('Ending Frequency (Part 1): ' + str(part1))
print('First Duplicate Frequency (Part 2): ' + str(dupeint))