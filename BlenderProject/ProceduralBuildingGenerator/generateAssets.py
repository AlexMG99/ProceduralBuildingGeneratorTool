import bpy, bmesh
import random

from pbg import utilities
from pbg import material

import imp
imp.reload(utilities)
imp.reload(material)

# Generate the window
def generateWindow(obj, windowSize, windowType):
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
    bpy.ops.mesh.inset(thickness=bpy.context.scene.buildingParameters.windowFrame, depth=0)
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
                                                             TRANSFORM_OT_translate={"value":(0, 0, 0.25)})
    bpy.ops.mesh.select_all(action = 'DESELECT')                                                         
    
    # Generate window
    utilities.selectFaceByIndex(obj, 17)
    if windowType == "Cross":
        generateOneWindow(obj)
    elif windowType == "Vertical":
        generateTwoWindows(obj, windowSize)


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
                                    
                
    
def generateTwoWindows(obj, windowSize):
    bpy.ops.transform.resize(value=(1.1, 0.6, 1.1), orient_type ='GLOBAL')
    bpy.ops.transform.translate(value=(0, -0.4 * windowSize + 0.05, 0.25), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    
    utilities.deselectFaceByIndex(obj, 13)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.1)})
    
    # Set crystal material
    material.addMaterialBase(obj, "Glass")
    
    # Duplicate window
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    
    windowOpen = random.uniform(0.1 * windowSize, windowSize * 0.6)
    bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, windowOpen, - 0.12), "orient_type":'GLOBAL'})

# Create simple door    
def generateDoor(obj):
    # Go to edit mode, edge selection modes
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    utilities.selectFaceByIndex(obj, 6)
    
    # Set crystal material
    material.addMaterialBase(obj, "Frame Door")
    
    bpy.ops.mesh.duplicate()
    
    bpy.ops.transform.translate(value=(0, 0.0, 0.27), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=bpy.context.scene.buildingParameters.doorFrame, depth=0)
    
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
    material.addMaterialBase(obj, "Glass Door")
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.1)})
    
    # Set bottom material
    bpy.ops.mesh.select_all(action = 'DESELECT')
    utilities.selectFaceByIndex(obj, 15)
    material.addMaterialBase(obj, "Bottom")

# Create balconyw window   
def generateBalconyWindow(obj, windowSize):
   # Go to edit mode, edge selection modes
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    utilities.selectFaceByIndex(obj, 6)
    
    # Set bottom material
    material.addMaterialBase(obj, "Bottom")
    
    bpy.ops.mesh.duplicate()
    
    # Set frame material
    material.addMaterialBase(obj, "Frame")
    
    # Generate window frame
    bpy.ops.mesh.inset(thickness=bpy.context.scene.buildingParameters.windowFrame, depth=0)
    bpy.ops.mesh.inset(thickness=0.02, depth=0)
    
    bpy.ops.mesh.select_more()
    utilities.deselectFaceByIndex(obj, 10)
    
    bpy.ops.mesh.delete(type='FACE')
    
    # Extrude frame
    it = 11
    while it < 15:
        utilities.selectFaceByIndex(obj, it)
        it += 1
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, 0.25)})
    bpy.ops.mesh.select_all(action = 'DESELECT')                                                       
    
    # Generate window
    utilities.selectFaceByIndex(obj, 10)
    generateWindowHorizontal(obj, windowSize)
    
def generateWindowHorizontal(obj, windowSize):
    bpy.ops.transform.resize(value=(0.5, 1.05, 1.1), orient_type ='GLOBAL')
    bpy.ops.transform.translate(value=(0.4, 0, 0.25), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    
    utilities.deselectFaceByIndex(obj, 13)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.1)})
    
    # Set crystal material
    material.addMaterialBase(obj, "Glass")
    
    # Duplicate window
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    
    windowOpen = random.uniform(0.5 * windowSize, windowSize * 0.8)
    bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(-windowOpen, 0.0, - 0.12), "orient_type":'GLOBAL'})