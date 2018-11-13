# -*- coding: utf-8 -*-
from node import Node

import node
#aDic=N
#
#if aDic==Empty:
#    print "None"
#else:
#    print "is not none"
    
    
#aList=[0,1,2,3,4]
#
#for ele in range(1,len(aList)):
#    print ele
#    
#print aList[1:]

root = Node()
root.label="root"

cld1 = Node()
cld2 = Node()
cld3 = Node()

cld1.label="cld1"
cld2.label="cld2"
cld3.label="cld2"

cld1_1 = Node()
cld1_1.label="cld1-1"

root.children=dict(a=cld1,b=cld2,c=cld3)

cld1.children=dict(x=cld1_1)
cld2.children=dict(x=cld1_1)
#print root.label
#clds= root.children.values()
#
#print clds
#
#cld1_bp=clds[0]
#clds_bp=clds
#
#print cld1_bp
#
#root.children={}
#print cld1_bp
#print clds
#print root.children
#root.children=clds_bp
#
#print root.children

allNodes= node.loopTree(root)
#print len(allNodes)
#
#for aNode in allNodes:
#    print aNode.label
##print root.children.values()
#
#for aNode in allNodes:
#    print aNode
#    if aNode==root:
#        for eachChild in root.children.values():
#            allSubChildNodes= node.loopTree(eachChild)
#            for eachSubChild in allSubChildNodes:
#                allNodes.remove(eachSubChild)

#print root.children
#
#allNodes[0].children={}
#print root.children

#print allNodes
#allNodes.remove(root)

#print allNodes
#print root


#aList=[1,2,3,4,5]
#
#for ele in aList:
#    print ele
#    if ele==1:
#        aList.remove(2)
#        aList.remove(5)
    
a=True
b=True
c=False

if a and b:
    print "ok"
if a and c:
    print "ok"
