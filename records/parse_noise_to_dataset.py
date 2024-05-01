import numpy as np
import sys, os
import itertools
import argparse
parser = argparse.ArgumentParser(description='save torch experience file to npy.')
parser.add_argument('-s', help='source torch experience file directory.', required=True)
parser.add_argument('-y', help='Yes to all', default=False, action='store_true')
args = parser.parse_args()


TP = -10
DIS = [5, 10, 15]
SR = [5, 20]
INTER = [0, 1]
CF = 2360

def get_filename(prefix, comb):
    return f"Non_process_{prefix}_RAND_TP{TP}_D{comb[0]}_SR{comb[1]}_CF{CF}_I{comb[2]}.dat"


def get_noise_files_from_source():

    prefix = args.s.split("/")[1]
    print(f"{prefix = }")

    combinations = itertools.product(DIS, SR, INTER)

    for comb in combinations:
        print(list(comb))
        filename = get_filename(prefix, comb)
        full_filename = f"{args.s}{filename}"


        print("-"*50)
        print(f"Checking {full_filename}...")
        if os.path.exists(full_filename):
            print("Success")
            pass
        else:
            print(f"{full_filename} is not exist.")

    pass

def main():

    if not os.path.isdir(args.s):
        print(f"{args.s} is not a directory.\nAbort.")
        exit()

    noise_files = get_noise_files_from_source()


if __name__ == "__main__":
    main()
