import sys
import glob
import os
import re
import pickle
from collections import Counter
def main(argv):
    features_file = open(argv[2], 'rb')
    features = pickle.load(features_file)
    features_file.close()
    output = open(argv[1], 'w')
    for file in sorted(glob.glob(os.path.join(argv[0], "*.txt"))):
        f = open(file, 'r', errors='ignore')
        n_line = []
        for line in f:
            n_line.extend(re.split(' |\n|,|\.|\t', line))
        n_line = filter(None, n_line)
        count = Counter(n_line)
        for key,  value in count.items():
            if key in features:
                 features[key]['frequency'] = value
        output.write(str(1) )
        for key,  value in features.items():
             if features[key]['frequency'] != 0:
                output.write(' '+str(features[key]['feature_num']))
                features[key]['frequency'] = 0
        output.write('\n')
        f.close()
        n_line = []
if __name__ == "__main__":
    main(sys.argv[1:])
