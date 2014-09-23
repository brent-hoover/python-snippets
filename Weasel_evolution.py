#!/usr/bin/python
import string
import random
import sys
import copy
# Copyright(C) 2011 Iddo Friedberg
# Released under Biopython license. http://www.biopython.org/DIST/LICENSE
# Do not remove this comment

ALLCHARS = string.lowercase+' '+string.punctuation
def loopweasel(target_string,n_offspring,mut_rate):
    i = 1
    target_string = target_string.lower()
    current_string = list(''.join(random.choice(ALLCHARS)
                        for i in range(len(target_string))))
    print "    %s" % target_string
    while target_string != ''.join(current_string):
        print "%4d %s" % (i,''.join(current_string))
        i += 1
        offsprings = create_offspring(current_string,
                                    n_offspring,mut_rate)
        current_string = evolve_string(offsprings, target_string)
    print "%4d %s" % (i,''.join(current_string))

def create_offspring(current_string,n_offspring,mut_rate):
    offspring_list = []
    for i in (range(n_offspring)):
        offspring = []
        for c in current_string:
            if random.random() < mut_rate:
                offspring.append(random.choice(ALLCHARS))
            else:
                offspring.append(c)
        offspring_list.append(offspring)
    return offspring_list

def diffseq(a,b):
    diffcount = 0
    for i,j in zip(a,b):
        if i != j:
            diffcount += 1
    return diffcount

def evolve_string(offspring_list, target_string):
    best_match = (2000,'')
    for offspring in offspring_list:
        diffscore = diffseq(offspring, target_string)
        if diffscore < best_match[0]:
            best_match = (diffscore,offspring)
    return best_match[1]

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "Usage: weasel target_string n_offspring mutation_rate"
        print
        print "target_string: the string you would eventually evolve into"
        print "n_offspring: number of offspring per generation"
        print "mutation_rate rate of mutation per position, 0=< m <1"
        sys.exit(1)
    target_string = sys.argv[1]
    n_offspring = int(sys.argv[2])
    mut_rate = float(sys.argv[3])
    for i in target_string:
        if i not in ALLCHARS:
            print "Error, string can only contain %s" % ALLCHARS
            sys.exit(1)
    if mut_rate >= 1.0 or mut_rate < 0:
        print "Error: 0 =< mutation rate < 1"
        sys.exit(1)
    loopweasel(target_string,n_offspring, mut_rate)
