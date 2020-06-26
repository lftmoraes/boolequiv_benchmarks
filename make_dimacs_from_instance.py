
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise RuntimeError("No arguments given. USAGE: python make_dimacs_from_instance.py <instance_file>")

    instance_filepath = sys.argv[1]

    TT = list(map(lambda x: int(x), open(instance_filepath).read().strip()))

    for i, value in enumerate(TT):
        if value == 1:
            print("{} 0".format(i+1))
        else:
            print("-{} 0".format(i+1))
