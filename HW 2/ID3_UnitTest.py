# -*- coding: utf-8 -*-
import ID3
import parse
import operator
import node
import copy
#Test randomPickOne
print ID3.randomPickOne(["a","b","c"])

#Test trivial data
dataSetTVD1=   [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'a'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'm', 'Class': 'b'},
              {'h': 'o', 'Class': 'b'}, {'h': 'k', 'Class': 'b'},
              ]

dataSetTVD2=   [{'h': 'n', 'Class': 'a'}, {'h': 'n', 'Class': 'a'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'n', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'n', 'Class': 'b'},
              {'h': 'n', 'Class': 'b'}, {'h': 'n', 'Class': 'b'},
              ]


dataSetTVD3=   [{'h': 'n', 'Class': 'a'}
              ]
dataSetTVD4=   [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'}
              ]


print "Expect False, Actual "+str(ID3.hasTrivialSplit(dataSetTVD1))
print "Expect True, Actual "+str(ID3.hasTrivialSplit(dataSetTVD2))
print "Expect True, Actual "+str(ID3.hasTrivialSplit(dataSetTVD3))
print "Expect False, Actual "+str(ID3.hasTrivialSplit(dataSetTVD4))

#Test getModeOut
dataSet1=    [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'a'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'b'}, {'h': 'm', 'Class': 'b'},
              {'h': 'o', 'Class': 'b'}, {'h': 'k', 'Class': 'b'},
              ]

dataSet2=    [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'a'}, 
              {'h': 'n', 'Class': 'b'}
              ]

dataSet3=    [{'h': 'n', 'Class': 'a'}
              ]

dataSet4=    [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'},
              {'h': 'o', 'Class': 'a'}, {'h': 'k', 'Class': 'b'},
              ]

dataSet5=    [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'd'}, 
              {'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'c'},
              {'h': 'o', 'Class': 'a'}, {'h': 'k', 'Class': 'b'},
              ]
