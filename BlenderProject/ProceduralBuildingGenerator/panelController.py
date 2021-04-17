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

from pbg.floorEdit import ScaleOperator

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
        row.operator(ScaleOperator.bl_idname, text="Modify Floor")
        
        row.prop(ScaleOperator.floorNum, "hide_select")
        
        row = layout.row()
        # Check if floor is created
        floorObj = bpy.context.scene.objects.get("Floor")
        if(floorObj):
            row.operator(AddFloor.bl_idname, text="Modify Floor", icon='CUBE')
        else:
            row.operator(AddFloor.bl_idname, text="Generate Building", icon='CUBE')

def addFloor(context, operator, size):
    
    # Generate a new cube
    bpy.ops.mesh.primitive_cube_add(scale=(size[0], size[1], size[2]))
    
    # Get created cube
    cube = bpy.context.selected_objects[0]
    
    # Modify name
    cube.name = "Floor"
    
def modifyFloor(context, operator, size):
    
    # Get created cube
    cube = bpy.context.selected_objects[0]
    
    # Change scale
    cube.scale = size;
        
        
class AddFloor(bpy.types.Operator):
    bl_label = "Add Floor with parameters"
    bl_idname = "pbg.addfloor"
    
    def execute(self, context):
        
        floorObj = bpy.context.scene.objects.get("Floor")
        if(floorObj):
            floorSize = [1.0, 2.0, 1.0]
            
            bpy.data.objects['Floor'].select_set(True)
            modifyFloor(self, context, floorSize)
        else:
            floorSize = [1.0, 2.0, 1.0]
            
            addFloor(self, context, floorSize)
            
        
        return{'FINISHED'}


def register():
    bpy.utils.register_class(MainPanelPBG)
    bpy.utils.register_class(AddFloor)
    bpy.utils.register_class(ScaleOperator)


def unregister():
    bpy.utils.unregister_class(MainPanelPBG)
    bpy.utils.unregister_class(AddFloor)
    bpy.utils.unregister_class(ScaleOperator)


if __name__ == "__main__":
    register()