import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  

import random

# Import rules fuinctions
from pbg import rules
from pbg import generateModules

# Reload module
import imp
imp.reload(rules)
imp.reload(generateModules)
                
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
    collection = bpy.data.collections.new("Building")
    bpy.context.scene.collection.children.link(collection)

    # NOTE the use of 'collection.name' to account for potential automatic renaming
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection
    
    generateModules.generateBuildingFloor(4, size)


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
    
    # Get collection
    collection = bpy.data.collections.get('Building')
 
    for obj in collection.objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    bpy.data.collections.remove(collection)
            


# Class Initialization
def register():
    bpy.utils.register_class(AddFloor)
    bpy.utils.register_class(RemoveFloor)


def unregister():
    bpy.utils.unregister_class(AddFloor)
    bpy.utils.unregister_class(RemoveFloor)


if __name__ == "__main__":
    register()