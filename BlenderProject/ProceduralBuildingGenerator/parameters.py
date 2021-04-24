import bpy

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
                       
from bpy.types import (PropertyGroup,)
                       

class UtilitiesParameters(PropertyGroup):
    edgeIdx : IntProperty(
        name="Edge Index",
        default = 0)
        
    objName : StringProperty(
        name="Object Name",
        default = "NoName")

class BuildingParameters(PropertyGroup):     
                     
    numFloor : IntProperty(
        name="Floors:",
        description="Number of floors the building will have",
        default = 1,
        min = 0,
        max = 10
        )
    
    rowX : IntProperty(
        name="X:",
        description="Number of modules in X axis",
        default = 5,
        min = 0,
        max = 20
        )
        
    rowY : IntProperty(
        name="Y:",
        description="Number of modules in Y axis",
        default = 5,
        min = 0,
        max = 20
        )
    
    moduleSize : FloatVectorProperty(
        name="Size",
        description="Size of the window modules",
        subtype="XYZ",
        precision=2,
        size=3,
        default=(1.0,1.0,1.0),
        min=0.0,
        max=10.0
        )

# Initialization
def register():
    bpy.utils.register_class(BuildingParameters)
    bpy.utils.register_class(UtilitiesParameters)
    bpy.types.Scene.buildingParameters = PointerProperty(name="Building parameters", type=BuildingParameters)
    bpy.types.Scene.utilitiesParameters = PointerProperty(name="Utilities parameters", type=UtilitiesParameters)


def unregister():
    bpy.utils.unregister_class(BuildingParameters)
    bpy.utils.unregister_class(UtilitiesParameters)
    del bpy.types.Scene.buildingParameters
    del bpy.types.Scene.utilitiesParameters


if __name__ == "__main__":
    register()
