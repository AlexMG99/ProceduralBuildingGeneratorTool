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

from pbg.floorEdit import AddFloor, RemoveFloor
from pbg.buildingGenerator import GenerateBuilding


# Creates Blender Main Panel Controller
class MainPanelPBG(bpy.types.Panel):
    bl_label = "Procedural Building Generator"
    bl_idname = "NODE_PT_MAINPANELPBG"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PBG'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Floor", icon='OBJECT_ORIGIN')
        
        row = layout.row()
        
        # Check if floor is created
        floorObj = bpy.context.scene.objects.get("Floor")
        if(floorObj):
            row.operator("pbg.generate", text="Generate Building", icon='GREASEPENCIL')
            row = layout.row()
            row.operator(RemoveFloor.bl_idname, text="Remove floor", icon='PANEL_CLOSE')
        else:
            row.operator(AddFloor.bl_idname, text="Create floor", icon='MESH_PLANE')


def register():
    bpy.utils.register_class(MainPanelPBG)


def unregister():
    bpy.utils.unregister_class(MainPanelPBG)


if __name__ == "__main__":
    register()