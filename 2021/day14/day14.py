
#imports the some tools it'll need
from collections import Counter
import operator
import copy

#opens input as stings in a list
with open ("puzzle14") as file:
    puzzle=[line.strip() for line in file]
#extracts the "polymer" to a new list, for ease of workflow
pol = puzzle[0]
#organises input into a dictionary
del puzzle[0], puzzle[0]
puzzle = [i.split(' -> ') for i in puzzle]
check = puzzle.copy()
puzzle = dict(puzzle)

#Counts the number of times each letter appear, by generating the polymer in full
def growz (polymer, rules, output, generation, genT):
    generation += 1
    counter = 0
    for i in range(0, len(polymer), 2):
        if polymer[i:i+2] in rules.keys():
            counter+=1
            polymerB = output[:counter] + rules[polymer[i:i+2]] + output[counter:]
            counter+=1
            output = polymerB
        if polymer[i+1:i+3] in rules.keys():
            counter+=1
            polymerB = output[:counter] + rules[polymer[i+1:i+3]] + output[counter:]
            counter+=1
            output = polymerB
    if generation == genT:
        return output
    return growz (output, rules, output, generation, genT)

ocurrances = Counter(growz (pol, puzzle, pol, 0, 10))

#substracts ocurrances of the letter that appears the least, 
#from the one that appears the most
print('Part 1 soution:' ,
       ocurrances[max(ocurrances.items(), key=operator.itemgetter(1))[0]] 
      - ocurrances[min(ocurrances.items(), key=operator.itemgetter(1))[0]])

###     PART 2


#creates a dict with all the different letters from input as keys and with value 0
def letterCounter (dictionary):
    lettercount = {}
    for p in dictionary:
        lettercount[dictionary[p]] = 0
    return lettercount

#Driver code
lettercount = letterCounter(puzzle)

#Adds 2 to the counter of the last letter in original polymer 
# (for the test only one is added???)
lettercount[pol[-1]] += 2

#creates dict to count pairs. Key = each pair :  Value = 0
def pairCounter (pairdictionary):
    paircount= copy.deepcopy(pairdictionary)
    for i in paircount:
        paircount[i]= 0
    return paircount

#Driver code
paircount= pairCounter(puzzle)

#Creates a copy of the pair counter (neccesary to have access to an empty copy)
emptyPaircounter = copy.deepcopy(paircount)

#fills the initial paircount from initial polymer
def pairCounterInput (polymer, paircounter):
    for i in range(0, len(polymer), 2):
            if polymer[i:i+2] in paircounter.keys():
                paircounter[polymer[i:i+2]]+=1
            if polymer[i+1:i+3] in paircounter.keys():
                paircounter[pol[i+1:i+3]]+=1

#Driver code
pairCounterInput (pol, paircount)

#creates dict with the 2 pairs created by each new letter that's added to the polymer
def paircountDatabase (dictionary):
    modified= puzzle.copy()
    for key, value in check:
        modified[key]= [key[0]+value , value + key[1]]
    return modified

#Driver code
pairDatabase = paircountDatabase (puzzle)

#function to count the num of pairs generated in each iteration
#it also counts the number of new letters created each generation
def counter(generations, current, dictPaircounter, emptyCounter):
    
    paircounted = copy.deepcopy(dictPaircounter)
    toBeFilled= copy.deepcopy(emptyCounter)
    
    for g in dictPaircounter:
        tt = pairDatabase[g][0]
        ttt= pairDatabase[g][1]
        toBeFilled[tt]+= paircounted[g]
        toBeFilled[ttt]+= paircounted[g]
        lettercount[puzzle[g]] += paircounted[g]

    if current == generations:
        return True
    return counter(generations, current+1, copy.deepcopy(toBeFilled) , emptyPaircounter )

#Driver code
counter(39, 0, paircount, emptyPaircounter)

#substracts ocurrances of the letter that appears the least, 
#from the one that appears the most
print('Part 2 soution:' ,
       lettercount[max(lettercount.items(), key=operator.itemgetter(1))[0]] 
      - lettercount[min(lettercount.items(), key=operator.itemgetter(1))[0]])
