import bpy, bmesh

import mathutils 
from mathutils import Vector 

from pbg import parameters
from pbg import material

# Reload module
import imp
imp.reload(parameters)
imp.reload(material)


# Select object edge by index operator
class SelectFace(bpy.types.Operator):
    bl_label = "Select face by number"
    bl_idname = "pbg.selectface"
    
    def execute(self, context):
        bpy.data.objects[bpy.context.scene.utilitiesParameters.objName].select_set(True)
        obj = bpy.context.selected_objects[0]
    
        selectFaceByIndex(obj, bpy.context.scene.utilitiesParameters.edgeIdx)
        
        return{'FINISHED'}


# Select object face by index
def selectFaceByIndex(obj, idx):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    bm.faces[idx].select_set(True)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

# Select object face by index
def selectFacesByIndex(obj, idx):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    bpy.ops.mesh.select_all(action = 'DESELECT') 
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    it = 0
    while it < len(idx):
        bm.faces[idx[it]].select_set(True)  # select index
        it += 1

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)
    
# Select object face by index
def deselectFaceByIndex(obj, idx):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'FACE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    bm.faces[idx].select_set(False)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)


# Select object edge by index operator
class SelectEdge(bpy.types.Operator):
    bl_label = "Select Edge by number"
    bl_idname = "pbg.selectedge"
    
    def execute(self, context):
        selectEdgeByIdx(bpy.context.scene.utilitiesParameters.objName, bpy.context.scene.utilitiesParameters.edgeIdx)
        
        return{'FINISHED'}

def selectEdgesByIndex(name, idx):
    
    bpy.data.objects[name].select_set(True)
    obj = bpy.context.selected_objects[0]
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    
    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    it = 0
    while it < len(idx):
        bm.edges[idx[it]].select_set(True)  # select index
        it += 1

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

def selectEdgeByIdx(name, idx):
    
    bpy.data.objects[name].select_set(True)
    obj = bpy.context.selected_objects[0]
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called edge
    bm.edges.ensure_lookup_table()
    bm.edges[idx].select_set(True)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)


# Select object edge by index operator
class ResizeObject(bpy.types.Operator):
    bl_label = "Resize Object"
    bl_idname = "pbg.resizeobject"
    
    def execute(self, context):
        obj = bpy.data.collections.get("Building").objects[0]
    
        resizeObject(obj, bpy.context.scene.buildingParameters.buildingScale)
        
        return{'FINISHED'}


# Select object face by index
def resizeObject(obj, scale):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_all(action = 'SELECT') 
    
    bpy.ops.transform.scale = scale

    bpy.ops.object.mode_set( mode = 'OBJECT')
    
    
# Generate Materials to all the objects
class GenerateMaterials(bpy.types.Operator):
    bl_label = "Generate materials"
    bl_idname = "pbg.generatematerials"
    
    def execute(self, context):
        generateMaterials()
        
        return{'FINISHED'}

def generateMaterials():
    
    # Generate Plane
    bpy.ops.mesh.primitive_plane_add()
    plane = bpy.context.selected_objects[0]
    
    # Add material
    material.addMaterial(plane, "Glass")
    material.addMaterial(plane, "Glass Door")
    material.addMaterial(plane, "Frame Door")
    material.addMaterial(plane, "Frame")
    material.addMaterial(plane, "Bottom")
    material.addMaterial(plane, "Brick")
    material.addMaterial(plane, "Roof")
    material.addMaterialBase(plane, "Wall 1")
    
    
    
# Class Inizialization
def register():
    bpy.utils.register_class(SelectEdge)
    bpy.utils.register_class(SelectFace)
    bpy.utils.register_class(ResizeObject)
    bpy.utils.register_class(GenerateMaterials)


def unregister():
    bpy.utils.unregister_class(SelectEdge)
    bpy.utils.unregister_class(SelectFace)
    bpy.utils.unregister_class(ResizeObject)
    bpy.utils.unregister_class(GenerateMaterials)

if __name__ == "__main__":
    register()