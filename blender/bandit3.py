import bpy
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Specify the path to the .blend file
blend_file_path = os.path.join(dir_path, "BasicBandit", "BasicBanditBlend.blend")

# Import the .blend file
with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
    for attr in dir(data_to):
        setattr(data_to, attr, getattr(data_from, attr))

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# Add the imported object(s) to the active view layer and select them
for obj in data_to.objects:
    if obj is not None:
        # Link the object to the active collection
        bpy.context.collection.objects.link(obj)
        # Select the object
        obj.select_set(True)
        # Set the object as the active object
        bpy.context.view_layer.objects.active = obj

print("Imported object(s) from .blend file")

# Set up materials and textures for the object
for mat in bpy.data.materials:
    print(mat)

# Set up the texture directory path
textures_dir = os.path.join(dir_path, "BasicBandit", "Textures")

# Set up output directory and file format
output_dir = os.path.join(dir_path, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

bpy.context.scene.render.filepath = os.path.join(output_dir, "rendered_image_3.png")
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Adjust camera position and rotation (you might need to tweak the values depending on your object)
camera = bpy.data.objects['Camera']
camera.location = (5, -5, 5.5)
camera.rotation_euler = (1.0, 0.0, 0.785)

armature_obj = None
for obj in bpy.context.scene.objects:
    if obj.type == 'ARMATURE':
        armature_obj = obj
        break

if armature_obj:
    # Select the armature object and set the mode to 'POSE'
    bpy.ops.object.select_all(action='DESELECT')
    armature_obj.select_set(True)
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='POSE')

    # Rotate the head bone to look at the camera
    head_bone_name = 'Head'
    head_bone = armature_obj.pose.bones.get(head_bone_name)

    if head_bone:
        head_bone.rotation_mode = 'XYZ'
        head_bone.rotation_euler.rotate_axis('X', 0.5)
        armature_obj.keyframe_insert(data_path=f'pose.bones["{head_bone_name}"].rotation_euler', frame=1)

    # Rotate the left arm bones
    upper_arm_l_bone = armature_obj.pose.bones.get('UpperArm.L')
    lower_arm_l_bone = armature_obj.pose.bones.get('LowerArm.L')
    if upper_arm_l_bone and lower_arm_l_bone:
        upper_arm_l_bone.rotation_mode = 'XYZ'
        lower_arm_l_bone.rotation_mode = 'XYZ'
        upper_arm_l_bone.rotation_euler.rotate_axis('X', 1.57) # 90 degrees in radians
        lower_arm_l_bone.rotation_euler.rotate_axis('X', -0.785) # -45 degrees in radians
        armature_obj.keyframe_insert(data_path='pose.bones["UpperArm.L"].rotation_euler', frame=1)
        armature_obj.keyframe_insert(data_path='pose.bones["LowerArm.L"].rotation_euler', frame=1)

    # Rotate the left thumb bones
    thumb_proximal_l_bone = armature_obj.pose.bones.get('ThumbProximal.L')
    thumb_middle_l_bone = armature_obj.pose.bones.get('ThumbMiddle.L')
    thumb_distal_l_bone = armature_obj.pose.bones.get('ThumbDistal.L')
    if thumb_proximal_l_bone and thumb_middle_l_bone and thumb_distal_l_bone:
        thumb_proximal_l_bone.rotation_mode = 'XYZ'
        thumb_middle_l_bone.rotation_mode = 'XYZ'
        thumb_distal_l_bone.rotation_mode = 'XYZ'
        thumb_proximal_l_bone.rotation_euler.rotate_axis('Z', 1.57) # 90 degrees in radians
        thumb_middle_l_bone.rotation_euler.rotate_axis('Z', 0.785) # 45 degrees in radians
        thumb_distal_l_bone.rotation_euler.rotate_axis('Z', 0.785) # 45 degrees in radians
        armature_obj.keyframe_insert(data_path='pose.bones["ThumbProximal.L"].rotation_euler', frame=1)
        armature_obj.keyframe_insert(data_path='pose.bones["ThumbMiddle.L"].rotation_euler', frame=1)
        armature_obj.keyframe_insert(data_path='pose.bones["ThumbDistal.L"].rotation_euler', frame=1)

# create light datablock, set attributes
light_data = bpy.data.lights.new(name="light_2.80", type='POINT')
light_data.energy = 40

# create new object with our light datablock
light_object = bpy.data.objects.new(name="light_2.80", object_data=light_data)

# link light object
bpy.context.collection.objects.link(light_object)

# make it active 
bpy.context.view_layer.objects.active = light_object

#change location
light_object.location = (1, -1, 0)

# Render the scene and save the image
bpy.ops.render.render(write_still=True)

print("Rendered image saved as PNG")