dataSet6=    [{'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'b'}, 
              {'h': 'n', 'Class': 'a'}, {'h': 'm', 'Class': 'c'}, 
              {'h': 'n', 'Class': 'd'}, {'h': 'm', 'Class': 'c'},
              {'h': 'o', 'Class': 'd'}, {'h': 'k', 'Class': 'b'},
              ]

print "Expect b, Actual "+ ID3.getModeOutput(dataSet1)
print "Expect a, Actual "+ ID3.getModeOutput(dataSet2)
print "Expect a, Actual "+ ID3.getModeOutput(dataSet3)
print "Expect a or b, Actual "+ ID3.getModeOutput(dataSet4)
print "Expect a, Actual "+ ID3.getModeOutput(dataSet5)
print "Expect a or b or c, Actual "+ ID3.getModeOutput(dataSet6)

#For get all attributes
dataAllAttr1=   [{'f1': 'n','f2': '1', 'Class': 'a'}, {'f1': 'm','f2': '1', 'Class': 'b'}, 
               {'f1': 'n','f2': '1', 'Class': 'a'}, {'f1': 'm', 'f2': '1','Class': 'b'}, 
               {'f1': 'n', 'f2': '1','Class': 'a'}, {'f1': 'm', 'f2': '1','Class': 'b'},
               {'f1': 'm','f2': '1', 'Class': 'b'}, {'f1': 'm', 'f2': '1','Class': 'b'}      
               ]
dataAllAttr2=   [{'f1': 'n', 'Class': 'a'} 
               ]
dataAllAttr3=   [{'f1': 'n','f2': '1', 'f3': '1','Class': 'a'}, {'f1': 'm','f2': '1', 'Class': 'b'}]

listAllAttr4=[]
aSampleData={}
for i in range(0,100):
    attribute="f"+str(i)
    aSampleData[attribute]=1
    listAllAttr4.append(attribute)
aSampleData["Class"]=1

dataAllAttr4=[aSampleData]

                
print "Expect ['f1','f2'], Actual "
print ID3.getAllAttributes(dataAllAttr1)

print "Expect ['f1'], Actual "
print ID3.getAllAttributes(dataAllAttr2)

print "Expect ['f1','f2','f3'], Actual "
print ID3.getAllAttributes(dataAllAttr3)

print "Expect length"
print len(listAllAttr4)
print " Actual length"
print len(ID3.getAllAttributes(dataAllAttr4))



#For split data

splitDataSet1=[{'f1': 'n','f2': '1', 'Class': 'a'}
               ]
splitDataSet2=[{'f1': 'n','f2': '1', 'Class': 'a'},
               {'f1': 'm','f2': '1', 'Class': 'a'}
               ]

splitDataSet3=[{'f1': 'n','f2': '1', 'Class': 'a'},
               {'f1': 'n','f2': '1', 'Class': 'b'},
               {'f1': 'm','f2': '1', 'Class': 'a'}
               ]

splitDataSet4=[{'f1': 'n','f2': '1', 'Class': 'a'},               
               {'f1': 'm','f2': '1', 'Class': 'a'},
               {'f1': 'n','f2': '1', 'Class': 'b'}
               ]

splitDataSet5=[{'f1': 'm','f2': '1', 'Class': 'a'}, 
               {'f1': 'n','f2': '1', 'Class': 'a'},
               {'f1': 'n','f2': '1', 'Class': 'b'}             
               ]

splitDataSet6=[{'f1': 'n','f2': '1', 'Class': 'a'},
               {'f1': 'n','f2': '2', 'Class': 'b'},
               {'f1': 'm','f2': '1', 'Class': 'a'}
               ]


print "Expect [{'f1': 'n','f2': '1', 'Class': 'a'}]" + " actual:"
print  ID3.getSplitData(splitDataSet1,'f1')

print "Expect [{'f1': 'n','f2': '1', 'Class': 'a'}]" + " actual:"
print  ID3.getSplitData(splitDataSet1,'f2')

print "Expect "
print splitDataSet2
print "[{'f1': 'n','f2': '1', 'Class': 'a'}]" + " actual:"
print  ID3.getSplitData(splitDataSet2,'f2')

print "Expect "
print splitDataSet2[0]
print splitDataSet2[1]

print "[{'f1': 'n','f2': '1', 'Class': 'a'}]" + " actual:"
print  ID3.getSplitData(splitDataSet2,'f1')



print  "Should f1: 1 m,  2n actual:"
print  ID3.getSplitData(splitDataSet3,'f1')
print  "Should f1: 1 m,  2n actual:"
print  ID3.getSplitData(splitDataSet4,'f1')
print  "Should f1: 1 m,  2n actual:"
print  ID3.getSplitData(splitDataSet5,'f1')


print  " actual:"
print  ID3.getSplitData(splitDataSet3,'f2')
print  " actual:"
print  ID3.getSplitData(splitDataSet4,'f2')
print  " actual:"
print  ID3.getSplitData(splitDataSet5,'f2')

print  "Should f2: one 2,  two 1 actual:"
print  ID3.getSplitData(splitDataSet6,'f2')





#For entropy
entropyDataSet1=[{'f1': 'n','f2': '1', 'Class': 'a'}
               ]

entropyDataSet2=[{'f1': 'n','f2': '1', 'Class': 'a'},
                 {'f1': 'n','f2': '1', 'Class': 'b'}
               ]

entropyDataSet3=[{'f1': 'n','f2': '1', 'Class': 'a'},
                 {'f1': 'm','f2': '1', 'Class': 'b'}
               ]

entropyDataSet4=[{'f1': 'n','f2': '1', 'Class': 'a'},
                 {'f1': 'n','f2': '2', 'Class': 'b'}
               ]

entropyDataSet5=[{'f1': 'n','f2': '1', 'Class': 'a'},
                 {'f1': 'n','f2': '2', 'Class': 'b'},
                 {'f1': 'n','f2': '2', 'Class': 'c'}
               ]


entropyDataSet6=[{'f1': '1','f2': 'n', 'Class': 'a'},
                 {'f1': 'n','f2': 'n', 'Class': 'b'},
                 {'f1': 'n','f2': 'n', 'Class': 'c'}
               ]

entropyDataSet7=[{'f1': 'a','f2': 'n', 'Class': 'x'},
                 {'f1': 'a','f2': 'n', 'Class': 'x'},
                 
                 {'f1': 'b','f2': 'n', 'Class': 'y'},
                 {'f1': 'b','f2': 'n', 'Class': 'y'},
                 
                 {'f1': 'c','f2': 'n', 'Class': 'x'},
                 {'f1': 'c','f2': 'n', 'Class': 'x'},
                 {'f1': 'c','f2': 'n', 'Class': 'y'},
                 {'f1': 'c','f2': 'n', 'Class': 'y'},
                 {'f1': 'c','f2': 'n', 'Class': 'y'},
                 {'f1': 'c','f2': 'n', 'Class': 'y'},
                 {'f1': 'c','f2': 'n', 'Class': 'z'},
                 {'f1': 'c','f2': 'n', 'Class': 'z'},
                 
                 {'f1': 'd','f2': 'n', 'Class': 'x'},
                 {'f1': 'd','f2': 'n', 'Class': 'x'},
                 {'f1': 'd','f2': 'n', 'Class': 'y'},
                 {'f1': 'd','f2': 'n', 'Class': 'y'},
                 {'f1': 'd','f2': 'n', 'Class': 'y'},
                 {'f1': 'd','f2': 'n', 'Class': 'y'},
   
                 {'f1': 'e','f2': 'n', 'Class': 'x'},
                 {'f1': 'e','f2': 'n', 'Class': 'x'},              
                 {'f1': 'e','f2': 'n', 'Class': 'x'},
                 {'f1': 'e','f2': 'n', 'Class': 'x'},
                 {'f1': 'e','f2': 'n', 'Class': 'y'},
                 {'f1': 'e','f2': 'n', 'Class': 'y'},   
                 
                 {'f1': 'f','f2': 'n', 'Class': 'x'},
                 {'f1': 'f','f2': 'n', 'Class': 'x'},
                 {'f1': 'f','f2': 'n', 'Class': 'y'},
                 {'f1': 'f','f2': 'n', 'Class': 'y'},
                 {'f1': 'f','f2': 'n', 'Class': 'z'},
                 {'f1': 'f','f2': 'n', 'Class': 'z'},
                 
                 {'f1': 'g','f2': 'n', 'Class': 'z'},
                 {'f1': 'g','f2': 'n', 'Class': 'z'},
                 {'f1': 'g','f2': 'n', 'Class': 'z'}                 
                ]


entropyDataSet8=[{'f1': 'n','f2': '1', 'f3':'1', 'Class': 'a'},
                 {'f1': 'n','f2': '2', 'f3':'1', 'Class': 'b'},
                 {'f1': 'n','f2': '2', 'f3':'1', 'Class': 'c'}
                ]

entropyDataSet9=[{'f1': 'n','f2': '1', 'f3':'1','f4':'1', 'Class': 'a'},
                 {'f1': 'n','f2': '2', 'f3':'1','f4':'2', 'Class': 'b'},
                 {'f1': 'n','f2': '2', 'f3':'1','f4':'2', 'Class': 'c'}
                ]
entropyDataSet10=[{'f1': 'n','f2': '1', 'f3':'1','f4':'1', 'f5':'1','Class': 'a'},
                 {'f1': 'n','f2': '2', 'f3':'1','f4':'2', 'f5':'2', 'Class': 'b'},
                 {'f1': 'n','f2': '2', 'f3':'1','f4':'2', 'f5':'2','Class': 'c'}
                ]

print ""
print "Entropy example 1"
print ""
print "Expect 0, actual "
print ID3.getEntropy(entropyDataSet1,'f1')
print ID3.getEntropy(entropyDataSet1,'f2')

print "Expect 0, actual "
print ID3.getEntropy(entropyDataSet1,'f2')
print ""

print "Entropy example 2"
print ""
print "Splited Data"
print  ID3.getSplitData(entropyDataSet2,'f2')
print "Feature 2, Expect 1, actual "
print ID3.getEntropy(entropyDataSet2,'f2')
print "Feature 1, Expect 1, actual "
print ID3.getEntropy(entropyDataSet2,'f1')
print ""

print "Entropy example 3"
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet3,'f2')
print "Feature 2, Expect 1, actual "
print ID3.getEntropy(entropyDataSet3,'f2')

