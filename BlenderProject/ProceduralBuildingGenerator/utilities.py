import bpy, bmesh

import mathutils 
from mathutils import Vector 

from pbg import parameters

# Reload module
import imp
imp.reload(parameters)

# Select object face by index
def selectMeshByIndex(obj, idx):
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    bm.faces[idx].select_set(True)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

# Select object edge by index operator
class SelectEdge(bpy.types.Operator):
    bl_label = "Select Edge by number"
    bl_idname = "pbg.selectedge"
    
    def execute(self, context):
        selectEdgeByIdx(bpy.context.scene.utilitiesParameters.objName, bpy.context.scene.utilitiesParameters.edgeIdx, self, context)
        
        return{'FINISHED'}

def selectEdgeByIdx(name, idx, self, context):
    
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


# Class Inizialization
def register():
    bpy.utils.register_class(SelectEdge)


def unregister():
    bpy.utils.unregister_class(SelectEdge)


if __name__ == "__main__":
    register()