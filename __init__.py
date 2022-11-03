# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    "name": "SmittyTools",
    "author": "Smitty Werben",
    "description": "The blender Scripts I use very often",
    "blender": (3, 0, 0),
    "version": (0, 0, 1),
    "location": "3D-Viewport > N-Panel",
    "warning": "",
    "category": "Generic",
}

from . import ui
from .src import select_deform_bones,Batch_Export_Shapkeys_as_OBJs

import bpy
# ---------------------------------------------
# Blender Register
# ---------------------------------------------

#ui has to be registered first
tools=[
    ui,
    select_deform_bones,
    Batch_Export_Shapkeys_as_OBJs

]

def register():
    for tool in tools:
        tool.register()



def unregister():
    for tool in reversed(tools):
        tool.unregister()
