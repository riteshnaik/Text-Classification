import sys
def main(argv):
    svmoutput = open(argv[0], 'r')
    svmlabels = open(argv[1], 'w')
    for line in svmoutput:
        if float(line.strip()) < 0:
            svmlabels.write(argv[2]+"\n")
        else:
            svmlabels.write(argv[3]+"\n")
if __name__ == "__main__":
    main(sys.argv[1:])
