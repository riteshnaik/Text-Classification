import sys
import pickle
import copy
import os
import math

def main(argv):
    if len(argv) != 2:
        print("Usage: python3 nblearn.py TRAININGFILE MODELFILE")
        sys.exit()
    if not os.path.exists(argv[0]):
        print('File does not exist')
        sys.exit()
    if not os.path.isfile(argv[0]):
        print('Not a file')
        
    input = open(argv[0], 'r')
    
    word_list = {}
    class_list = {}
    class_size = {}
    prior_prob = {}
    feat_prob = {}
    model = {}
    N = 0
    
    for line in input:
        list = line.split()
        if list[0] not in class_list:
            class_list[list[0]] = 0
        if list[0] not in class_size:
            class_size[list[0]] = len(list[1:])
        else:
            class_size[list[0]] += len(list[1:])
        for word in list[1:]:
            if word not in word_list:
               word_list[word] = {} 
            if list[0] not in word_list[word]:
                word_list[word][list[0]] = 1
            else:
                word_list[word][list[0]] += 1
        class_list[list[0]] += 1
        N += 1
    input.close()
    for key, value in class_list.items():
        prior_prob[key] = math.log(value/N)
    
    
    #f_myfile = open('myfile.pickle', 'rb')
    #favorite_color = pickle.load(f_myfile)  # variables come out in the order you put them in
    #f_myfile.close()
    
    feat_prob = copy.deepcopy(word_list)
    test = open('test.txt', 'w')
    for key, value in feat_prob.items():
        for cls, dummy in class_list.items():
            if cls in value:
                 feat_prob[key] [cls]  =  math.log((feat_prob[key] [cls]  + 1 )/(class_size[cls] + len(feat_prob)))
            else:
                 feat_prob[key] [cls]  =  math.log((1 )/(class_size[cls] + len(feat_prob)))
            test.write(key+' '+str(feat_prob[key] [cls])+'\n')
    model['class'] = class_list
    model['prior'] = prior_prob
    model['features'] = feat_prob
    
    output = open(argv[1], 'wb')
    pickle.dump(model, output)
    output.close()
    
    #print('Number of Words in HAM: {}'.format(class_size['HAM']))
    #print('Number of Words in SPAM: {}'.format(class_size['SPAM']))
    #print('Vocabulary SIZE: {}'.format(len(feat_prob)))
if __name__ =="__main__":
    main(sys.argv[1:])
