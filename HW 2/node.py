import Queue

class Node:
  def __init__(self):
    self.label        = None
    self.children     = {}
    self.defaultValue = None

    self.modeValue     = None
     
#Iterate tree by depth first search
def loopTree(root):
    
        s=[]
        node_value=[]
        q = Queue.Queue()
        s.append(root)      #Ensure non loop is there
        q.put(root)
        
        while not q.empty():
            current=q.get()
            
            
            
            current_children=current.children
            
            
            if len(current_children)!=0:
                node_value.append(current) #Excludes leaves
                
                for key, value in current_children.iteritems():
                    if value not in s:
                        s.append(value)
                        q.put(value)
                        
        return node_value