print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet3,'f1')
print "Feature 1, Expect 0, actual "
print ID3.getEntropy(entropyDataSet3,'f1')
print ""

print "Entropy example 4"
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet4,'f2')
print "Feature 2, Expect 0, actual "
print ID3.getEntropy(entropyDataSet4,'f2')

print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet4,'f1')
print "Feature 1, Expect 1, actual "
print ID3.getEntropy(entropyDataSet4,'f1')


print ""
print "Entropy example 5"
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet5,'f2')
print "Feature 2, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet5,'f2')

print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet5,'f1')
print "Feature 1, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet5,'f1')

print ""
print "Entropy example 6"
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet6,'f2')
print "Feature 2, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet6,'f2')

print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet6,'f1')
print "Feature 1, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet6,'f1')



print ""
print "Entropy example 7"
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet7,'f2')
print "Feature 2, Expect 1.53, actual "
print ID3.getEntropy(entropyDataSet7,'f2')

print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet7,'f1')
print "Feature 1, Expect 0.98, actual "
print ID3.getEntropy(entropyDataSet7,'f1')


print ""
print ""
print "Entropy example 8"
print ""
print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet8,'f1')
print "Feature 1, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet8,'f1')
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet8,'f2')
print "Feature 2, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet8,'f2')
print ""
print "Splited Data by Feature 3"
print  ID3.getSplitData(entropyDataSet8,'f3')
print "Feature 3, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet8,'f3')

