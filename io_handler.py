import numpy as np


def get_gene_sequence(filename):
    print("Reading from " + filename)
    file = open(filename, "r")
    gene = file.read().strip()

    out = []

    for char in gene:
        if char == "a":
            out.append(0)
        elif char == "c":
            out.append(1)
        elif char == "g":
            out.append(2)
        else:
            out.append(3)

    return np.array(out)

def get_observations (filename):
    print("Reading from " + filename)
    file = open(filename, "r")
    gene = file.read().strip()

    out = []

    for char in gene:
        out.append(char)

    return np.array(out)


def save_cpg_islands(filename, text):
    file = open(filename, "w")
    file.write(text)
    print("Output saved to " + filename)
    file.close()
