import bpy, bmesh

import mathutils 
from mathutils import Vector 

def selectMeshByIndex(obj, idx):
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    bm.faces[idx].select_set(True)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

def CenterOrigin():
    bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL')
    
    #put cursor at origin 
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

