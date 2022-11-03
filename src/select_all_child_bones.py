import bpy


def main(context:bpy.types.Context):
    #get selected bones
    selected_bones=[]
    if context.mode=="POSE":
        selected_bones=context.selected_pose_bones
    elif  context.mode=="EDIT_ARMATURE":
        selected_bones=context.selected_bones

    #capture current mode
    old_mode=context.mode
    if old_mode=="EDIT_ARMATURE":
        old_mode="EDIT"

    #recursively select their children
    bpy.ops.object.mode_set(mode='POSE')
    for selected_bone in selected_bones:
        recursive_select_bone(context,context.active_object.data.bones[selected_bone.name])

    #set old mode back
    bpy.ops.object.mode_set(mode=old_mode)

def recursive_select_bone(context:bpy.types.Context,bone):
        for child in bone.children_recursive:
            child.select=True




class SMITTY_OT_SelectAllChildBones(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "smitty.select_child_bones"
    bl_label = "Recursively Select all child Bones"

    @classmethod
    def poll(cls, context):
        if context.active_object:
            if context.active_object.type=="ARMATURE":
                return context.mode=="POSE"or context.mode=="EDIT_ARMATURE"
        return False

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):

    self.layout.operator(SMITTY_OT_SelectAllChildBones.bl_idname, text=SMITTY_OT_SelectAllChildBones.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SMITTY_OT_SelectAllChildBones)
    bpy.types.OBJECT_PT_SmittyTools.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SMITTY_OT_SelectAllChildBones)
    bpy.types.OBJECT_PT_SmittyTools.remove(menu_func)
