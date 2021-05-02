import bpy

import random
from mathutils import Vector

# Import rules fuinctions
from pbg import generateModules
from pbg import parameters
from pbg import material

# Reload module
import imp
imp.reload(parameters)
imp.reload(generateModules)
imp.reload(material)

# Generate one building side                                                             
def generateBuildingFacade(side, colX, colY, cFloor, size, buildingPlant):
    i = 0
    turnBuilding = 0
    advancement = 0.0
    colOut = 0.0
    
    fromLast = 0
    
    opened = False
    closed = False
    
    hasDoor = False
    
    buildingParameters = bpy.context.scene.buildingParameters
    
    while i < colX:
        turned = False
        
        # Generate a new plane
        bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], 1.0))
    
        # Get created cube
        plane = bpy.context.selected_objects[0]
        plane.name = "Module " + str(side) + "." + str(i)
            
        # Generate Module and move
        """ rand = random.randint(0, 1)
        if rand == 0:
            generateModuleWindow(plane)
        else:
            generateModuleWall(plane) """
        
        # Add door
        """if cFloor == 0 and side == 0 and i == int(colX * 0.5):
            generateModules.generateModuleDoor(plane, 0.5, 0.75)
        else:"""
        
        # Random facade Generation ----------------------------------------------------------------------------------------------------- #
        # Building one module out
        if bpy.context.scene.buildingParameters.buildingType == 'Random':
            if opened == False and closed == False:
                if turnBuilding == 0 and i != 0 and i != colX - 1:
                    turnBuilding = random.randint(0, 1)

                # Module Outside
                if turnBuilding == 1:
                    advancement -= 1.0
                    bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='LOCAL')
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
                    bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='LOCAL')
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
                
        # Symmetrical facade Generation ------------------------------------------------------------------------------------------------------------------- #
        elif bpy.context.scene.buildingParameters.buildingType == 'Symmetrical':
            if opened == False and closed == False and int(i < colX * 0.5):
                if turnBuilding == 0 and i != 0 and i != colX - 1:
                    turnBuilding = random.randint(0, 1)

                # Module Outside
                if turnBuilding == 1:
                    advancement -= 1.0
                    bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='LOCAL')
                    turnBuilding = 2
                    turned = True
                    opened = True
                    fromLast = i 
                
                    if side == 0:
                        bpy.ops.transform.translate(value=(0.0, 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
                    elif side == 1:
                        bpy.ops.transform.translate(value=(1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                    elif side == 2:
                        bpy.ops.transform.translate(value=(0.0, -1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)        
                    elif side == 3:
                        bpy.ops.transform.translate(value=(-1.0, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)         

            # Module inside
            if opened == True and closed == False and (colX - fromLast) == i:         
                advancement -= 1.0
                print(str(colX - fromLast))
                bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='LOCAL')
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
        
        # -------------------------------------------------------------------------------------------------------------------------------------------------- #
        # Generate module 
        doorRand = random.randint(0, 10)
        if cFloor == 0 and side == 0 and hasDoor == False and turned == False and (doorRand == 0 or i == colX - 1):
            generateModules.generateModuleDoor(plane, buildingParameters.doorSize[0], buildingParameters.doorSize[1])
            hasDoor = True
        else:
            generateModule(plane, turned, buildingParameters)
        
        if opened == True and closed == False and turned == False:
            if side == 0:
                buildingPlant[i] = True   
            elif side == 1:
                buildingPlant[colX + i] = True    
            elif side == 2:
                buildingPlant[colY + colX + i] = True   
            elif side == 3:
                buildingPlant[colY * 2 + colX + i] = True   
        
        
        # generateModules.generateModuleWindow(plane, buildingParameters.doorSize[0], buildingParameters.doorSize[1])
        # Set module correct transformation
        bpy.data.objects[plane.name].select_set(True)  
          
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
        
        # Check next module position
        if turned == True:
            advancement += 1.0
            if opened == True and closed == False:
                colOut = 2.0
            else:
                colOut = 0.0
        else:
            advancement += 2.0
            i += 1
        
        if opened == True and bpy.context.scene.buildingParameters.buildingType == 'Random':
            fromLast += 1
        
        
    return plane.name, buildingPlant

# Generate one building side from previous                                                             
def generateBuildingFacadeFromPrevious(side, colX, colY, cFloor, size, buildingPlant, floor):
    i = 0
    turnBuilding = 0
    advancement = 0.0
    colOut = 0.0
    
    opened = False
    closed = False
    
    buildingParameters = bpy.context.scene.buildingParameters
    
    nextBuildingModule = 0
    
    while i < colX:
        turned = False
        
        # Generate a new plane
        bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], 1.0))
    
        # Get created cube
        plane = bpy.context.selected_objects[0]
        plane.name = "Module " + str(side) + "." + str(i)
        
        # Assign value to next module
        if side == 0 and i < colX:   
            nextBuildingModule = buildingPlant[i]            
        elif side == 1 and colY + colX:
            nextBuildingModule = buildingPlant[colX + i]   
        elif side == 2 and colX * 2 + colY:
            nextBuildingModule = buildingPlant[colY + colX + i]  
        elif side == 3 and colX * 2 + colY * 2:
            nextBuildingModule = buildingPlant[colY * 2 + colX + i] 
        
        # Check next buildingPlant to open or close module
        if nextBuildingModule == True and opened == False:
            advancement -= 1.0
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='LOCAL')
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
            
        elif nextBuildingModule == False and opened == True and closed == False:
            advancement -= 1.0
            bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='LOCAL')
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
        
        # Generate module 
        generateModule(plane, turned, buildingParameters)
        
        # Set module correct transformation
        bpy.data.objects[plane.name].select_set(True)  
          
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
        
        # Check next module position
        if turned == True:
            advancement += 1.0
            if opened == True and closed == False:
                colOut = 2.0
            else:
                colOut = 0.0
        else:
            advancement += 2.0
            i += 1
        
    return plane.name, buildingPlant

