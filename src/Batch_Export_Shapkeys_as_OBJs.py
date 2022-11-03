# Export all Shape Keys as OBJs in Blender
# Tested Version 3.2.2
# =========================================
# Original Script by Tlousky

import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty,BoolProperty
import os
from os.path import join

def main(self,context,_exportPath):
    # Reference the active object
    o = context.active_object

    #variable containing list of active object's shapekeys
    blocks:bpy.types.ShapeKey = o.data.shape_keys.key_blocks

    #iterate over object's list of shapekeys

    #for ind in range(len(blocks)):
    #    print(blocks[ind].name)

    # CHANGE THIS to the folder you want to save your OBJ files in
    # NOTE: no spaces, no trailing slash
    exportPath =bpy.path.abspath( _exportPath)

    # Reset all shape keys to 0 (skipping the Basis shape on index 0
    for skblock in o.data.shape_keys.key_blocks[1:]:
        skblock.value = 0

    # Iterate over shape key blocks and save each as an OBJ file
    # Excluding Basis Shape
    blockamount= max(0,len(blocks))
    for ind in range(1,len(blocks)):
        blocks[ind].value = 1.0 # Set shape key value to max

        # Set OBJ file path and Export OBJ
        objFileName =o.name+"_"+ blocks[ind].name + ".obj" # File name = shapekey name
        objPath = join( exportPath, objFileName )
        bpy.ops.export_scene.obj(
            filepath = objPath,
            use_selection = True,
            global_scale = 1 ,
            keep_vertex_order=True,
            use_mesh_modifiers=False,
            use_smooth_groups=False,
            use_smooth_groups_bitflags=False,
            use_normals=False,
            use_uvs= False,
            use_materials= False,
            use_triangles= False,
            use_nurbs= False,
            use_vertex_groups= False
            )

        blocks[ind].value = 0 # Reset shape key value to 0
    self.report({"INFO"},"Exported "+str(blockamount)+"shape keys!")



class SMITTY_OT_BatchExportShapeKeysToObj(bpy.types.Operator,ExportHelper):
    """Tooltip"""
    bl_idname = "smitty.batch_export_shape_keys_obj"
    bl_label = "Batch Export Shape Keys to Obj"

   # ExportHelper mixin class uses this
    filename_ext = ".obj"
    filepath=""
    filter_glob: StringProperty(
        default="*.obj",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    # use_setting: BoolProperty(
    #     name="Example Boolean",
    #     description="Example Tooltip",
    #     default=True,
    # )


    @classmethod
    def poll(cls, context):
        return context.active_object.type=="MESH"

    def execute(self, context):
        abspath=bpy.path.abspath(self.filepath)
        dirpath=os.path.join(abspath,os.pardir)

        if not os.path.exists(dirpath):
            self.report({"ERROR"},"Selected Directory does not Exist")
            return {"CANCELLED"}
        main(self,context,dirpath)
        return {'FINISHED'}


def menu_func(self, context):

    self.layout.operator(SMITTY_OT_BatchExportShapeKeysToObj.bl_idname, text=SMITTY_OT_BatchExportShapeKeysToObj.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SMITTY_OT_BatchExportShapeKeysToObj)
    bpy.types.OBJECT_PT_SmittyTools.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SMITTY_OT_BatchExportShapeKeysToObj)
    bpy.types.OBJECT_PT_SmittyTools.remove(menu_func)
