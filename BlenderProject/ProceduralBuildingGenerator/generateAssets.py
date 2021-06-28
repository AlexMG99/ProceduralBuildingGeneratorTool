import bpy, bmesh
import random

from . import utilities
from . import material


# Generate the window
def generateWindow(obj, windowHeight, windowType):
    # Go to edit mode, edge selection modes
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    utilities.selectFaceByIndex(obj, 4)
    
    # Set bottom material
    material.addMaterialBase(obj, "Bottom")
    
    bpy.ops.mesh.duplicate()
    
    # Set frame material
    material.addMaterialBase(obj, "Frame")
    
    # Generate window frame
    bpy.ops.mesh.inset(thickness=bpy.context.scene.buildingParameters.windowFrame, depth=0)
    bpy.ops.mesh.inset(thickness=0.0000001, depth=0)
    
    bpy.ops.mesh.select_more()
    utilities.deselectFaceByIndex(obj, 13)
    
    bpy.ops.mesh.delete(type='FACE')
    
    # Extrude frame
    it = 14
    while it < 18:
        utilities.selectFaceByIndex(obj, it)
        it += 1
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, 0.25)})
    bpy.ops.mesh.select_all(action = 'DESELECT')                                                         
    
    # Generate window
    utilities.selectFaceByIndex(obj, 13)
    if windowType == "Cross":
        generateOneWindow(obj)
    elif windowType == "Vertical":
        generateWindowVertical(obj, windowHeight)


def generateOneWindow(obj):
    bpy.ops.transform.translate(value=(0, 0.0 , 0.15), orient_type ='GLOBAL')
    
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":47, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
    
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.06, offset_pct=0, affect='EDGES')
    
    # Cut in half the plane
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":67, 
                                                "mesh_select_mode_init":(False, True, False)}, 
                                                TRANSFORM_OT_edge_slide={"value":0})
                                            
    # Apply bevel                                            
    bpy.ops.mesh.bevel(offset=0.06, offset_pct=0, affect='EDGES')
    
    # Glass creation
    idx = [13, 32, 33, 37]
    utilities.selectFacesByIndex(obj, idx)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.07)})
    
    # Frame Material                                                         
    bpy.ops.mesh.select_more()
    material.addMaterialBase(obj, "Frame")      
    
    # Glass material
    idx = [33, 39, 40, 41]
    utilities.selectFacesByIndex(obj, idx)
    material.addMaterialBase(obj, "Glass")
    
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    bpy.ops.transform.resize(value=(1.1, 1.1, 1.1), orient_type='GLOBAL')
                                    
                
    
def generateWindowVertical(obj, windowHeight):
    windowFrame = bpy.context.scene.buildingParameters.windowFrame
    bpy.ops.transform.resize(value=(1.0 , 0.5, 1.0), orient_type ='GLOBAL')
    bpy.ops.transform.translate(value=(0, -(windowHeight - windowFrame)* 0.5, 0.25), orient_type ='GLOBAL')
    
    bpy.ops.mesh.inset(thickness=0.05, depth=0)
    
    utilities.deselectFaceByIndex(obj, 9)
    
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, 
                                                             "use_dissolve_ortho_edges":False, 
                                                             "mirror":False}, 
                                                             TRANSFORM_OT_translate={"value":(0, 0, -0.1)})
    
    # Set crystal material
    material.addMaterialBase(obj, "Glass")
    
    # Duplicate window
    bpy.ops.mesh.select_more()
    bpy.ops.mesh.select_more()
    
    windowOpen = random.uniform(0.25 * windowHeight, windowHeight * 0.5)
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
    bpy.ops.mesh.inset(thickness=bpy.context.scene.buildingParameters.balconyFrame, depth=0)
    bpy.ops.mesh.inset(thickness=0.0000001, depth=0)
    
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
    balconyFrame = bpy.context.scene.buildingParameters.balconyFrame
    bpy.ops.transform.resize(value=(0.5 , 1.0, 1.0), orient_type ='GLOBAL')
    bpy.ops.transform.translate(value=((windowSize - balconyFrame)* 0.5 , 0, 0.25), orient_type ='GLOBAL')
    
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
    
    windowOpen = random.uniform(0.25 * windowSize, windowSize * 0.5)
    bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(-windowOpen, 0.0, - 0.12), "orient_type":'GLOBAL'})
    