import bpy


class SMITTY_PT_SmittyTools(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Smitty Tools"
    bl_idname = "OBJECT_PT_SmittyTools"
    bl_category = "Smitty-Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"



    def draw(self, context):
        layout = self.layout


def register():
    bpy.utils.register_class(SMITTY_PT_SmittyTools)


def unregister():
    bpy.utils.unregister_class(SMITTY_PT_SmittyTools)
