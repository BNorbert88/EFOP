import bpy
import random

def randomLightPosition():
    x = random.uniform(2, 4) * pow(-1, random.randint(1, 2))
    y = random.uniform(2, 4) * pow(-1, random.randint(1, 2))
    z = random.uniform(0.2, 5)
    return (x, y, z)

# Delete the original objects
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete(use_global=False)
bpy.ops.object.select_by_type(type='LAMP')
bpy.ops.object.delete(use_global=False)

bpy.data.worlds['World'].light_settings.use_environment_light = True
bpy.data.worlds['World'].light_settings.environment_energy = 0.2

# Add a camera
bpy.ops.object.camera_add(location=(6, -3, 5), rotation=(0, 0, 0))
bpy.context.object.rotation_euler[0] = 0.9
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 1.1

# Add a lamp.
bpy.ops.object.lamp_add(type='POINT', location=(3, 2, 6))
bpy.context.object.data.shadow_method = 'RAY_SHADOW'
bpy.context.object.name = "Light"

# Create a cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bpy.context.object.name = "Cube1"
mat = bpy.data.materials.new("Mat1")
mat.diffuse_color = (1.2, 3.0, 1.0)
bpy.context.selected_objects[0].active_material = mat

# Create the plane
bpy.ops.mesh.primitive_plane_add(radius=10, location=(0, 0, -1))

# render settings


for x in range(3):
    pos = randomLightPosition()

    bpy.ops.object.select_by_type(type='LAMP')
    bpy.ops.object.delete(use_global=False)

    # Add a lamp.
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.name = "Light"

    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "D:/kocka/image" + str(x) + "shadow.png"
    bpy.ops.render.render(write_still=1)

    bpy.ops.object.select_by_type(type='LAMP')
    bpy.ops.object.delete(use_global=False)

    # Add a lamp.
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'NOSHADOW'
    bpy.context.object.name = "Light"

    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "D:/kocka/image" + str(x) + "no_sh.png"
    bpy.ops.render.render(write_still=1)




