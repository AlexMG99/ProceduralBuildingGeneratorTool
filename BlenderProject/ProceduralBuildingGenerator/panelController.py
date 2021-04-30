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
class MainPanelPBG(bpy.types.Panel):
    bl_label = "Procedural Building Generator"
    bl_idname = "NODE_PT_MAINPANELPBG"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PBG'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        
        # Check if floor is created
        floorObj = bpy.data.collections.get("Building")
        if(floorObj):
            
            mat = floorObj.objects[0].data.materials["Frame"]

            # Extra details¡¡
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            row = box.row()
            row.prop(mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"], "default_value", text="Window color")
            
            # floorObj.objects[0].data.material[1] = mat
            
            row = layout.row()
            row.operator(RemoveBuilding.bl_idname, text="Remove building", icon='PANEL_CLOSE')
        else:
            # Parameter section
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
            
            # Extra details
            box = layout.box()
            
            row = box.row()
            row.label(text="Texture parameters", icon='BRUSH_DATA')
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "twoColors")
            row.prop(context.scene.buildingParameters, "wallTexture")
            
            row = box.row()
            row.prop(context.scene.buildingParameters, "windowColor", text="Window color")
            
            # Generate Building button
            row = layout.row()
            row.operator(GenerateBuilding.bl_idname, text="Generate Building", icon='MESH_PLANE')
        
            
            
        # Auxiliar help
        row = layout.row()
        row.prop(context.scene.utilitiesParameters, "edgeIdx")
        row.prop(context.scene.utilitiesParameters, "objName")
        row = layout.row()
        row.operator(SelectEdge.bl_idname, text="Select Object Edge")
        row.operator(SelectFace.bl_idname, text="Select Object Face")


def register():
    bpy.utils.register_class(MainPanelPBG)


def unregister():
    bpy.utils.unregister_class(MainPanelPBG)


if __name__ == "__main__":
    register()