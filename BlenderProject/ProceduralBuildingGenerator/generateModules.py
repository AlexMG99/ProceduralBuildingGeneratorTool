import bpy, bmesh
import random

from pbg import utilities
from pbg import material
from pbg import generateAssets

import imp
imp.reload(utilities)
imp.reload(material)
imp.reload(generateAssets)

# Generate module window
def generateModuleWindow(obj, windowSize, windowType):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Generate the window frame ----------------------------------------------------------------------------- #
    
    # Cut window in two
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=windowSize[0], offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=windowSize[1], offset_pct=0, affect='EDGES')
    
    # Deselect all and select middle face
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectFaceByIndex(obj, 6)
    
    # Inset window frame
    bpy.ops.mesh.inset(thickness=0.2, depth=0)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.2)})
    
    # Generate UVS and add material to object
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [1, 4, 10, 15]
    material.generateUVS(obj, idx)
    material.addMaterial(obj, "Wall")
    
    # ------------------------------------------------------------------------------------------------------ #
                                                         
    # Generate Window
    generateAssets.generateWindow(obj, windowSize[1], windowType)
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')
                                             


# Generate door module
def generateModuleDoor(obj, doorWidth, doorHeight):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Go to edit mode, face selection modes
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    # Generate the window frame ----------------------------------------------------------------------------- #
    
    # Cut window in two
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=doorWidth, offset_pct=0, affect='EDGES')
    
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":1, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":doorHeight})
                                                
    
    # Deselect all and select middle face
    bpy.ops.mesh.select_all( action = 'DESELECT' )
    utilities.selectFaceByIndex(obj, 2)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.25)})
    
    # Generate UVS and add material to object
    bpy.ops.mesh.select_all(action = 'DESELECT') #Deselecting all
    idx = [1,8,9,15]
    material.generateUVS(obj, idx)
    material.addMaterial(obj, "Wall")
    
    # ------------------------------------------------------------------------------------------------------ #
                                                         
    # Generate Window
    generateAssets.generateDoor(obj)
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')
    
# Generate module wall
def generateModuleWall(obj):
    bpy.data.objects[obj.name].select_set(True)
    material.addMaterial(obj, "Wall")
    
    # Rotate building 90 degrees to align it with the building
    bpy.ops.object.mode_set( mode = 'OBJECT' )
    bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL')

# Create simple door    
def generateRoofModule(obj):
    material.addMaterial(obj, "Roof")
    
    # Inset window frame
    bpy.ops.mesh.inset(thickness=0.06, depth=0)

    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.5)})
    
    idx = [0,1,2,3,16,17,18,19]
    material.generateUVS(obj, idx)
