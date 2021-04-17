import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  
  
class ScaleOperator(bpy.types.Operator):  
 """Scale Operator"""  
 bl_idname = "object.scale_operator"  
 bl_label = "Floor Scale"  
 bl_space_type = 'VIEW_3D'
 bl_region_type = 'UI'
 bl_options = {'REGISTER', 'UNDO'}  
  
 scale = FloatVectorProperty(  
   name="Scale",  
   default=(1.0, 1.0, 1.0),  
   subtype='XYZ',  
   description="Scale the building floor size"  
   )  
   
 floorNum = IntProperty(  
   name="Floor Number",  
   default = 1,  
   subtype='UNSIGNED',  
   unit='LENGTH',  
   description="Choose the number of floors the building will have"  
   )

 def execute(self, context):  
  scale = self.scale
  context.active_object.scale = scale
  return {'FINISHED'}  
  
 @classmethod  
 def poll(cls, context):  
  ob = context.active_object  
  return ob is not None and ob.mode == 'OBJECT'  