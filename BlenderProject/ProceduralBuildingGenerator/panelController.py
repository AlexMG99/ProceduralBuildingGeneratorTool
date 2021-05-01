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
        row.label(text="Building parameters", icon='OBJECT_ORIGIN')
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "moduleSize")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "numFloor")
        row.prop(context.scene.buildingParameters, "rowX")
        row.prop(context.scene.buildingParameters, "rowY")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "buildingType")
        

class WindowPanelPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Window parameters"
    bl_idname = "NODE_PT_WINDOWPANELPBG"
    bl_parent_id = "NODE_PT_MAINPANELPBG"
    
    def draw(self, context):
        layout = self.layout
        box = layout.box()
        
        # Window building parameters
        floorObj = bpy.data.collections.get("Building")
          
        row = box.row()
        row.label(text="Window parameters", icon='OBJECT_ORIGIN')
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "windowSize")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "windowFrame")
        
        row = box.row()
        row.prop(context.scene.buildingParameters, "windowType")
        
        # Window texture parameters
        row = box.row()
        row.label(text="Texture parameters", icon='BRUSH_DATA')
        
        row = box.row()
        row.prop(context.scene.textureParameters, "twoColors")
        row.prop(context.scene.textureParameters, "wallTexture")
        
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
        row.operator(SelectEdge.bl_idname, text="Select Object Edge",)
        row.operator(SelectFace.bl_idname, text="Select Object Face")
        
class ButtonPBG(BaseClassPBG, bpy.types.Panel):
    bl_label = "Button action"
    bl_idname = "NODE_PT_TOOLPANELPBG"
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
classes = (MainPanelPBG, WindowPanelPBG, ToolPanelPBG, ButtonPBG)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()