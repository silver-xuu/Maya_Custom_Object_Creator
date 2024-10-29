import maya.cmds as cmds

class Custom_Obeject_Creation_Window(object):
    
    def __init__(self):
        
        self.window = "Custom_Obeject_Creation_Window"
        self.title = "Custom Object Creator"
        self.size = (400,400)
        
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)
            
        cmds.columnLayout(adjustableColumn= True)    
            
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.showWindow()

myWindow = Custom_Obeject_Creation_Window()