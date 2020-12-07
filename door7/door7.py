data = []

def getBagDict(rule):
    bags = dict()
    words = rule.split()

    for i in range(len(words)):
        # >= 4 because first 4 words are the bag itself
        # %4 because one rule contains of 4 words "<number> <color1> <color2> bags"
        if i >= 4 and (i % 4) == 0:
            try:
                # if bag contains "no other bags" is tried to convert
                # to integer, exception is thrown
                bags[f'{words[i+1]} {words[i+2]}'] = int(words[i])
            except:
                break

    return bags

def getRuleName(rule):
    words = rule.split()
    return f'{words[0]} {words[1]}'


def isContainingBag(outerBag, ruleDict, breakCritereon):
    retVal = False

    for bag in ruleDict[outerBag]:
        # stop when break critereon is reached
        if outerBag == breakCritereon:
            retVal = True
        # or if bag is contained
        elif isContainingBag(bag, ruleDict, breakCritereon):
            retVal = True

    return retVal

if __name__ == "__main__":
    with open('data_test.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    ruleDict = dict()

    # part 1
    for rule in data:
        ruleDict[getRuleName(rule)] = getBagDict(rule)

    part1 = 0
    for bag in ruleDict:
        part1 += isContainingBag(bag, ruleDict, 'shiny gold')

    # remove shiny gold bag itself
    part1 -= 1

    print(f'Part 1: {part1}')
