1.To create training file:
  python3 generate.py PATH_TO_TRAINING_FOLDER TRAININGFILE train
2.To create test file:
  python3 generate.py PATH_TO_TEST_FOLDER TESTFILE test
3.To create modelfile:
  python3 nblearn.py TRAININGFILE MODELFILE
4.To get test labels:
  python3 nbclassify.py MODELFILE TESTFILE
