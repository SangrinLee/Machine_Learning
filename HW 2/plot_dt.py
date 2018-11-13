# -*- coding: utf-8 -*-
import ID3, parse, random, node, math
import matplotlib.pyplot as plt



# inFile - string location of the house data file
def testPruningOnHouseData(train_size,prune_train_perct,inFile):
  withPruning = []
  withoutPruning = []
  data = parse.parse(inFile)
  
  train_set_size_prune=int(train_size*prune_train_perct)

  
  for i in range(100):
    print "Running with Training size: "+str(train_size) + " Trial: "+str(i)
    random.shuffle(data)
     
    train = data[:train_set_size_prune]
    valid = data[train_set_size_prune:train_size]
    test  = data[train_size:]
  
    tree = ID3.ID3(train, 'democrat')
    ID3.prune(tree, valid)
    acc = ID3.test(tree, test)
    withPruning.append(acc)
    
    
    tree = ID3.ID3(train+valid, 'democrat')
    acc = ID3.test(tree, test)
    withoutPruning.append(acc)
    
    
  avg_withPruning     =       sum(withPruning)/len(withPruning)
  avg_withoutPruning  =       sum(withoutPruning)/len(withoutPruning)
  
  return dict(withPruning=avg_withPruning,withoutPruning=avg_withoutPruning)
  




with_pruning       =[]
without_pruning    =[]
num_examples       =[]

for train_size in xrange(10,310,10):
    
          
    prune_train_perct=0.7
    inFile=".\house_votes_84.data"
    
    dtAcc=testPruningOnHouseData(train_size,prune_train_perct,inFile)
    num_examples.append(train_size)
    with_pruning.append(dtAcc["withPruning"])
    without_pruning.append(dtAcc["withoutPruning"])




plt.title('Training curve with and without pruning')
plt.plot(num_examples, without_pruning, label="without pruning")
plt.xlabel('Number of training examples')
plt.plot(num_examples, with_pruning, label="with pruning")
plt.ylabel('Accuracy on testing set')
plt.legend()
plt.show()

