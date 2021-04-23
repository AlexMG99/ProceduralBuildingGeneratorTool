import bpy, bmesh
import random

from pbg import utilities

import imp
imp.reload(utilities)

# Generate module window
def generateModuleWindow(obj):
    
    bpy.data.objects[obj.name].select_set(True)
    obj.rotation_mode = 'XYZ'
    obj.rotation_euler = (0,0,0)
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Cut in half the planes
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.5, offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.75, offset_pct=0, affect='EDGES')
    
    # Here we have created the window frame
    
    # Deselect all and select middle face
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectMeshByIndex(obj, 6)
    
    # Inset window frame
    bpy.ops.mesh.inset(thickness=0.2, depth=0)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.2)})
                                                             
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')
    
# Generate one building side                                                             
def generateBuildingSide(size, side, colX, colY, cFloor):
    i = 0
    while i < colX:
        # Generate a new cube
        bpy.ops.mesh.primitive_plane_add(scale=(size[0], size[1], size[2]))
    
        # Get created cube
        plane = bpy.context.selected_objects[0]
        plane.name = "Module " + str(side) + "." + str(i)
        
        # Generate Module and move
        rand = random.randint(0,1)
        if rand == 0:
            generateModuleWindow(plane)
        else:
            bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')
            
        bpy.data.objects[plane.name].select_set(True)
        
        if side == 0:
            bpy.ops.transform.translate(value=(2.0 * i, 0.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 1:
            bpy.ops.transform.translate(value=(2.0 * (colY - 1) + 1.0 , - 2.0 * i - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 2:
            bpy.ops.transform.translate(value=(2.0 * (colX - 1) - 2.0 * i, - 2.0 * colY, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        elif side == 3:
            bpy.ops.transform.translate(value=(-1.0, - 2.0 * (colX - 1) + 2.0 * i - 1.0, 0.0), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        bpy.ops.transform.rotate(value=-1.5708 * side, orient_axis='Z', orient_type='GLOBAL')
        bpy.ops.transform.translate(value=(0.0, 0.0, 2.0 * cFloor), orient_type='GLOBAL', orient_matrix_type='GLOBAL', mirror=True)
        
        i += 1
        
    return plane.name

# Generate a building floor with 4 sides                                                             
def generateBuildingFloor(cFloor, colX, colY, size):
    side = 0
    while side < 4:
        if side % 2 == 0:
            lastModName = generateBuildingSide(size, side, colX, colY, cFloor)
        else:
            lastModName = generateBuildingSide(size, side, colY, colX, cFloor)
        side += 1
    
    return lastModName

# Generate the building
def generateBuilding(floor, colX, colY, size):
    currFloor = 0
    while currFloor < floor:
        # Generate one floor
        lastModName = generateBuildingFloor(currFloor, colX, colY, size)
        # bpy.data.objects["Floor " + str(currFloor)].location = (0,0,20.0 * currFloor)
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