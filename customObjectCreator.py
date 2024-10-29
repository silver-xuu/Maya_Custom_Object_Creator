import maya.cmds as cmds

class Custom_Obeject_Creation_Window(object):
    
    def __init__(self):
        
        self.window = "Custom_Obeject_Creation_Window"
        self.title = "Custom Object Creator"
        self.size = (400,600)
        self.objTypes = ['Cube','Sphere']
        
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)
            
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        self.createUI()
        
        cmds.showWindow()
    
    def createUI(self):
        cmds.columnLayout(adjustableColumn= True)
        
        cmds.text(self.title)
        cmds.separator(height=20)
        # default object type is cube
        self.objType = cmds.radioButtonGrp(label = 'Select an Object Type: ', labelArray2 = self.objTypes, 
                                           select= 0, numberOfRadioButtons = 2, onCommand1 = self.onCubeSelected, onCommand2 = self.onSphereSelected)
        self.currentType = 0
        self.objCount = cmds.intSliderGrp(field=True, label = "Object Count:", 
                                             value = 1, minValue = 1, maxValue = 50)
        
        cmds.separator(height=20)
        
        self.objName = cmds.textFieldGrp(label = 'Defaut Object Name:', text='pCube')
        cmds.separator(height = 10, style = 'none')
        #size slider groups
        cmds.text("Size")
        self.objWidth = cmds.floatSliderGrp(field=True, label='Width: ', 
                                            value = 1, minValue = 0, maxValue = 10)
        self.objHeight = cmds.floatSliderGrp(field=True, label='Height: ', 
                                             value = 1, minValue = 0, maxValue = 10)
        self.objDepth = cmds.floatSliderGrp(field=True, label='Depth: ', 
                                            value = 1, minValue = 0, maxValue = 10)
        # by default this option is grey out
        self.objRadius = cmds.floatSliderGrp(field=True, label='Radius: ', 
                                            value = 1, minValue = 0, maxValue = 10,
                                            enable = False)
        
        cmds.separator(height = 10, style = 'none')
        cmds.text("Subdivisions")
        #subdivision slider groups
        self.objWidthDiv = cmds.intSliderGrp(field=True, label = "Width Divisions:", 
                                             value = 1, minValue = 1, maxValue = 50)
        self.objHeightDiv = cmds.intSliderGrp(field=True, label = "Height Divisions:", 
                                               value = 1, minValue = 1, maxValue = 50)
        self.objDepthDiv = cmds.intSliderGrp(field=True, label = "Depth Divisions:", 
                                             value = 1, minValue = 1, maxValue = 50)
        # by default this option is grey out
        self.objAxisDiv = cmds.intSliderGrp(field=True, label = "Axis Divisions:", 
                                            value = 1, minValue = 1, maxValue = 50,
                                            enable = False)
        cmds.separator(height = 20, style = 'none')
        cmds.text("Default Pivot Position")
        self.pivotLocation = cmds.radioButtonGrp(label = 'Select Default Pivot Position : ', labelArray2 = ['Centre','Centre Bottom'], 
                                           select= 0, numberOfRadioButtons = 2)
        cmds.separator(height = 20, style = 'none')
        self.cubeCreateBtn = cmds.button(label='Create Cubes',command = self.createObj)
    
    def createObj(self, *args):
        name = cmds.textFieldGrp(self.objName, query = True, text = True)
        # get size
        width = cmds.floatSliderGrp(self.objWidth, query = True, value = True)
        height = cmds.floatSliderGrp(self.objHeight, query = True, value = True)
        depth = cmds.floatSliderGrp(self.objDepth, query = True, value = True)
        radius = cmds.floatSliderGrp(self.objRadius, query = True, value = True)
        # get subdivisions
        widthDiv = cmds.intSliderGrp(self.objWidthDiv, query = True, value = True)
        heightDiv = cmds.intSliderGrp(self.objHeightDiv, query = True, value = True)
        depthDiv = cmds.intSliderGrp(self.objDepthDiv, query = True, value = True)
        axisDiv = cmds.intSliderGrp(self.objAxisDiv, query = True, value = True)
        
    
    def onCubeSelected(self, *args):
        self.toggleCubeUI(enable = True)
        self.toggleSphereUI(enable = False)
        
        self.changeButtonLabel(0)
        self.changeDefaultName(0)
        
    
    def onSphereSelected(self, *args):
        self.toggleCubeUI(enable = False)
        self.toggleSphereUI(enable = True)
        
        self.changeButtonLabel(1)
        self.changeDefaultName(1)
    
    def changeDefaultName(self, type:int):
        name = cmds.textFieldGrp(self.objName, query = True, text = True)
        if any(ele in name for ele in self.objTypes):
            cmds.textFieldGrp(self.objName, edit = True, text=f'p{self.objTypes[type]}')
    
    def changeButtonLabel(self, type:int):
        cmds.button(self.cubeCreateBtn, edit = True, label=f'Create {self.objTypes[type]}s')
    
    def toggleCubeUI(self, enable:bool):
        cmds.floatSliderGrp(self.objWidth, edit = True, enable = enable)
        cmds.floatSliderGrp(self.objHeight, edit = True, enable = enable)
        cmds.floatSliderGrp(self.objDepth, edit = True, enable = enable)
        cmds.intSliderGrp(self.objWidthDiv, edit = True, enable = enable)
        cmds.intSliderGrp(self.objDepthDiv, edit = True, enable = enable)
        
    
    def toggleSphereUI(self, enable:bool):
        cmds.floatSliderGrp(self.objRadius, edit = True, enable = enable)
        cmds.intSliderGrp(self.objAxisDiv, edit = True, enable = enable)
        
    
    def bottomObjPivot(self):
        pass
myWindow = Custom_Obeject_Creation_Window()