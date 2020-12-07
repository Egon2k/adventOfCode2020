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

def countBags(ruleDict, outerBag):
    sumBags = 1 # set to 1, otherwise recursion does not work
    
    # iterate over items in dict: https://stackoverflow.com/a/3294899
    for bag, numberOfBags in ruleDict[outerBag].items():
        sumBags += (countBags(ruleDict, bag)) * numberOfBags

    return sumBags

if __name__ == "__main__":
    data = []

    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    ruleDict = dict()


    for rule in data:
        ruleDict[getRuleName(rule)] = getBagDict(rule)

    # part 1
    part1 = 0
    for bag in ruleDict:
        part1 += isContainingBag(bag, ruleDict, 'shiny gold')

    # remove shiny gold bag itself
    print(f'Part 1: {part1 - 1}')

    # part 2
    part2 = countBags(ruleDict, 'shiny gold')

    # remove shiny gold bag itself
    print(f'Part 2: {part2 - 1}')


