import glob
import sys
import os
import re

def main(argv):
    output = open(argv[1], 'w')
    n_line = []
    for file in sorted(glob.glob(os.path.join(argv[0], "*.txt"))):
             label = file.split('.')[0].split('/')[-1]
             f = open(file, 'r', errors='ignore')
             for line in f:
                 n_line.extend(re.split(' |\n|,|\.', line))
             w_line = " ".join(n_line)
             w_line = re.sub( '\s+', ' ', w_line , )
             if argv[2] == "train":
                output.write(label + " " + w_line)
             elif argv[2] == "test":
                output.write(w_line)
             output.write('\n')
             f.close()
             n_line = []
             w_line = ""

if __name__ =="__main__":
    main(sys.argv[1:])
