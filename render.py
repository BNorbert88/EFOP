import bpy
import random
import math
import mathutils


def randomSpherePosition(dist):
    phi = math.radians(random.uniform(0, 360))
    theta = math.radians(random.uniform(10, 80))
    xc = dist * math.sin(theta) * math.cos(phi)
    yc = dist * math.sin(theta) * math.sin(phi)
    zc = dist * math.cos(theta)
    return (xc, yc, zc)


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
    a = random.random()
    if a < 0.25:
        return randomCube()
    if a < 0.50:
        return randomTorus()
    if a < 0.75:
        return randomCone()
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


def randomCone():
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0),
                                    rotation=(
                                        random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
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
    pos = randomSpherePosition(7)
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.energy = random.uniform(0.5, 3)
    bpy.context.object.name = name


def randomCamera(name, dist):
    loc = randomSpherePosition(dist)
    bpy.ops.object.camera_add(location=loc)
    bpy.context.object.name = name
    camera = bpy.context.object
    looking_direction = mathutils.Vector(loc) - mathutils.Vector((0.0, 0.0, 0.0))
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat * mathutils.Vector((0.0, 0.0, random.uniform(10, 20))) + mathutils.Vector(
        [random.uniform(-3, 3), random.uniform(-3, 3), 0])
    bpy.context.scene.camera = camera


# Setup a global environmental lightning
world = bpy.data.worlds['World']
world.light_settings.use_environment_light = True
world.light_settings.environment_energy = 0.2
# world.mist_settings.use_mist = True
# world.mist_settings.intensity = random.uniform(0.2, 0.95)
# world.mist_settings.intensity = 0.6
# world.mist_settings.depth = 15
# world.mist_settings.height = 10

for x in range(5000):

    # Delete the original default objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type='LAMP')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type='CAMERA')
    bpy.ops.object.delete(use_global=False)

    # Add a camera
    randomCamera("camera1", random.uniform(2, 4))

    # Add a lamp.
    randomLamp("lamp1")

    # Create a cube
    randomObject()

    # Create the plane
    bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())

    # Rendering (with shadow)
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = "D:/kocka/images/shadow/image" + str(x) + ".png"
    bpy.context.scene.render.resolution_x = 200
    bpy.context.scene.render.resolution_y = 200
    bpy.ops.render.render(write_still=1)

    # bpy.data.objects['lamp1'].data.shadow_method = 'NOSHADOW'
    #
    # # Rendering (without shadow)
    # bpy.context.scene.render.image_settings.file_format = 'PNG'
    # bpy.context.scene.render.filepath = "D:/kocka/images/noshadow/image" + str(x) + ".png"
    # bpy.context.scene.render.resolution_x = 200
    # bpy.context.scene.render.resolution_y = 200
    # bpy.ops.render.render(write_still=1)
