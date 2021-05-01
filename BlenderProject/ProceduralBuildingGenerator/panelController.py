bl_info = {
    "name" : "Procedural Building Generator",
    "author" : "Alex Morales Garcia",
    "version" : 1.0,
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Procedural",
}

import bpy

from pbg.generateBuilding import *
from pbg.utilities import *

from pbg import parameters

# Reload module
import imp
imp.reload(parameters)

# Creates Blender Main Panel Controller
class BaseClassPBG:
    bl_label = "Procedural Building Generator"
    bl_idname = "NODE_PT_MAINPANELPBG"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PBG'

class MainPanelPBG(BaseClassPBG, bpy.types.Panel):

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        
        # Check if floor is created
        row = box.row()
        row.label(text="Structure parameters", icon='OBJECT_ORIGIN')
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "moduleSize")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "numFloor")
        row.prop(context.scene.buildingParameters, "rowX")
        row.prop(context.scene.buildingParameters, "rowY")
        
        box = layout.box()
        row = box.row()
        row.label(text="Facade parameters", icon='SNAP_FACE')
        row = box.row()
        row.prop(context.scene.buildingParameters, "randomnessBuilding", text="Randomness")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "buildingType")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "buildingStreet")
        

class WindowPanelPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Window parameters"
    bl_idname = "NODE_PT_WINDOWPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    
    def draw(self, context):
        layout = self.layout
    
        
        # Window building parameters
        floorObj = bpy.data.collections.get("Building")
        
        if(floorObj):
            # Window texture parameters
            box = layout.box()
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            # Window colors
            row = box.row()
            mat = floorObj.objects[0].data.materials["Frame"]
            row.prop(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"], "default_value", text="Frame color")
            
            row = box.row()
            mat = floorObj.objects[0].data.materials["Glass"]
            row.prop(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"], "default_value", text="Glass color")
        
        else:
            box = layout.box()
            row = box.row()
            row.label(text="Construction parameters", icon='OBJECT_ORIGIN')
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "windowSize")
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "windowFrame")
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "windowType", text="Type")
            
            # Window texture parameters
            box = layout.box()
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            # Window colors
            row = box.row()
            row.prop(context.scene.textureParameters, "windowColor", text="Frame color")
            
            row = box.row()
            row.prop(context.scene.textureParameters, "glassColor", text="Glass color")
    
    
class WallPanelPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Wall parameters"
    bl_idname = "NODE_PT_WALLPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        
        # Wall texture parameters
        row = box.row()
        row.label(text="Texture parameters", icon='BRUSH_DATA')
        
        row = box.row()
        row.prop(context.scene.textureParameters, "twoColors")
        row.prop(context.scene.textureParameters, "wallTexture")
        
        # Wall colors
        if(context.scene.textureParameters.wallTexture == False):
            row = box.row()
            row.prop(context.scene.textureParameters, "wallColor", text="Wall color")
            if(context.scene.textureParameters.twoColors == True):
                row = box.row()
                row.prop(context.scene.textureParameters, "wallColorAux", text="Wall color 2")
        else:
            row = box.row()
            row.prop(context.scene.textureParameters, "wallTextures")
          
        
class DoorPanelPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Door parameters"
    bl_idname = "NODE_PT_DOORPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    
    def draw(self, context):
        layout = self.layout
        
        # Door building parameters
        floorObj = bpy.data.collections.get("Building")
        
        if(floorObj):
            # Door texture parameters
            box = layout.box()
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            # Window colors
            row = box.row()
            mat = floorObj.objects[0].data.materials["Frame Door"]
            row.prop(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"], "default_value", text="Frame color")
            
            row = box.row()
            mat = floorObj.objects[0].data.materials["Glass Door"]
            row.prop(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"], "default_value", text="Glass color")
        
        else:
            box = layout.box()
            row = box.row()
            row.label(text="Construction parameters", icon='OBJECT_ORIGIN')
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "doorSize")
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "doorFrame")
            
            # Window texture parameters
            box = layout.box()
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            # Window colors
            row = box.row()
            row.prop(context.scene.textureParameters, "windowColor", text="Frame color")
            
            row = box.row()
            row.prop(context.scene.textureParameters, "glassColor", text="Glass color") 

class ToolPanelPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Tool debug"
    bl_idname = "NODE_PT_TOOLPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        
        # Auxiliar help
        row = box.row()
        row.label(text="Debug parameters", icon='TOOL_SETTINGS')
        
        row = box.row()
        row.prop(context.scene.utilitiesParameters, "edgeIdx", text="Index")
        row.prop(context.scene.utilitiesParameters, "objName")
        row = box.row()
        row.operator(SelectEdge.bl_idname, text="Select Object Edge")
        row.operator(SelectFace.bl_idname, text="Select Object Face")
        
class ButtonPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Button action"
    bl_idname = "NODE_PT_BUTTONPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    bl_options = {'HIDE_HEADER'}
    
    def draw(self, context):
        layout = self.layout
        
        floorObj = bpy.data.collections.get("Building")
        if(floorObj):
            row = layout.row()
            row.operator(RemoveBuilding.bl_idname, text="Remove building", icon='PANEL_CLOSE')
        else:
            # Generate Building button
            row = layout.row()
            row.operator(GenerateBuilding.bl_idname, text="Generate Building", icon='MESH_PLANE')


# Register classes
classes = (MainPanelPBG, WindowPanelPBG, DoorPanelPBG, WallPanelPBG, ToolPanelPBG, ButtonPBG)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()