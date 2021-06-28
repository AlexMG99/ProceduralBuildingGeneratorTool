# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Procedural Building Generato",
    "author": "Alex Morales Garcia",
    "version": (1, 4, 4),
    "blender": (2, 80, 0),
    "location": "View3d > Tool",
    "description": "Generates buildings procedurally",
    "doc_url": "https://github.com/AlexMG99/ProceduralBuildingGeneratorTool",
    "tracker_url": "https://github.com/AlexMG99/ProceduralBuildingGeneratorTool/issues",
    "category": "Procedural",
}

import os

from . import utilities
from . import parameters
from . import generateBuilding
from . import panelController

# =========================================================================
# Registration:
# =========================================================================

def register():
    utilities.register()
    parameters.register()
    generateBuilding.register()
    panelController.register()


def unregister():
    utilities.unregister()
    parameters.unregister()
    generateBuilding.unregister()
    panelController.unregister()


if __name__ == "__main__":
    register()
