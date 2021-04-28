import bpy, bmesh
import random

from pbg import utilities
from pbg import material

import imp
imp.reload(utilities)
imp.reload(material)

# Generate module window
def generateModuleWindow(obj, windowSize):
    
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
    size = random.randint(0,1)
    if windowSize[0] == 0.5:
        windowType = 1  
    else:
        windowType = 0
        
    generateWindow(obj, windowType)
    
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
    generateDoor(obj)
    
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


# Generate the window
def generateWindow(obj, windowType):
    # Go to edit mode, edge selection modes
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    utilities.selectFaceByIndex(obj, 13)
    
    # Set bottom material
    material.addMaterialBase(obj, "Bottom")
    
    bpy.ops.mesh.duplicate()
    
    # Set frame material
    material.addMaterialBase(obj, "Frame")
    
    # Generate window frame
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    bpy.ops.mesh.inset(thickness=0.02, depth=0)
    
    bpy.ops.mesh.select_more()
    utilities.deselectFaceByIndex(obj, 17)
    
    bpy.ops.mesh.delete(type='FACE')
    
    # Extrude frame
    it = 18
    while it < 22:
        utilities.selectFaceByIndex(obj, it)
        it += 1
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, 0.2)})
    bpy.ops.mesh.select_all(action = 'DESELECT')                                                         
    
    # Generate window
    utilities.selectFaceByIndex(obj, 17)
    if windowType == 0:
        generateOneWindow(obj)
    elif windowType == 1:
        generateTwoWindows(obj)


def generateOneWindow(obj):
    bpy.ops.transform.translate(value=(0, 0.0 , 0.15), orient_type ='GLOBAL')
    
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":54, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.06, offset_pct=0, affect='EDGES')
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":52, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
                                            
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.06, offset_pct=0, affect='EDGES')
    
    # Glass creation
    idx = [17, 36, 37, 41]
    utilities.selectFacesByIndex(obj, idx)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.07)})
    
    # Frame Material                                                         
    bpy.ops.mesh.select_more()
    material.addMaterialBase(obj, "Frame")      
    
    # Glass material
    idx = [37, 43, 44, 45]
    utilities.selectFacesByIndex(obj, idx)
    material.addMaterialBase(obj, "Glass")
    
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    bpy.ops.transform.resize(value=(1.1, 1.1, 1.1), orient_type='GLOBAL')
                                    
                
    
def generateTwoWindows(obj):
    bpy.ops.transform.resize(value=(1.1, 0.5, 1.1), orient_type ='GLOBAL')
    bpy.ops.transform.translate(value=(0, -0.27, 0.15), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    
    utilities.deselectFaceByIndex(obj, 13)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.05)})
    
    # Set crystal material
    material.addMaterialBase(obj, "Glass")
    
    # Duplicate window
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    
    windowOpen = random.uniform(0.1, 0.5)
    bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, windowOpen, - 0.07), "orient_type":'GLOBAL'})
    
def generateDoor(obj):
    # Go to edit mode, edge selection modes
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    utilities.selectFaceByIndex(obj, 6)
    
    # Set bottom material
    material.addMaterialBase(obj, "Bottom")
    
    bpy.ops.mesh.duplicate()
    
    # Create door frame
    material.addMaterialBase(obj, "Frame")
    
    bpy.ops.transform.translate(value=(0, 0.0, 0.27), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.12)})
    
    # Create door
    bpy.ops.mesh.duplicate()
    
    bpy.ops.transform.translate(value=(0, 0.0, 0.13), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.04, depth=0)

    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":46, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    bpy.ops.mesh.bevel(offset=0.055, offset_pct=0, affect='EDGES')
    
    # Glass material
    idx = [24,29]
    utilities.selectFacesByIndex(obj, idx)
    material.addMaterialBase(obj, "Glass")
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.1)})