print ""
print ""
print "Entropy example 9"
print ""
print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet9,'f1')
print "Feature 1, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet9,'f1')
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet9,'f2')
print "Feature 2, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet9,'f2')
print ""
print "Splited Data by Feature 3"
print  ID3.getSplitData(entropyDataSet9,'f3')
print "Feature 3, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet9,'f3')
print ""
print "Splited Data by Feature 4"
print  ID3.getSplitData(entropyDataSet9,'f4')
print "Feature 4, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet9,'f4')


print ""
print ""
print "Entropy example 10"
print ""
print "Splited Data by Feature 1"
print  ID3.getSplitData(entropyDataSet10,'f1')
print "Feature 1, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet10,'f1')
print ""
print "Splited Data by Feature 2"
print  ID3.getSplitData(entropyDataSet10,'f2')
print "Feature 2, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet10,'f2')
print ""
print "Splited Data by Feature 3"
print  ID3.getSplitData(entropyDataSet10,'f3')
print "Feature 3, Expect 1.585, actual "
print ID3.getEntropy(entropyDataSet10,'f3')
print ""
print "Splited Data by Feature 4"
print  ID3.getSplitData(entropyDataSet10,'f4')
print "Feature 4, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet10,'f4')
print ""
print "Splited Data by Feature 5"
print  ID3.getSplitData(entropyDataSet10,'f5')
print "Feature 5, Expect 0.67, actual "
print ID3.getEntropy(entropyDataSet10,'f5')
#==============================================================================
# 
#==============================================================================


#For getMinEntropyAttribute
print ""
print "Entropy example 1"
print ""
print "Expect f1 or f2, actual "
print ID3.getMinEntropyAttribute(entropyDataSet1)


print ""
print "Entropy example 2"
print ""
print "Expect f1 or f2, actual "
print ID3.getMinEntropyAttribute(entropyDataSet2)


print ""
print "Entropy example 3"
print ""
print "Expect f1, actual "
print ID3.getMinEntropyAttribute(entropyDataSet3)


