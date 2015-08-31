import sys
import pickle
import copy
import operator
import os

def main(argv):
    if len(argv) != 2:
        print("Usage: python3 nbclassify.py MODELFILE TESTFILE")
        sys.exit()
    if not os.path.exists(argv[0]):
        print('File does not exist')
        sys.exit()
    if not os.path.isfile(argv[0]):
        print('Not a file')
    
    model_file = open(argv[0], 'rb')
    model = pickle.load(model_file)
    model_file.close()
    
    test_file = open(argv[1], 'r')
    
    class_value = copy.deepcopy(model['prior'])
    for line in test_file:
        list = line.split()
        for word in list:
            if word in model['features']:
                for key,  value in  model['features'][word].items():
                    class_value[key] = class_value[key] + value
        print(max(class_value.items(), key=operator.itemgetter(1))[0])
        class_value.clear()
        class_value = copy.deepcopy(model['prior'])

if __name__=="__main__":
    main(sys.argv[1:])
