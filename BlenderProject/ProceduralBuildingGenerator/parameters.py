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
        name="Width:",
        description="Number of modules in X axis",
        default = 5,
        min = 0,
        max = 20
        )
        
    rowY : IntProperty(
        name="Depth:",
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
        
    twoColors : BoolProperty(
        name="Two colors",
        description="Building with two color configuration for the facade",
        default= False
        )
        
    wallTexture : BoolProperty(
        name="Building Texture",
        description="When active, the building uses a texture for the facade",
        default= False
        )
    
    windowColor : FloatVectorProperty(  
       name="Window Color",
       subtype='COLOR',
       default=(0.0, 0.0, 0.0, 1.0),
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of windows"
       )
       
    wallColor : FloatVectorProperty(  
       name="Wall Color",
       subtype='COLOR',
       default=[1.0, 1.0, 1.0, 1.0],
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the facade"
       )
       
    wallColorAux : FloatVectorProperty(  
       name="Wall Color 2",
       subtype='COLOR',
       default=(0.8, 0.8, 0.8),
       precision=2,
       size=3,
       min=0.0, max=1.0,
       description="Chose the secondary color of the facade"
       )
       
    buildingType : EnumProperty(
        name="Building Type",
        description="Choose building position",
        items= [("Symmetrical", "Symmetrical", "Symmetrical building facade", "", 0),
                ("Random", "Random", "Random building facade", "", 1),
                ("Plane", "Plane", "Plane building facade", "", 2)],
        default = "Plane")

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
