import bpy  
from bpy.types import Operator  
from bpy.props import FloatVectorProperty, FloatProperty, IntProperty  
  
class ScaleOperator(bpy.types.Operator):  
 """Scale Operator"""  
 bl_idname = "object.scale_operator"  
 bl_label = "Scale Operator"  
 bl_options = {'REGISTER', 'UNDO'}  
  
 scale = FloatVectorProperty(  
   name="Scale",  
   default=(1.0, 1.0, 1.0),  
   subtype='XYZ',  
   description="Scale the building floor size"  
   )  
   
 floorNum = IntProperty(  
   name="Floor Number",  
   default=1.0,  
   subtype='DISTANCE',  
   unit='LENGTH',  
   description="Choose the number of floors the building will have"  
   )  
  
 def execute(self, context):  
  scale = self.scale
  context.active_object.scale *= scale
  return {'FINISHED'}  
  
 @classmethod  
 def poll(cls, context):  
  ob = context.active_object  
  return ob is not None and ob.mode == 'OBJECT'  
  
def add_object_button(self, context):  
 self.layout.operator(  
  Move3Operator.bl_idname,  
  text= "Hola",  
  icon='PLUGIN')  
  
def register():  
 bpy.utils.register_class(ScaleOperator)  
 bpy.types.VIEW3D_MT_object.append(add_object_button)  
  
if __name__ == "__main__":  
 register()  