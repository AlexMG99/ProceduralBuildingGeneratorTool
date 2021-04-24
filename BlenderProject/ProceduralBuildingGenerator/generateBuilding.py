import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  

import random

# Import rules fuinctions
from pbg import generateModules
from pbg import parameters

# Reload module
import imp
imp.reload(parameters)
imp.reload(generateModules)
                
# Generate Building operator
class GenerateBuilding(bpy.types.Operator):
    bl_label = "Generate Building with parameters"
    bl_idname = "pbg.generatebuilding"
    
    def execute(self, context):
        # Creates the floor base
        generateBuilding(self, context)
        
        return{'FINISHED'}

# Creates the building exterior structure  
def generateBuilding(context, operator):
    collection = bpy.data.collections.new("Building")
    bpy.context.scene.collection.children.link(collection)

    # NOTE the use of 'collection.name' to account for potential automatic renaming
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection
    
    buildingParameters = bpy.context.scene.buildingParameters
    
    generateModules.generateBuilding(buildingParameters.numFloor, buildingParameters.rowX, buildingParameters.rowY, bpy.context.scene.buildingParameters.moduleSize)
    # generateModules.generateBuildingSide(buildingParameters.moduleSize, 0, 1, 1, 0)

# Remove floor operator    
class RemoveBuilding(bpy.types.Operator):
    bl_label = "Remove Building"
    bl_idname = "pbg.removebuilding"
    
    def execute(self, context):
        
        # Delete the building collection
        removeBuilding(self, context)
        
        return{'FINISHED'}

# Delete the building collection   
def removeBuilding(context, operator):
    
    # Get collection
    collection = bpy.data.collections.get('Building')
 
    for obj in collection.objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    bpy.data.collections.remove(collection)
            


# Class Initialization
def register():
    bpy.utils.register_class(GenerateBuilding)
    bpy.utils.register_class(RemoveBuilding)


def unregister():
    bpy.utils.unregister_class(GenerateBuilding)
    bpy.utils.unregister_class(RemoveBuilding)


if __name__ == "__main__":
    register()