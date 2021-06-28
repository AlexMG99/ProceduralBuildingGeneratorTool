import bpy, bmesh
import os

from pbg import utilities
from pbg import parameters

import imp
imp.reload(utilities)
imp.reload(parameters)

# Generate window UVS
def generateUVS(obj, idx):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called edge
    bm.edges.ensure_lookup_table()
    
    utilities.selectEdgesByIndex(obj.name, idx)
    
    # Mark Edge Seam and smart UV
    bpy.ops.mesh.mark_seam(clear=False)
    
    bpy.ops.mesh.select_all( action = 'SELECT')
    bpy.ops.uv.smart_project()

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

# Add material with texture
def addMaterial(obj, name):
    
    # Select object 
    bpy.data.objects[obj.name].select_set(True)
    
    if name in bpy.data.materials:
        mat = reloadMaterial(name)
    else:
        mat = createMaterial(obj, name)
    
    obj.data.materials.append(mat)
    obj.data.materials[0] = mat
    

# Add material window to object
def addMaterialBase(obj, name):
    bpy.data.objects[obj.name].select_set(True)
    
    if name in bpy.data.materials:
        mat = reloadMaterial(name)
    else:
        mat = createMaterialBase(obj, name)
    
    obj.data.materials.append(mat)
    bpy.context.object.active_material_index = len(obj.data.materials) - 1
    
    bpy.ops.object.material_slot_assign()


def reloadMaterial(name):
    mat = bpy.data.materials.get(name)
    
    if name == "Frame":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.windowColor
    elif name == "Glass":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.glassColor
    elif name == "Wall 1":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.wallColor
    elif name == "Frame Door":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.doorColor
    elif name == "Glass Door":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.doorGlassColor    
    return mat
    
def createMaterialBase(obj, texName):
    # Create new material
    mat = bpy.data.materials.new(name=texName)
    mat.use_nodes = True
    
    # Create material by name
    if texName == "Frame":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.windowColor
    elif texName == "Glass":
        mat.node_tree.nodes["Principled BSDF"].inputs["Transmission"].default_value = 1
        mat.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0
        mat.use_screen_refraction = True

        mat.blend_method = 'HASHED'
        mat.refraction_depth = 0.001
    elif texName == "Bottom":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (1, 1, 1, 1)
    elif texName == "Wall 1":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.wallColor 
    elif texName == "Frame Door":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.doorColor
    elif texName == "Glass Door":
        mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = bpy.context.scene.textureParameters.doorGlassColor   
    return mat
    
def createMaterial(obj, texName):
    # Create new material
    mat = bpy.data.materials.new(name=texName)
    mat.use_nodes = True
    
    # TODO: Change relative path
    # texturePath = bpy.path.abspath(cwd + "/textures/")
    texturePath = bpy.path.dirname(os.path.dirname(os.path.abspath("material.py")) + "/textures/")
    
    # Rename textures
    if texName == "Glass Door":
        texName = "Glass"
    elif texName == "Frame Door":
        texName = "Door"
        
    # Load Images    
    imgDiffuse = bpy.data.images.load(texturePath + texName + "_Diffuse.tif")
    print(texturePath + texName + "_Diffuse")
    imgNormal = bpy.data.images.load(texturePath + texName + "_Normal.tif")
    imgAO = bpy.data.images.load(texturePath + texName + "_AO.tif")
    imgRoughness = bpy.data.images.load(texturePath + texName + "_Roughness.tif")
    
    # Add textures to material
    loadDiffuseAO(mat, imgDiffuse, imgAO)
    loadRoughness(mat, imgRoughness)
    loadNormal(mat, imgNormal)

    return mat

def loadDiffuseAO(mat, imgD, imgAO):
    # Create Diffuse Texture node
    texImageD = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImageD.image = imgD
    
    # Create AO Texture node
    texImageAO = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImageAO.image = imgAO
    
    # Create Multiply node
    multNode = mat.node_tree.nodes.new('ShaderNodeMixRGB')
    multNode.blend_type = 'MULTIPLY'
    
    # Link nodes
    mat.node_tree.links.new(multNode.inputs['Color1'], texImageD.outputs['Color'])
    mat.node_tree.links.new(multNode.inputs['Color2'], texImageAO.outputs['Color'])
    
    mat.node_tree.links.new(mat.node_tree.nodes["Principled BSDF"].inputs['Base Color'], multNode.outputs['Color'])    
    
def loadRoughness(mat, img):
    # Create Roughness Texture node
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = img
    
    # Create ColorRamp node
    colRamp = mat.node_tree.nodes.new('ShaderNodeValToRGB')
    colRamp.color_ramp.elements[0].position = 0.45;
    colRamp.color_ramp.elements[1].position = 0.8;
    
    # Link nodes
    mat.node_tree.links.new(colRamp.inputs[0], texImage.outputs['Color'])
    
    mat.node_tree.links.new(mat.node_tree.nodes["Principled BSDF"].inputs['Roughness'], colRamp.outputs['Color'])

def loadNormal(mat, img):
    # Create Normal Texture node
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = img
    
    # Create Multiply node
    normalNode = mat.node_tree.nodes.new('ShaderNodeNormalMap')
    
    # Link nodes
    mat.node_tree.links.new(normalNode.inputs['Color'], texImage.outputs['Color'])
    
    mat.node_tree.links.new(mat.node_tree.nodes["Principled BSDF"].inputs['Normal'], normalNode.outputs['Normal'])        