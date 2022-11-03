import bpy
import os

# select all bones that are used in the selected object


def main(self,context):
    selected_objects=context.selected_objects
    armature=None
    models=[]

    for obj in selected_objects:
        if obj.type=="ARMATURE":
            armature=obj
        elif obj.type=="MESH":
            models.append(obj)

    if len(models)==0  or armature is None:
        self.report({"ERROR"},"Select all Models and one Armature")
        return {"CANCELLED"}


    bone_names=[x.name for x in armature.data.bones]
    true_deform_bones=[]


    for model in models:
        for vgrp in model.vertex_groups:
            if vgrp.name in bone_names:
                true_deform_bones.append(vgrp.name)

    #make list unique
    true_deform_bones =list(set(true_deform_bones))

    #select armature and go in pose mode
    context.view_layer.objects.active=armature
    bpy.ops.object.mode_set(mode='POSE')

    #deselect all bones
    bpy.ops.pose.select_all(action='DESELECT')

    #go in edit mode
    #bpy.ops.object.mode_set(mode='EDIT')


    #select true deform bones
    for tdb in true_deform_bones:
        armature.data.bones[tdb].select=True
    return {"FINISHED"}



class SMITTY_OT_SelectBonesUsedByMesh(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "smitty.select_bones_used_by_mesh"
    bl_label = " select all bones that are used in the selected object and armature"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
       return main(self,context)

def menu_func(self, context):

    self.layout.operator(SMITTY_OT_SelectBonesUsedByMesh.bl_idname, text=SMITTY_OT_SelectBonesUsedByMesh.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SMITTY_OT_SelectBonesUsedByMesh)
    bpy.types.OBJECT_PT_SmittyTools.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SMITTY_OT_SelectBonesUsedByMesh)
    bpy.types.OBJECT_PT_SmittyTools.remove(menu_func)
