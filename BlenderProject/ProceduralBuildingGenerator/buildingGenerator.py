import bpy  
from bpy.types import Operator  

# Generates the building structure
class GenerateBuilding(bpy.types.Operator):
    bl_label = "Generates the building structure"
    bl_idname = "pbg.generate"
    
    def execute(self, context):
        generateBuilding(self, context, 5)
        
        return{'FINISHED'}

# Creates the base floor   
def generateBuilding(context, operator, numFloor):
    
    # Go to edit mode, face selection mode
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})
    
    bpy.ops.object.mode_set( mode = 'OBJECT' )

# Class Initialization
def register():
    bpy.utils.register_class(GenerateBuilding)


def unregister():
    bpy.utils.unregister_class(GenerateBuilding)


if __name__ == "__main__":
    register()