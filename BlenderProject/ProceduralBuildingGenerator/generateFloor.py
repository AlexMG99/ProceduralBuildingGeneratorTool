import bpy

import random
from mathutils import Vector

# Import rules fuinctions
from pbg import generateModules
from pbg import generateFacade
from pbg import parameters

# Reload module
import imp
imp.reload(parameters)
imp.reload(generateModules)
imp.reload(generateFacade)


# Generate a building floor with 4 sides                                                             
def generateBuildingFloor(cFloor, colX, colY, size, buildingPlant):
    side = 0
    buildingStreet = bpy.context.scene.buildingParameters.buildingStreet
    
    if buildingStreet == "Solo":
        while side < 4:
            if side % 2 == 0:
                lastModName, buildingPlant = generateFacade.generateBuildingFacade(side, colX, colY, cFloor, size, buildingPlant)
            else:
                lastModName, buildingPlant = generateFacade.generateBuildingFacade(side, colY, colX, cFloor, size, buildingPlant)
            side += 1
            
    elif buildingStreet == "Middle":
        while side < 4:
            if side % 2 == 0:
                lastModName , buildingPlant = generateFacade.generateBuildingFacade(side, colX, colY, cFloor, size, buildingPlant)
            else:
                lastModName = generateFacade.generateBuildingFacadeFlat(side, colY, colX, cFloor, size)
            side += 1
            
    elif buildingStreet == "Corner":
        while side < 4:
            if side % 2 == 0:
                if side == 0:
                    lastModName = generateFacade.generateBuildingFacadeFlat(side, colX, colY, cFloor, size)
                else:
                    lastModName, buildingPlant = generateFacade.generateBuildingFacade(side, colX, colY, cFloor, size, buildingPlant)
            else:
                if side == 1:
                    lastModName = generateFacade.generateBuildingFacadeFlat(side, colY, colX, cFloor, size)
                else:
                    lastModName , buildingPlant = generateFacade.generateBuildingFacade(side, colX, colY, cFloor, size, buildingPlant)
            side += 1
    
    # print(buildingPlant)
    
    return lastModName, buildingPlant

# Generate a building floor with 4 sides from the previous structure
def generateBuildingFloorFromPrevious(cFloor, colX, colY, size, buildingPlant, floor):
    side = 0
    buildingStreet = bpy.context.scene.buildingParameters.buildingStreet
    
    if buildingStreet == "Solo":
        while side < 4:
            if side % 2 == 0:
                lastModName, buildingPlant = generateFacade.generateBuildingFacadeFromPrevious(side, colX, colY, cFloor, size, buildingPlant, floor)
            else:
                lastModName, buildingPlant = generateFacade.generateBuildingFacadeFromPrevious(side, colY, colX, cFloor, size, buildingPlant, floor)
            side += 1
            
    elif buildingStreet == "Middle":
        while side < 4:
            if side % 2 == 0:
                lastModName, buildingPlant = generateFacade.generateBuildingFacadeFromPrevious(side, colY, colX, cFloor, size, buildingPlant, floor)
            else:
                lastModName = generateFacade.generateBuildingFacadeFlat(side, colY, colX, cFloor, size)
            side += 1
            
    elif buildingStreet == "Corner":
        while side < 4:
            if side % 2 == 0:
                if side == 0:
                    lastModName = generateFacade.generateBuildingFacadeFlat(side, colX, colY, cFloor, size)
                else:
                    lastModName, buildingPlant = generateFacade.generateBuildingFacadeFromPrevious(side, colY, colX, cFloor, size, buildingPlant, floor)
            else:
                if side == 1:
                    lastModName = generateFacade.generateBuildingFacadeFlat(side, colY, colX, cFloor, size)
                else:
                    lastModName, buildingPlant = generateFacade.generateBuildingFacadeFromPrevious(side, colY, colX, cFloor, size, buildingPlant, floor)
            side += 1
         
    if cFloor == (floor - 1):
        side = 0
        while side < 4:                
            # Generate upper roof 
            if side % 2 == 0:
                lastModName = generateFacade.generateUpperModuleRoof(side, cFloor, colX, colY, size, buildingPlant, lastModName)
            else:
                lastModName = generateFacade.generateUpperModuleRoof(side, cFloor, colY, colX, size, buildingPlant, lastModName)
            
            side += 1
        
    return lastModName

# Generate a roof for the building                                                         
def generateBuildingRoof(floor, colX, colY, size):
    
    # Generate a new plane
    bpy.ops.mesh.primitive_plane_add()
    bpy.ops.transform.resize(value=(colX * size[1], colY * size[0], 1.0))
    bpy.ops.transform.translate(value=(colX * size[0] - 1, -colY * size[0], 2.0 * floor - size[1]), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
    
    plane = bpy.context.selected_objects[0]
    bpy.ops.object.editmode_toggle()
    
    generateModules.generateRoofModule(plane)
    
    return plane.name

# Duplicate previous building floor                                                             
def duplicateBuildingFloor(cFloor, floor, name):
    # Select all module objects
    collection = bpy.data.collections.get('Building')
    bpy.ops.object.mode_set( mode = 'OBJECT')
    
    i = 0
    for obj in collection.objects:
        if(i >= cFloor - 1):
            lastModName = obj.select_set(True)
        i += 1
    
    bpy.ops.object.mode_set( mode = 'OBJECT')
    
    bpy.ops.object.join()
    bpy.ops.object.editmode_toggle()
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'OBJECT')
    
    endFloor = 0
    while endFloor < floor - 1:
        bpy.ops.object.duplicate_move()
        bpy.ops.transform.translate(value=(0.0, 0.0, 2.0 * cFloor), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
    
        endFloor += 1
        
    return bpy.context.active_object.name, endFloor