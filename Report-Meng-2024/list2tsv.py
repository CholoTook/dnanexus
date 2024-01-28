import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument("--input-file", "-i")

args = argparser.parse_args()

num_cols = 6

header = True
row = []

with open(args.input_file) as list_file:
    for line in list_file:
        row.append(line.strip())
        if len(row) < num_cols:
            continue

        print("\t".join(row))
        row = []
