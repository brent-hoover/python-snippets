"""
URL: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/302478
Title: Generating combinations of objects from multiple sequences
Submitter: David Klaffenbach
Last Updated: 2004/08/29
Version no: 1.0
Category: Algorithms 

Description:
The function combine takes multiple sequences and creates a list in
which each item is constructed from items from each input sequence,
and all possible combinations are created. If that description is
confusing, look at the example in the docstring. It's a pretty simple
transformation. The function xcombine is similar, but returns a generator
rather than creating the output all at once.

Discussion:
A trivial example would be to find the distribution of the rolls of two die:

range(1,7) nicely lists the possible values of a single roll.

>>> dist={}
>>> for roll in [sum(die_vals) for die_vals in combine(range(1,7),range(1,7))]:
... dist[roll]=dist.setdefault(roll,0)+1
...
>>> dist
{2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}

A more substantial usage would be in repeating a calculation or simulation
with input parameters varied over tolerance ranges:

>>> def Vdiv(Vin, Rupper, Rlower):
... '''returns output voltage of a voltage divider'''
... return Rlower/(Rupper+Rlower)*Vin
...
>>> Vin=[12*.95, 12*1.05] # 12V supply with +/- 5% tol
>>> Rlower=[5000*0.99,5000*1.01] # 5kohm resistor, +/- 1% tol
>>> Rupper=[7000*.99, 7000*1.01] # 7kohm resistor, +/- 1% tol
>>> data=[Vdiv(V,Ru,Rl) for V,Ru,Rl in combine(Vin,Rlower,Rupper)]
>>> data
[6.6499999999999995, 6.7053244592346086, 6.5944908180300494, 6.6499999999999995,
7.3500000000000014, 7.4111480865224637, 7.2886477462437407, 7.3500000000000014]
>>> min(data)
6.5944908180300494
>>> max(data)
7.4111480865224637

For problems which need to check over many combinations, this recipe
eliminates nested for loops (or list comprehensions with multiple
for's) and extends to many variables without changing the structure
of the code. Thanks to Python's *args tuple packing way of handling an
arbritrary number of arguments and the use of recursion, these functions
don't care how many sequences are handed to them. In the dice example,
combine makes a list with 36 items (six possible rolls of two dice). In
the circuit example, it makes a list of eight items (two choices each
in three variables).

I also wrote non-recursive versions but they were harder to understand
and slower. If this recipe is used with a very large number of input
lists, one would want to think about the recursion limit (see the sys
module), but I would expect most uses to involve a modest number of
input sequences.

The sequences (other than the first anyway) must allow repeated loops
through their values and must give the same values each time in order
for the output to be meaningful. If a simple generator is handed in,
it will only go through it's values once and you won't get it in full
combination with the other sequences. Other sequences related to files
or network sources may also not do the same thing every time. For these
type of sequences, wrapping it with list(...) will give combine a list
that it can loop over multiple times, creating proper results.
"""

def combine(*seqin):
    '''returns a list of all combinations of argument sequences.
for example: combine((1,2),(3,4)) returns
[[1, 3], [1, 4], [2, 3], [2, 4]]'''
    def rloop(seqin,listout,comb):
        '''recursive looping function'''
        if seqin:                       # any more sequences to process?
            for item in seqin[0]:
                newcomb=comb+[item]     # add next item to current comb
                # call rloop w/ rem seqs, newcomb
                rloop(seqin[1:],listout,newcomb)
        else:                           # processing last sequence
            listout.append(comb)        # comb finished, add to list
    listout=[]                      # listout initialization
    rloop(seqin,listout,[])         # start recursive process
    return listout

def xcombine(*seqin):
    '''returns a generator which returns combinations of argument sequences
for example xcombine((1,2),(3,4)) returns a generator; calling the next()
method on the generator will return [1,3], [1,4], [2,3], [2,4] and
StopIteration exception.  This will not create the whole list of 
combinations in memory at once.'''
    def rloop(seqin,comb):
        '''recursive looping function'''
        if seqin:                   # any more sequences to process?
            for item in seqin[0]:
                newcomb=comb+[item]     # add next item to current combination
                # call rloop w/ remaining seqs, newcomb
                for item in rloop(seqin[1:],newcomb):   
                    yield item          # seqs and newcomb
        else:                           # processing last sequence
            yield comb                  # comb finished, add to list
    return rloop(seqin,[])
