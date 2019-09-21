import bpy
import random


def randomLightPosition():
    x = random.uniform(2, 4) * pow(-1, random.randint(1, 2))
    y = random.uniform(2, 4) * pow(-1, random.randint(1, 2))
    z = random.uniform(0.2, 5)
    return (x, y, z)


def objectLowestPoint(obj):
    matrix_w = obj.matrix_world
    vectors = [matrix_w * vertex.co for vertex in obj.data.vertices]
    return min(vectors, key=lambda item: item.z)


def absoluteLowestPoint():
    bpy.ops.object.select_all(action='SELECT')
    obs = bpy.context.selected_objects
    minv = [0, 0, 0]
    for obj in obs:
        matrix_w = obj.matrix_world
        vectors = [matrix_w * vertex.co for vertex in obj.data.vertices]
        v = min(vectors, key=lambda item: item.z)
        if minv[2] > v[2]:
            minv = v
        return minv


def randomObject():
    a=random.random()
    if a < 0.33:
        return randomCube()
    if a < 0.66:
        return randomTorus()
    return randomMonkey()


def randomCube():
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0),
                                    rotation=(
                                    random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def randomMonkey():
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0),
                                      rotation=(0, 0, random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def randomTorus():
    bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0),
                                     rotation=(
                                     random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def randomLamp(name):
    pos = randomLightPosition()
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.name = name


# Setup a global environmental lightning
world = bpy.data.worlds['World']
world.light_settings.use_environment_light = True
world.light_settings.environment_energy = 0.2

# Add a camera
bpy.ops.object.camera_add(location=(6, -3, 5), rotation=(0, 0, 0))
bpy.context.object.name = "camera1"
bpy.context.object.rotation_euler[0] = 0.9
bpy.context.object.rotation_euler[1] = 0.0
bpy.context.object.rotation_euler[2] = 1.1

for x in range(10):
    # Delete the original default objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type='LAMP')
    bpy.ops.object.delete(use_global=False)

    # Add a lamp.
    randomLamp("lamp1")

    # Create a cube
    randomObject()

    # Create the plane
    bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())

    # Rendering
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "D:/kocka/images/image" + str(x) + "shadow.png"
    bpy.ops.render.render(write_still=1)

    bpy.data.objects['lamp1'].data.shadow_method = 'NOSHADOW'

    # Rendering
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "D:/kocka/images/image" + str(x) + "noshadow.png"
    bpy.ops.render.render(write_still=1)
