import bpy, bmesh

def selectMeshByIndex(obj, idx):
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called faces
    bm.faces.ensure_lookup_table()
    bm.faces[idx].select_set(True)  # select index

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)