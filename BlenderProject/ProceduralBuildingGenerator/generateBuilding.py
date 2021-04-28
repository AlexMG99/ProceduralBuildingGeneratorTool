import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  

import random
from mathutils import Vector

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
    #generateBuildingFacade(0, 1, 1, 0, buildingParameters.moduleSize)
    
# Generate one building side                                                             
def generateBuildingFacade(side, colX, colY, cFloor, size):
    i = 0
    turnBuilding = 0
    advancement = 0.0
    colOut = 0.0
    
    fromLast = 0
    
    opened = False
    closed = False
    
    while i < colX:
        turned = False;
        
        # Generate a new cube
        bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], size[2]))
    
        # Get created cube
        plane = bpy.context.selected_objects[0]
        plane.name = "Module " + str(side) + "." + str(i)
            
        # Generate Module and move
        """ rand = random.randint(0, 1)
        if rand == 0:
            generateModuleWindow(plane)
        else:
            generateModuleWall(plane) """
        
        generateModules.generateModuleWindow(plane, Vector((0.5, 0.75)))
            
        bpy.data.objects[plane.name].select_set(True)
        
        # Building one module out
        if opened == False and closed == False:
            if turnBuilding == 0 and i != 0 and i != colX:
                turnBuilding = random.randint(0, 1)
        
            # Module Outside
            if turnBuilding == 1:
                advancement -= 1.0
                bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL')
                turnBuilding = 2
                turned = True
                opened = True
            
                if side == 0:
                    bpy.ops.transform.translate(value=(0.0, 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
                elif side == 1:
                    bpy.ops.transform.translate(value=(1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                elif side == 2:
                    bpy.ops.transform.translate(value=(0.0, -1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                elif side == 3:
                    bpy.ops.transform.translate(value=(-1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)         
        
        # Module inside
        if opened == True and closed == False and fromLast > 1:        
            turnBuilding = random.randint(0, 3)
            
            if turnBuilding == 1 or i == colX - 1:    
                advancement -= 1.0
                bpy.ops.transform.rotate(value=-1.5708, orient_axis='Z', orient_type='GLOBAL')
                turnBuilding = 2
                turned = True
                closed = True
                
                if side == 0:
                    bpy.ops.transform.translate(value=(0.0, -1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
                elif side == 1:
                    bpy.ops.transform.translate(value=(-1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                elif side == 2:
                    bpy.ops.transform.translate(value=(0.0, 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                elif side == 3:
                    bpy.ops.transform.translate(value=(1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
             
        # Move to building position   
        if side == 0:
            bpy.ops.transform.translate(value=(advancement, colOut, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 1:
            bpy.ops.transform.translate(value=(colOut + 2.0 * (colY - 1) + 1.0 , - advancement - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 2:
            bpy.ops.transform.translate(value=(2.0 * (colX - 1) - advancement, -colOut - 2.0 * colY, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 3:
            bpy.ops.transform.translate(value=(-colOut -1.0, - 2.0 * (colX - 1) + advancement - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        bpy.ops.transform.rotate(value=-1.5708 * side, orient_axis='Z', orient_type='GLOBAL')
        bpy.ops.transform.translate(value=(0.0, 0.0, 2.0 * cFloor), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        if turned == True:
            advancement += 1.0
            if opened == True and closed == False:
                colOut = 2.0
            else:
                colOut = 0.0
        else:
            advancement += 2.0
            i += 1
        
        if opened == True:
            fromLast += 1
        
        
    return plane.name

# Generate a building floor with 4 sides                                                             
def generateBuildingFloor(cFloor, colX, colY, size):
    side = 0
    while side < 4:
        if side % 2 == 0:
            lastModName = generateBuildingFacade(side, colX, colY, cFloor, size)
        else:
            lastModName = generateBuildingFacade(side, colY, colX, cFloor, size)
        side += 1
    
    return lastModName

# Generate the building
def generateBuildingStructure(floor, colX, colY, size):
   
    # Generate all building floors
    currFloor = 0
    while currFloor < floor:
        # Generate one floor
        lastModName = generateBuildingFloor(currFloor, colX, colY, size)
        currFloor += 1
    
    # Select all module objects
    collection = bpy.data.collections.get('Building')
    
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
    
    bpy.ops.mesh.remove_doubles(threshold=0.02)
    
    bpy.ops.mesh.select_all( action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'OBJECT')    


def generateBuildingRandomly(floor, colX, colY, size):
    currFloor = 0
    while currFloor < floor:
        # Generate one floor
        lastModName = generateBuildingFloor(currFloor, colX, colY, size)
        currFloor += 1     

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