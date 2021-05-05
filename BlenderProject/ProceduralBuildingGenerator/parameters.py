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
        
    buildingScale : FloatVectorProperty(
        name="Building Scale",
        description="Scale of the building",
        subtype="XYZ",
        precision=2,
        size=3,
        default=(1.0,1.0, 1.0),
        min=0.0,
        max=20.0
        )
        
    rowY : IntProperty(
        name="Depth:",
        description="Number of modules in Y axis",
        default = 5,
        min = 0,
        max = 20
        )
        
    randomnessBuilding : IntProperty(
        name="Randomness:",
        description="The higher the randomness, the higher differences between floors",
        default = 1,
        min = 0,
        max = 5
        )
    
    doorFrame : FloatProperty(
        name="Door width",
        description="Width of the window frame",
        default = 0.15,
        min = 0.01,
        max = 0.15
        )
    
    doorSize : FloatVectorProperty(
        name="Door size",
        description="Size of the door",
        subtype="XYZ",
        precision=2,
        size=2,
        default=(1.0,1.0),
        min=0.45,
        max=0.75
        )
    
    windowFrame : FloatProperty(
        name="Frame width",
        description="Width of the window frame",
        default = 0.1,
        min = 0.05,
        max = 0.1
        )
        
    windowSize : FloatVectorProperty(
        name="Window size",
        description="Size of the window",
        subtype="XYZ",
        precision=2,
        size=2,
        default=(1.0,1.0),
        min=0.5,
        max=1.0
        )
        
    balconyOuterSize : FloatVectorProperty(
        name="Balcony outer size",
        description="Size of the balcony outer construction",
        subtype="XYZ",
        precision=2,
        size=3,
        default=(1.0,1.0,1.0),
        min=0.5,
        max=1.0
        ) 
    
    balconyFrame : FloatProperty(
        name="Frame width",
        description="Width of the balcony frame",
        default = 0.1,
        min = 0.05,
        max = 0.1
        )
    
    balconySize : FloatVectorProperty(
        name="Balcony size",
        description="Size of the balcony",
        subtype="XYZ",
        precision=2,
        size=2,
        default=(1.0,1.0),
        min=0.5,
        max=1.0
        )
        
    windowType : EnumProperty(
        name="Window Type",
        description="Choose window type",
        items= [("Cross", "Cross", "", "", 0),
                ("Vertical", "Vertical", "", "", 1)],
        default = "Cross")
    
    moduleSize : FloatVectorProperty(
        name="Module size",
        description="Size of the modules",
        subtype="XYZ",
        precision=2,
        size=2,
        default=(1.0,1.0),
        min=0.0,
        max=10.0
        )
       
    buildingType : EnumProperty(
        name="Building Type",
        description="Choose building position",
        items= [("Symmetrical", "Symmetrical", "Symmetrical building facade", "", 0),
                ("Random", "Random", "Random building facade", "", 1),
                ("Flat", "Flat", "Plane building facade", "", 2)],
        default = "Flat")
    
    buildingStreet : EnumProperty(
        name="Building Street",
        description="Choose the position of the building in the street",
        items= [("Corner", "Corner", "", "", 0),
                ("Middle", "Middle", "", "", 1),
                ("Solo", "Solo", "", "", 2)],
        default = "Solo")
        
class TextureParameters(PropertyGroup):        
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
       name="Frame Color",
       subtype='COLOR',
       default=(0.0, 0.0, 0.0, 1.0),
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the window frame"
       )
    
    balconyColor : FloatVectorProperty(  
       name="Balcony Color",
       subtype='COLOR',
       default=(0.0, 0.0, 0.0, 1.0),
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the balcony "
       )
    
    glassColor : FloatVectorProperty(  
       name="Glass Color",
       subtype='COLOR',
       default=(1.0, 1.0, 1.0, 1.0),
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the window glass"
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
    
    doorColor : FloatVectorProperty(  
       name="Door Color",
       subtype='COLOR',
       default=[0.0, 0.0, 0.0, 1.0],
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the door frame"
       )
    
    doorGlassColor : FloatVectorProperty(  
       name="Door Color",
       subtype='COLOR',
       default=[1.0, 1.0, 1.0, 1.0],
       precision=2,
       size=4,
       min=0.0, max=1.0,
       description="Chose color of the door glass"
       )
       
    wallTextures : EnumProperty(
        name="Wall textures",
        description="Choose wall texture",
        items= [("Brick", "Brick", "Wall brick facade", "", 0),
                ("Stone", "Stone", "Wall stone facade", "", 1),
                ("Wood", "Wood", "Wall wood facade", "", 2)],
        default = "Brick")
        

# Initialization
def register():
    bpy.utils.register_class(BuildingParameters)
    bpy.utils.register_class(UtilitiesParameters)
    bpy.utils.register_class(TextureParameters)
    bpy.types.Scene.textureParameters = PointerProperty(name="Texture parameters", type=TextureParameters)
    bpy.types.Scene.buildingParameters = PointerProperty(name="Building parameters", type=BuildingParameters)
    bpy.types.Scene.utilitiesParameters = PointerProperty(name="Utilities parameters", type=UtilitiesParameters)


def unregister():
    bpy.utils.unregister_class(BuildingParameters)
    bpy.utils.unregister_class(UtilitiesParameters)
    bpy.utils.unregister_class(TextureParameters)
    del bpy.types.Scene.textureParameters
    del bpy.types.Scene.buildingParameters
    del bpy.types.Scene.utilitiesParameters


if __name__ == "__main__":
    register()
