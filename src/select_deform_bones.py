import bpy


def main(context):
    bpy.ops.object.mode_set(mode='POSE')
    obj = bpy.context.object
    for bone in obj.data.bones:
        if bone.use_deform:
            bone.select=True
        else:
            bone.select=False


class SMITTY_OT_AdjustRiggingToShape(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "smitty.select_deform_bones"
    bl_label = "Select all only Deform Bones"

    @classmethod
    def poll(cls, context):
         if context.active_object is not None:
            return context.active_object.type=="ARMATURE"
         return False

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):

    self.layout.operator(SMITTY_OT_AdjustRiggingToShape.bl_idname, text=SMITTY_OT_AdjustRiggingToShape.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SMITTY_OT_AdjustRiggingToShape)
    bpy.types.OBJECT_PT_SmittyTools.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SMITTY_OT_AdjustRiggingToShape)
    bpy.types.OBJECT_PT_SmittyTools.remove(menu_func)
