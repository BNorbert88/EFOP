import bpy
import random
import math
import mathutils


# Define a position around the origin above the horizontal plane
def randomSpherePosition(dist):
    phi = math.radians(random.uniform(0, 360))
    theta = math.radians(random.uniform(10, 80))
    xc = dist * math.sin(theta) * math.cos(phi)
    yc = dist * math.sin(theta) * math.sin(phi)
    zc = dist * math.cos(theta)
    return (xc, yc, zc)


# Gives the lowest point of an object.
def objectLowestPoint(obj):
    matrix_w = obj.matrix_world
    vectors = [matrix_w * vertex.co for vertex in obj.data.vertices]
    return min(vectors, key=lambda item: item.z)


# Gives the lowest point of the full configuration.
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


# Gives a cube object randomly rotated around the origin.
def randomCube():
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0),
                                    rotation=(
                                        random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


# Gives a fixed cube.
def fixedCube(obj_name="cube", rot=(1, 1, 1), col=(0.5, 0.5, 0.5)):
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=rot)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = col
    c.active_material = mat
    c.name = obj_name
    return c


# Gives a cube object randomly rotated around the line e(t)=(0,0,t).
def randomMonkey():
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0),
                                      rotation=(0, 0, random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c

# Gives a fixed cube.
def fixedMonkey(obj_name="monkey", rot=(0, 0, 1), col=(0.5, 0.5, 0.5)):
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0), rotation=rot)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = col
    c.active_material = mat
    c.name = obj_name
    return c


# Gives a cube object randomly rotated around the origin.
def randomCone():
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0),
                                    rotation=(
                                        random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


# Gives a fixed cone.
def fixedCone(obj_name="torus", rot=(1, 1, 1), col=(0.5, 0.5, 0.5)):
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0), rotation=rot)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = col
    c.active_material = mat
    c.name = obj_name
    return c


# Gives a cube object randomly rotated around the origin.
def randomTorus():
    bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0),
                                     rotation=(
                                         random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


# Gives a fixed cube.
def fixedTorus(obj_name="torus", rot=(1, 1, 1), col=(0.5, 0.5, 0.5)):
    bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0), rotation=rot)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = col
    c.active_material = mat
    c.name = obj_name
    return c


# Gives a random object.
def randomObject():
    a = random.random()
    if a < 0.25:
        return randomCube()
    elif a < 0.50:
        return randomTorus()
    elif a < 0.75:
        return randomCone()
    else:
        return randomMonkey()

# Gives a random object.
def fixedObject(obj_name, rot, col):
    a = random.random()
    if a < 0.25:
        return "cube", fixedCube(obj_name=obj_name, rot=rot, col=col)
    elif a < 0.50:
        return "torus", fixedTorus(obj_name=obj_name, rot=rot, col=col)
    elif a < 0.75:
        return "cone", fixedCone(obj_name=obj_name, rot=rot, col=col)
    else:
        return "monkey", fixedMonkey(obj_name=obj_name, rot=rot, col=col)


# Creates a lamp object in a random position with a given name.
def randomLamp(obj_name, dist=7):
    pos = randomSpherePosition(dist)
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.energy = random.uniform(0.5, 3)
    bpy.context.object.name = obj_name


# Creates a lamp object in a random position with a given name.
def fixedLamp(obj_name="lamp", pos=(0.5, 0.5, 0.5), ener=0.5):
    bpy.ops.object.lamp_add(type='POINT', location=pos)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.energy = ener
    bpy.context.object.name = obj_name


# Creates a camera object in a random position with a given name.
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


def fixedCamera(obj_name="cam", loc=(1, 1, 1)):
    bpy.ops.object.camera_add(location=loc)
    bpy.context.object.name = obj_name
    camera = bpy.context.object
    looking_direction = mathutils.Vector(loc) - mathutils.Vector((0.0, 0.0, 0.0))
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    bpy.context.scene.camera = camera


# Deletes all the object in the constellation.
def deleteAll():
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type='LAMP')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type='CAMERA')
    bpy.ops.object.delete(use_global=False)


# Setup a global environmental lightning
world = bpy.data.worlds['World']
world.light_settings.use_environment_light = True
world.light_settings.environment_energy = 0.2
# world.mist_settings.use_mist = True
# world.mist_settings.intensity = random.uniform(0.2, 0.95)
# world.mist_settings.intensity = 0.6
world.mist_settings.depth = 15
world.mist_settings.height = 10

