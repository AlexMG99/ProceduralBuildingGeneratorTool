import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  
  
class AddFloor(bpy.types.Operator):
    bl_label = "Add Floor with parameters"
    bl_idname = "pbg.addfloor"
    
    def execute(self, context):
        # Creates the floor base
        floorSize = [1.0, 1.0, 1.0]  
        addFloor(self, context, floorSize)
        
        return{'FINISHED'}

# Creates the base floor   
def addFloor(context, operator, size):
    
    # Generate a new cube
    bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], size[2]))
    
    # Get created cube
    plane = bpy.context.selected_objects[0]
    
    # Modify name
    plane.name = "Floor"
    
    renameMesh(plane)
            
            
def register():
    bpy.utils.register_class(AddFloor)


def unregister():
    bpy.utils.unregister_class(AddFloor)


if __name__ == "__main__":
    register()