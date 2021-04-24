import bpy, bmesh
import os

def generateUVS(obj):
    
    # Go to edit mode, edge selection modes
    bpy.ops.object.mode_set( mode = 'EDIT')
    bpy.ops.mesh.select_mode( type = 'EDGE')
    
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    # notice in Bmesh polygons are called edge
    bm.edges.ensure_lookup_table()
    bm.edges[1].select_set(True)
    bm.edges[4].select_set(True)
    bm.edges[10].select_set(True)
    bm.edges[15].select_set(True)
    
    # Mark Edge Seam and smart UV
    bpy.ops.mesh.mark_seam(clear=False)
    bpy.ops.uv.smart_project()

    # Show the updates in the viewports
    bmesh.update_edit_mesh(me, True)

def addMaterial(obj, name):
    
    # Select object 
    bpy.data.objects[obj.name].select_set(True)
    
    if "Wall" in bpy.data.materials:
        mat = bpy.data.materials.get("Wall")
    else:
        mat = createMaterial(obj, name)
    
    obj.data.materials.append(mat)
    obj.data.materials[0] = mat
    
    
def createMaterial(obj, texName):
    
    # Create new material
    mat = bpy.data.materials.new(name=texName)
    mat.use_nodes = True
    cwd = os.getcwd()
    
    # TODO: Change relative path
    texturePath = bpy.path.abspath(cwd + "/2.91/scripts/startup/pbg/textures/")
    
    # Load Images
    imgDiffuse = bpy.data.images.load(texturePath + texName + "_Diffuse.tif")
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