f = open("D:/kocka/images/test/data.txt", "w")

# Generates name-rotation pairs for cubes
list_objects_positions = []
for i in range(10):
    name = "obj" + str(i)
    rot = (random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14))
    col = (random.random(), random.random(), random.random())
    list_objects_positions.append([name, rot, col])

# Generates name-position pairs for the lights
list_lights_positions = []
for i in range(10):
    name = "lamp" + str(i)
    pos = randomSpherePosition(7)
    energy = (i+1)
    list_lights_positions.append([name, pos, energy])
    f.write(name + " -- position: "+str(pos)+", energy: " + str(energy) + "\n")


# Generates name-position pairs for the cameras
list_cameras_positions = []
for i in range(10):
    name = "cam" + str(i)
    pos = randomSpherePosition(random.uniform(8,15))
    list_cameras_positions.append([name, pos])
    f.write(name + " -- position: " + str(pos) + "\n")


for obj in list_objects_positions:

    deleteAll()
    fixobj = fixedObject(obj_name=obj[0], rot=obj[1], col=obj[2])
    f.write(fixobj[1].name + " -- type: " + fixobj[0] + ", position: " + str(obj[1]) + ", color: " + str(obj[2]) + "\n")

    bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())

    for light in list_lights_positions:
        bpy.ops.object.select_by_type(type='LAMP')
        bpy.ops.object.delete(use_global=False)
        fixedLamp(obj_name=light[0], pos=light[1], ener=light[2])

        for cam in list_cameras_positions:
            bpy.ops.object.select_by_type(type='CAMERA')
            bpy.ops.object.delete(use_global=False)
            fixedCamera(obj_name=cam[0], loc=cam[1])

            world.mist_settings.use_mist = False

            bpy.context.scene.render.image_settings.file_format = 'PNG'
            bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_"\
                                                + cam[0] + "_mist0.png"
            bpy.context.scene.render.resolution_x = 200
            bpy.context.scene.render.resolution_y = 200
            bpy.ops.render.render(write_still=1)

            bpy.data.objects[light[0]].data.shadow_method = 'NOSHADOW'

            bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_"\
                                                + cam[0] + "_mist0_noshadow.png"
            bpy.ops.render.render(write_still=1)

            bpy.data.objects[light[0]].data.shadow_method = 'RAY_SHADOW'
            world.mist_settings.use_mist = True

            for j in range(9):
                world.mist_settings.intensity = (j+1)/10
                bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_"\
                                                    + cam[0] + "_mist" + str(j+1) + ".png"
                bpy.ops.render.render(write_still=1)

for i in range(9):
    name = "mist" + str(i+1)
    f.write(name + " -- intensity: " + str((i+1)/10) + "\n")

f.close()

# for x in range(5000):
#     # Delete the original default objects
#     deleteAll()
#
#     # Add a camera
#     randomCamera("camera1", random.uniform(2, 4))
#
#     # Add a lamp.
#     randomLamp("lamp1")
#
#     # Create a cube
#     randomObject()
#
#     # Create the plane
#     bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())
#
#     # Rendering (with shadow)
#     bpy.context.scene.render.image_settings.file_format = 'PNG'
#     bpy.context.scene.render.filepath = "D:/kocka/images/shadow2/image" + str(x) + ".png"
#     bpy.context.scene.render.resolution_x = 400
#     bpy.context.scene.render.resolution_y = 400
#     bpy.ops.render.render(write_still=1)
#
#     # Delete the original default objects
#     deleteAll()
#
#     # Add a camera
#     randomCamera("camera1", random.uniform(2, 4))
#
#     # Add a lamp.
#     randomLamp("lamp1")
#
#     # Create a cube
#     randomObject()
#
#     # Create the plane
#     bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())
#
#     bpy.data.objects['lamp1'].data.shadow_method = 'NOSHADOW'
#
#     # Rendering (without shadow)
#     bpy.context.scene.render.image_settings.file_format = 'PNG'
#     bpy.context.scene.render.filepath = "D:/kocka/images/noshadow2/image" + str(x) + ".png"
#     bpy.context.scene.render.resolution_x = 400
#     bpy.context.scene.render.resolution_y = 400
#     bpy.ops.render.render(write_still=1)
