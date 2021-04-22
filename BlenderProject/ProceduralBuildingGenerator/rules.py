import bpy, bmesh

def splitMesh(obj, numCuts, edgeIndex):
    
    bpy.data.objects[obj.name].select_set(True)
    
    # Go to edit mode, face selection mode
    bpy.ops.object.mode_set( mode = 'EDIT' )
    bpy.ops.mesh.select_mode( type = 'FACE' )
    bpy.ops.mesh.select_all( action = 'SELECT' )
    
    bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":numCuts, 
                                                "smoothness":0, 
                                                "falloff":'INVERSE_SQUARE', 
                                                "object_index":0, 
                                                "edge_index":edgeIndex, 
                                                "mesh_select_mode_init":(False, False, True)}, 
                                                TRANSFORM_OT_edge_slide={"value":0.0,
                                                "use_clamp":True, 
                                                "mirror":True, 
                                                "correct_uv":True})
    
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.mode_set( mode = 'OBJECT' ) 
                                                            


    
