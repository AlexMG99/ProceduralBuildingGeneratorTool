import bpy

def addMaterial(obj, name):
    
    # Select object 
    bpy.data.objects[obj.name].select_set(True)
    
    # Create new material
    bpy.ops.material.new()
    bpy.context.object.active_material_index = 0
    bpy.context.object.active_material.name = "Wall"
