import bpy
import math
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Delete default cube
bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()
# Add a new cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
# Get the object
cube = bpy.context.object
# Set the location
cube.location = (0, 0, 0)
# Set the dimensions
cube.dimensions = (1, 1, 1)
# Set the rotation
cube.rotation_euler = (math.radians(45) , math.radians(45) , math.radians(45))
# Set the material
mat = bpy.data.materials.new(name="MaterialName")
cube.data.materials.append(mat)
# Render the image
bpy.context.scene.render.filepath = dir_path + '\\output\\cube.png'
bpy.ops.render.render(write_still=True)