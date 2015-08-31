import sys
import os
import re
import glob
import pickle
from collections import Counter
from collections import OrderedDict
features = OrderedDict()
def main(argv):
    output = open(argv[1], 'w')
    n_line = []
    i=0
    fcount = 0
    for file in sorted(glob.glob(os.path.join(argv[0], "*.txt"))):
         fcount = fcount + 1
         label = file.split('.')[0].split('/')[-1]
         if label == argv[2]:
            cls = 1
         else:
             cls = 0
         f = open(file, 'r', errors='ignore')
         for line in f:
            n_line.extend(re.split(' |\n|,|\.|\t', line))
         n_line = filter(None, n_line)
         count = Counter(n_line)
         for key,  value in count.items():
            if key not in features:
                features[key] = {}
                i = i + 1
                features[key]['feature_num'] = i
            features[key]['frequency'] = value
         output.write(str(cls) )
         for key,  value in features.items():
             if features[key]['frequency'] != 0:
                output.write(' '+str(features[key]['feature_num']))
                features[key]['frequency'] = 0
         output.write('\n')
         f.close()
         n_line = []
         if fcount %100 == 0:
            print('File: '+ str(fcount))
    features_file = open(argv[3], 'wb')
    pickle.dump(features, features_file)
    features_file.close()
if __name__ == "__main__":
    main(sys.argv[1:])