print ""
print "Entropy example 4"
print ""
print "Expect f2, actual "
print ID3.getMinEntropyAttribute(entropyDataSet4)




print ""
print "Entropy example 5"
print ""
print "Expect f2, actual "
print ID3.getMinEntropyAttribute(entropyDataSet5)


print ""
print "Entropy example 6"
print ""
print "Expect f1, actual "
print ID3.getMinEntropyAttribute(entropyDataSet6)



print ""
print "Entropy example 7"
print ""
print "Expect f1, actual "
print ID3.getMinEntropyAttribute(entropyDataSet7)


#print ""
#print "Entropy example 8"
#print ""
#print "Expect f1, actual "
#print ID3.getMinEntropyAttribute(dataBest1)
#
#print ""
#print "Entropy example 9"
#print ""
#print "Expect f2, actual "
#print ID3.getMinEntropyAttribute(dataBest2)
#
#print ""
#print "Entropy example 8"
#print ""
#print "Expect f2, actual "
#print ID3.getMinEntropyAttribute(dataBest3)
#==============================================================================
 #For Info Gain
 
dataBest1=   [{'f1': 'n','f2': '1', 'Class': 'a'}, {'f1': 'm','f2': '1', 'Class': 'b'}, 
               {'f1': 'n','f2': '1', 'Class': 'a'}, {'f1': 'm', 'f2': '1','Class': 'b'}, 
               {'f1': 'n', 'f2': '1','Class': 'a'}, {'f1': 'm', 'f2': '1','Class': 'b'},
               {'f1': 'm','f2': '1', 'Class': 'b'}, {'f1': 'm', 'f2': '1','Class': 'b'}      
               ]
dataBest2=   [{'f1': 'm','f2': '1', 'Class': 'a'}, {'f1': 'm','f2': '2', 'Class': 'b'}, 
               {'f1': 'n','f2': '1', 'Class': 'a'}, {'f1': 'm', 'f2': '2','Class': 'b'}, 
               {'f1': 'n', 'f2': '1','Class': 'a'}, {'f1': 'm', 'f2': '2','Class': 'b'},
               {'f1': 'm','f2': '2', 'Class': 'b'}, {'f1': 'm', 'f2': '2','Class': 'b'}      
               ]

dataBest3=   [{'f1': 'm','f2': '1', 'Class': 'a'}, {'f1': 'm','f2': '2', 'Class': 'b'}, 
               {'f1': 'm','f2': '1', 'Class': 'a'}, {'f1': 'm', 'f2': '2','Class': 'b'}, 
               {'f1': 'm', 'f2': '1','Class': 'a'}, {'f1': 'm', 'f2': '2','Class': 'b'},
               {'f1': 'm','f2': '2', 'Class': 'b'}, {'f1': 'm', 'f2': '2','Class': 'b'}      
               ]







best=ID3.getAttWithHighestInfoGain(dataBest1)
print "Expect f1, Actual " + best

best=ID3.getAttWithHighestInfoGain(dataBest2)
print "Expect f2, Actual " + best

best=ID3.getAttWithHighestInfoGain(dataBest3)
print "Expect f2, Actual " + best

#Test for GetMode


#Miscellaneous Test
#outputs={"a":3,"b":1,"c":2}
#sorted_outputs = sorted(outputs.items(), key=operator.itemgetter(1),reverse=True)
#
#print sorted_outputs
#print sorted_outputs[0]


#==============================================================================

print("\n\n\n")

#TEST ID3 TREE


def removekey(lst, key):
    rstList=[]
    for aData in lst:
       rstList.append( removekeyInDic(aData,key)) 
    return rstList

def removekeyInDic(d, key):
    r = dict(d)
    del r[key]
    return r 

XXdata = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]