def generateBuildingFacadeFlat( side, colX, colY, cFloor, size):
    i = 0
    advancement = 0.0
    
    buildingParameters = bpy.context.scene.buildingParameters
    
    while i < colX:
        turned = False;
        
        # Generate a new plane
        bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], 1.0))
    
        # Get created cube
        plane = bpy.context.selected_objects[0]
        plane.name = "Module " + str(side) + "." + str(i)
        generateModules.generateModuleWall(plane) 
        
        # Set module correct transformation
        bpy.data.objects[plane.name].select_set(True)  
          
        # Move to building position   
        if side == 0:
            bpy.ops.transform.translate(value=(advancement, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 1:
            bpy.ops.transform.translate(value=(2.0 * (colY - 1) + 1.0 , - advancement - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 2:
            bpy.ops.transform.translate(value=(2.0 * (colX - 1) - advancement, - 2.0 * colY, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 3:
            bpy.ops.transform.translate(value=(- 1.0, - 2.0 * (colX - 1) + advancement - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        bpy.ops.transform.rotate(value=-1.5708 * side, orient_axis='Z', orient_type='GLOBAL')
        bpy.ops.transform.translate(value=(0.0, 0.0, 2.0 * cFloor), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        advancement += 2.0
        i += 1
        
    return plane.name

def generateModule(plane, turned, buildingParameters):
    if turned == True:
        generateModules.generateModuleWall(plane)
    else:
        generateModules.generateModuleWindow(plane, Vector((buildingParameters.windowSize[0], buildingParameters.windowSize[1])), buildingParameters.windowType)


def generateUpperModuleRoof(side, cFloor, colX, colY, size, buildingPlant, name):
    advancement = 0
    i = 0
    nextBuildingModule = 0
    retName = name
    
    while i < colX:
        # Assign value to next module
        if side == 0 and i < colX:   
            nextBuildingModule = buildingPlant[i]            
        elif side == 1 and colY + colX:
            nextBuildingModule = buildingPlant[colX + i]   
        elif side == 2 and colX * 2 + colY:
            nextBuildingModule = buildingPlant[colY + colX + i]  
        elif side == 3 and colX * 2 + colY * 2:
            nextBuildingModule = buildingPlant[colY * 2 + colX + i]
        
        if nextBuildingModule == True:    
        # Generate a new plane
            bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], 1.0))
            
            # Get created cube
            plane = bpy.context.selected_objects[0]
            plane.name = "Module Roof" + str(side) + "." + str(i)
            
            material.addMaterial(plane, "Roof")
            
            retName = plane.name
        
            # Move to building position   
            if side == 0:
                bpy.ops.transform.translate(value=(advancement, 1.0, 2.0 * cFloor + size[1]), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
            elif side == 1:
                bpy.ops.transform.translate(value=(2.0 * (colY - 1) + 2.0 , - advancement - 1.0, 2.0 * cFloor + size[1]), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
            elif side == 2:
                bpy.ops.transform.translate(value=(2.0 * (colX - 1) - advancement, - 2.0 * colY - 1.0, 2.0 * cFloor + size[1]), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
            elif side == 3:
                bpy.ops.transform.translate(value=(-2.0, - 2.0 * (colX - 1) + advancement - 1.0, 2.0 * cFloor + size[1]), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        advancement += 2.0
        i += 1
        
    return retName    