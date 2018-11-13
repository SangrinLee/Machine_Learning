#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
from node import Node

import math
import operator
import random
import copy
import node
#data: list of dictionary


def ID3(examples, default):
    #Cond:   Example is empty
    #Return: Node contains Output value
    if len(examples)==0:
        root = Node()
        root.label=default
#        root.number=len(examples)
        root.modeValue=getModeOutput(examples)
        return root 
      
    #Cond:   All given examples have the same output value
    #Return: Node contains Output value
    elif  hasSameClassification(examples):
        root = Node()
        root.label=examples[0]["Class"]
#        root.number=len(examples)
        root.modeValue=getModeOutput(examples)
        return root 
    
    #Cond:   No non-trivial split of the examples is possible
    #Return: Node contains Output value
    elif  hasTrivialSplit(examples):
        root = Node()
        root.label=getModeOutput(examples) 
#        root.number=len(examples)
        root.modeValue=getModeOutput(examples)
        return root 

    else:
        best_attr=getAttWithHighestInfoGain(examples)
        
        root = Node()
        root.label=best_attr
#        root.number=len(examples)
        root.modeValue=getModeOutput(examples)
        
        splitedDataSets=getSplitData(examples,best_attr)
        
        
        for subDataSet in splitedDataSets:
            
            subtree=ID3(subDataSet,default)
#            subtree.number=len(subDataSet)
            subtree.modeValue=getModeOutput(subDataSet)

            root.children[subDataSet[0][best_attr]]= subtree
            
        root.defaultValue=randomPickOne(root.children.keys())

        return root

def prune(root_node, examples):
    org_acc =test(root_node,examples)
    allNodes=node.loopTree(root_node)
    
    for aNode in allNodes:
        
        label_pre =aNode.label
        childs_pre=aNode.children
        
        aNode.label=aNode.modeValue
        aNode.children={}
        
        updt_acc=test(root_node,examples)
        if updt_acc<org_acc:   #Lazy action, if is equal no undo is conducted
            aNode.label   =label_pre
            aNode.children=childs_pre
        else:
            allSubChilds=node.loopTree(aNode)
            for subChild in allSubChilds:
                allNodes.remove(subChild)
               
    return root_node  


        
def test(root_node, examples):   
    exampleNum=len(examples)
    correctNum=0
    
    for example in examples:
        if example["Class"]== evaluate(root_node,example):
            correctNum=correctNum+1
    return correctNum/exampleNum

def evaluate(root_node, example):
    nodeCopy=copy.deepcopy(root_node)
    while len(nodeCopy.children)!=0:  
        childNodeKey=example[nodeCopy.label]
        if childNodeKey not in nodeCopy.children.keys():
            childNodeKey=nodeCopy.defaultValue

        nodeCopy= nodeCopy.children[childNodeKey]

    return nodeCopy.label




#==============================================================================
# #Helper functions
#==============================================================================
def findModeChild(children):
    childs=children.values()   
    mod_childs=[]
    
    mod_value=childs[0].number
      
    for child in childs[1:]:
        if child.number > mod_value:
            mod_value=child.number 
    
    for child in childs:
        if child.number==mod_value:
            mod_childs.append(child) #Add all tie silbings incd itself

    return mod_childs

#Return an attribute value
def getModeOutput(data):
    outputs={}
    
    for aDataSet in data:     
        key=aDataSet["Class"]
        if key in outputs:
            outputs[key]+=1
        else:
            outputs[key] =1  
    
    sorted_outputs = sorted(outputs.items(), key=operator.itemgetter(1),reverse=True)
    
    return getMode(sorted_outputs)

    
    
#Input: list: e.g. [('a', 3), ('c', 2), ('b', 1)]        
def getMode(sorted_outputs):
    tie_outputs=[]
    max_value =sorted_outputs[0][1]
    
    for pair in sorted_outputs:
        if pair[1]==max_value:
            tie_outputs.append(pair[0]) 
       
    if len(tie_outputs)==1:
        return tie_outputs[0]
    else:
        return randomPickOne(tie_outputs)
    
    
def randomPickOne(tie_outputs):
    randomIndex=random.randint(0, len(tie_outputs)-1)   
    return tie_outputs[randomIndex]
               

    
    
# PPS:Check whether all data is non trival
# Input: Data
# Output: Boolean
def hasTrivialSplit(data):     
    baseAttributes =removekey(data[0],"Class")

    for aData in data:
        if removekey(aData,"Class")!=baseAttributes:
            return False
    
    return True
    

# PPS:Check whether all data has same output class
# Input: Data
# Output: Boolean
def hasSameClassification(data):
    
    firstDataClass=data[0]["Class"]
      
    for aData in data:
        if aData["Class"]!=firstDataClass:
            return False
    
    return True
        
    


#PPS： Get the attribute with the split data, that has highest Information Gain
# Input: data
# Output: a list that contains an attribute and the split data in data format
def getAttWithHighestInfoGain(data):
    return getMinEntropyAttribute(data)

# PPS： Get the attribute with the split data, that has least entropy
# Input: data
# Output: a list that contains an attribute and the split data
def getMinEntropyAttribute(data):
    attributes=getAllAttributes(data)    
    
    attributesEntropies={}
    
    for attribute in attributes:  
       attributesEntropies[attribute]=getEntropy(data,attribute)

    OrderedAttrEntropies = sorted(attributesEntropies.items(), key=operator.itemgetter(1))
    attribute=getMode(OrderedAttrEntropies)
    
    return attribute
  

      



# PPS: Split the data by the value of the given attribute
#Input: a data set, attrivute
#Ouput: a list of seperated list of data
def getSplitData(data, attribute):
    splitData=[]
    attributeValue={}
    
    for aEntry in data:
        attributeValue[aEntry[attribute]]=1
    
    for key, value in attributeValue.iteritems():
        aList=[]
        for aEntry in data:
            if aEntry[attribute] ==key:
                aList.append(aEntry)
        splitData.append(aList)
    
    return splitData
  
    


#Get all attributes
def getAllAttributes(data):   
    allAttributes=data[0].keys()
    allAttributes.remove("Class")   
    return allAttributes
 
    


#PPS:Calculate the entropy by given attribute
#Input: Original Data
#Output: float (the entropy)
def getEntropy(data,attribute):
    outputs   ={}
    entropy   =0 #Initial entorpy
    numofData =len(data)
    
    splitedData=getSplitData(data,attribute)

    for oneDataGroup in splitedData:
        
        numofDataInaGroup=len(oneDataGroup)
        partEntropy=0
        outputs   ={}
        for aData in oneDataGroup:
            outputValue=aData["Class"]
            if outputValue in outputs:
                outputs[outputValue]+=1
            else:
                outputs[outputValue] =1  

        for outputValue, counts in outputs.iteritems():
            curt_value_portion=counts/numofDataInaGroup
            partEntropy+=curt_value_portion*get_log(curt_value_portion)

        entropy+=(numofDataInaGroup/numofData)*partEntropy
        
    entropy=-entropy
    
    return entropy 

    
#PPS:Calculate the log with base 2 for the entropy        
def get_log(value):
    if value ==0:
        return 0;
    else:        
        return math.log(value,2)
    
    
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