def testID3AndEvaluate(data, dataName):
  
  tree = ID3.ID3(data, 0)
  dataExldOutput=removekey(data,"Class")
  
  if tree != None:
    index=0
    for aSample in dataExldOutput:
        ans = ID3.evaluate(tree, aSample)
        if ans != data[index]["Class"]:
          print "ID3 C"+dataName+"E" +str(index)+" test failed."
        else:
          print "ID3 C"+dataName+"E" +str(index)+" test succeeded."
        index=index + 1
    
  else:
    print "ID3 C"+dataName+ "test failed -- no tree returned"
    

testID3AndEvaluate(XXdata,"XXdata")    
 

testDataSet=[
        entropyDataSet1,
             entropyDataSet2,
              entropyDataSet3,
             entropyDataSet4,
             entropyDataSet5,
             entropyDataSet6,
             entropyDataSet7,
             entropyDataSet8,
             entropyDataSet9,
             entropyDataSet10,
             dataBest1,
             dataBest2,
             dataBest3
             ]
testDataIndex=0
for testData in testDataSet:
    testDataIndex=testDataIndex+1
    testID3AndEvaluate(testData,str(testDataIndex))    



def testID3AndTest():
  trainData = [dict(a=1, b=0, c=0, Class=1), dict(a=1, b=1, c=0, Class=1), 
  dict(a=0, b=0, c=0, Class=0), dict(a=0, b=1, c=0, Class=1)]
  testData = [dict(a=1, b=0, c=1, Class=1), dict(a=1, b=1, c=1, Class=1), 
  dict(a=0, b=0, c=1, Class=0), dict(a=0, b=1, c=1, Class=0)]
  tree = ID3.ID3(trainData, 0)
  fails = 0
  if tree != None:
    acc = ID3.test(tree, trainData)
    if acc == 1.0:
      print "testing on train data succeeded."
    else:
      print "testing on train data failed."
      fails = fails + 1
    acc = ID3.test(tree, testData)
    if acc == 0.75:
      print "testing on test data succeeded."
    else:
      print "testing on test data failed."
      fails = fails + 1
    if fails > 0:
      print "Failures: ", fails
    else:
      print "testID3AndTest succeeded."
  else:
    print "testID3andTest failed -- no tree returned."

testID3AndTest()





data=parse.parse("house_votes_84.data")
#tree=ID3.ID3(data,"1")
#acc = ID3.test(tree, data)
#
#if acc ==1.0:
#    print "testing on train data succeeded."
#else:
#    print "testing on test data failed."
print "\n\n\n"
#node.breadth_first_search(tree)


#For subtree number testing

if ID3.ID3(entropyDataSet1,1).number==1:
    print "Pass number testing 1"
else:
    print "Fail to pass number testing 1"
    
    
sampleDataforNumberTesting=[
 dict(a=1, b=0, c=1, Class=4),
 dict(a=1, b=15, c=1, Class=4),
 dict(a=1, b=14, c=1, Class=4),
 
 dict(a=0, b=0, c=1, Class=1),
 dict(a=0, b=0, c=1, Class=1),
 
 dict(a=0, b=1, c=0, Class=2),
 dict(a=0, b=1, c=0, Class=2),
 dict(a=0, b=1, c=0, Class=2),
 
 dict(a=0, b=1, c=1, Class=3),
 dict(a=0, b=1, c=1, Class=3)
 ]  

numberTestRoot2=ID3.ID3(sampleDataforNumberTesting,1)

print numberTestRoot2.number
if numberTestRoot2.number==10:
    children_numberTestRoot2=numberTestRoot2.children
    
#    print children_numberTestRoot2
#    print numberTestRoot2.label
#    print children_numberTestRoot2[0].number
#    print children_numberTestRoot2[1].number
#    print children_numberTestRoot2[14].number
#    print children_numberTestRoot2[15].number
    
print "\n\n"
#x= children_numberTestRoot2[0].children.values()
#for element in x:
#    print element.label
##    if (r==3)：
##        print "OK"
#node.breadth_first_search(numberTestRoot2)

#leaveNodes =  numberTestRoot2.getLeaves()
#for leaveNode in leaveNodes:
#    print leaveNode.parent.label
#print leaveNodes
#for leaveNode in leaveNodes:
#    print leaveNode.label