import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  

import random
from mathutils import Vector

# Import rules fuinctions
from . import generateModules
from . import generateFacade
from . import generateFloor
from . import parameters
                
# Generate Building operator
class GenerateBuilding(bpy.types.Operator):
    bl_label = "Generate Building with parameters"
    bl_idname = "pbg.generatebuilding"
    
    def execute(self, context):
        # Creates the floor base
        generateBuilding()
        
        return{'FINISHED'}

# Creates the building exterior structure  
def generateBuilding():
    collection = bpy.data.collections.new("Building")
    bpy.context.scene.collection.children.link(collection)

    # NOTE the use of 'collection.name' to account for potential automatic renaming
    layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection
    
    buildingParameters = bpy.context.scene.buildingParameters
    
    generateBuildingStructure(buildingParameters.numFloor, buildingParameters.rowX, buildingParameters.rowY, bpy.context.scene.buildingParameters.moduleSize)
    # buildingPlant = [False] * (2 * buildingParameters.rowX + 2 * buildingParameters.rowY)
    # generateFacade.generateBuildingFacade(0, 1, 1, 0, buildingParameters.moduleSize, buildingPlant)

# Generate the building
def generateBuildingStructure(floor, colX, colY, size):
    
    # Generate all building floors
    currFloor = 0
    copy = False
    lastModName = "None"
    
    # Information about last floor
    buildingPlant = [False] * (2 * colX + 2* colY)
    
    while currFloor < floor:
        # Generate one floor
        if copy == False:
            lastModName = generateFloor.generateBuildingFloor(currFloor, colX, colY, size, buildingPlant)
            copy = True
        else:
            lastModName = generateFloor.generateBuildingFloorFromPrevious(currFloor, colX, colY, size, buildingPlant, floor)
            # lastModName, currFloor = generateFloor.duplicateBuildingFloor(currFloor, floor, lastModName)
        
        currFloor += 1
    
    
    # Generate building roof
    bpy.ops.object.select_all(action='DESELECT')
        
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    bpy.ops.mesh.select_all( action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'OBJECT')

    lastModName = generateFloor.generateBuildingRoof(floor, colX, colY, size)
    
    # Select all module objects
    collection = bpy.data.collections.get('Building')
    bpy.ops.object.mode_set( mode = 'OBJECT')
    
    for obj in collection.objects:
        obj.select_set(True)
    
    # Combine all objects in one
    bpy.ops.object.join()
    bpy.ops.object.editmode_toggle()
    
    # Rename
    bpy.data.objects.get(lastModName).name = "Building"
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    bpy.ops.mesh.select_all( action = 'SELECT')
    
    bpy.ops.mesh.remove_doubles(threshold=0.01)
    
    bpy.ops.mesh.select_all( action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'OBJECT') 

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
    
    # Update material colors
    mat = collection.objects[0].data.materials["Frame"]
    bpy.context.scene.textureParameters.windowColor = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value
    
    mat = collection.objects[0].data.materials["Glass"]
    bpy.context.scene.textureParameters.glassColor = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value
    
    """mat = collection.objects[0].data.materials["Wall 1"]
    if(mat.name == "Wall 1"):
        bpy.context.scene.textureParameters.wallColor = mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value
    """
    
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