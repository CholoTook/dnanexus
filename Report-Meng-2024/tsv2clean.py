import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument("--input-file", "-i", default="data-pen.tsv")

args = argparser.parse_args()

header = True

with open(args.input_file) as input_file:
    for line in input_file:
        if header:
            header = False
            continue

        cols = line.strip("\n").split("\t")
        cols.append("")
        cols[3], cols[6] = cols[3].split(" ")
        cols[5] = cols[5].replace(" x 10", "e")

        print("\t".join(cols))
