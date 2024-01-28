import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument("--input-file", "-i", default="data-depression.clean.tsv")

args = argparser.parse_args()

score = 0

with open(args.input_file) as input_file:
    for line in input_file:
        cols = line.strip("\n").split("\t")

        rsid, effect_allele = cols[0].split("_", 1)
        alleles = cols[1].split(" / ", 1)
        count = alleles.count(effect_allele)
        effect = float(cols[3])
        score += count * effect

print(score)
