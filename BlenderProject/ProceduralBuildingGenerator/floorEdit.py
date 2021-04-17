import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  

import random

# Import rules fuinctions
from pbg import rules
                
# Add Floor operator
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
    
    # Generate random floor
    numCuts = random.randint(1,3)
    edgeSplit = random.randint(0, len(plane.data.edges))
    rules.splitMesh(plane, numCuts, edgeSplit)
    
    # Modify name
    plane.name = "Floor"


# Remove floor operator    
class RemoveFloor(bpy.types.Operator):
    bl_label = "Remove Floor"
    bl_idname = "pbg.removefloor"
    
    def execute(self, context):
        
        # Creates the floor base
        removeFloor(self, context)
        
        return{'FINISHED'}

# Creates the base floor   
def removeFloor(context, operator):
    
    # Get created cube
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    plane = bpy.data.objects['Floor'].select_set(True)
    
    bpy.ops.object.delete() 
            


# Class Initialization
def register():
    bpy.utils.register_class(AddFloor)
    bpy.utils.register_class(RemoveFloor)


def unregister():
    bpy.utils.unregister_class(AddFloor)
    bpy.utils.unregister_class(RemoveFloor)


if __name__ == "__main__":
    register()