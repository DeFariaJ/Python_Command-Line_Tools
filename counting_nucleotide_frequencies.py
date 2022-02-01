#!/usr/bin/env python3
"""
Author : goncaloleiria <goncaloleiria@localhost>
Date   : 2022-01-30
Purpose: This programs counts nucleotide frequencies from files or direct command-line input"
Aim: Exercise 1 from "Mastering Python for Bioinformatics
"""

import argparse
from typing import NamedTuple, TextIO
import os 


class Args(NamedTuple): #define class for the arguments
    """ Get command-line arguments """
    dna: str # this class has a single field called dna which
    #has a type string
 
# --------------------------------------------------   
# --------------------------------------------------

# THIS IS ARGPARSE CODE (get_args function handles the argparse code)

def get_args() -> Args: # funtion returns object of type args
    """ Get command-line arguments """

    #parser object is used to define the program's parameters
    parser = argparse.ArgumentParser(
        description='Counting nucleotides from files or direct command-line input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', #dna argument
                        metavar='DNA', # short description
                        help='input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna) #return new Args object that contains the
    #single value from args.dna

# --------------------------------------------------
#THIS IS THE PROGRAM ITSELF #all programs start with main()
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    count_A, count_T, count_C, count_G = 0,0,0,0

    for base in args.dna:

        if base == "A":
            count_A = count_A + 1

        elif base == "T":
            count_T = count_T + 1

        elif base == "C":
            count_C = count_C + 1

        elif base == "G":
            count_G = count_G + 1


    print("A=" + str(count_A),"T="+ str(count_T),"C="+ str(count_C),"G=" + str(count_G))


# --------------------------------------------------
if __name__ == '__main__':
    main()
