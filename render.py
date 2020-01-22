import bpy
import random
import math
import mathutils


def random_sphere_position(dist):
    """
    Define a position around the origin above the horizontal plane with a given distance.

    @type dist: float
    @param dist: how far is the point from the origin
    @rtype: tuple
    @return: coordinates of a point
    """
    phi = math.radians(random.uniform(0, 360))
    theta = math.radians(random.uniform(10, 80))
    xc = dist * math.sin(theta) * math.cos(phi)
    yc = dist * math.sin(theta) * math.sin(phi)
    zc = dist * math.cos(theta)
    return xc, yc, zc


def object_lowest_point(object):
    """
    Gives the lowest point of an object.

    @type object: blender object
    @param object: an investigated object to determine its lowest point
    @rtype: float
    @return: lowest point of the vectorized object
    """
    matrix_w = object.matrix_world
    vectors = [matrix_w * vertex.co for vertex in object.data.vertices]
    return min(vectors, key=lambda item: item.z)


def absolute_lowest_point():
    """
    Gives the lowest point of the full configuration.

    @rtype: array(3)
    @return: lowest point of the set of vectorized objects
    """
    bpy.ops.object.select_all(action='SELECT')
    obs = bpy.context.selected_objects
    min_v = [0, 0, 0]
    for object in obs:
        matrix_w = object.matrix_world
        vectors = [matrix_w * vertex.co for vertex in object.data.vertices]
        v = min(vectors, key=lambda item: item.z)
        if minv[2] > v[2]:
            min_v = v
        return min_v


def random_cube():
    """
    Adds a cube into the scene.
    Default position is the origin and it is randomly rotated.

    @rtype: blender object
    @return: a blender cube that is added to the scene
    """
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0),
                                    rotation=(
                                        random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def fixed_cube(obj_name="cube", rotation=(1, 1, 1), color=(0.5, 0.5, 0.5)):
    """
    Adds a cube into the scene with fixed position and orientation.

    @type obj_name: string
    @param obj_name: name of the object, default: "cube"
    @type rotation: tuple
    @param rotation: rotation of the cube, default: (1,1,1)
    @type color: tuple
    @param color: color of the cube, default: (0.5,0.5,0.5)
    @rtype: blender object
    @return: a blender cube that is added to the scene
    """
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=rotation)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = color
    c.active_material = mat
    c.name = obj_name
    return c


def random_monkey():
    """
    Adds a monkey into the scene.
    Default position is the origin and it is randomly rotated along the vertical axis.

    @rtype: blender object
    @return: a blender monkey that is added to the scene
    """
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0),
                                      rotation=(0, 0, random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def fixed_monkey(obj_name="monkey", rotation=(0, 0, 1), color=(0.5, 0.5, 0.5)):
    """
    Adds a monkey into the scene with fixed position and orientation.

    @type obj_name: string
    @param obj_name: name of the object, default: "monkey"
    @type rotation: tuple
    @param rotation: rotation of the cube, default: (0,0,1)
    @type color: tuple
    @param color: color of the cube, default: (0.5,0.5,0.5)
    @rtype: blender object
    @return: a blender monkey that is added to the scene
    """
    bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0), rotation=rotation)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = color
    c.active_material = mat
    c.name = obj_name
    return c


def random_cone():
    """
    Adds a cone into the scene.
    Default position is the origin and it is randomly rotated.

    @rtype: blender object
    @return: a blender monkey that is added to the scene
    """
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0),
                                    rotation=(
                                        random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14)))
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def fixed_cone(obj_name="cone", rotation=(1, 1, 1), color=(0.5, 0.5, 0.5)):
    """
    Adds a cone into the scene with fixed position and orientation.

    @type obj_name: string
    @param obj_name: name of the object, default: "cone"
    @type rotation: tuple
    @param rotation: rotation of the cube, default: (1,1,1)
    @type color: tuple
    @param color: color of the cube, default: (0.5,0.5,0.5)
    @rtype: blender object
    @return: a blender cone that is added to the scene
    """
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 0), rotation=rotation)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = color
    c.active_material = mat
    c.name = obj_name
    return c


def random_torus():
    """
    Adds a torus into the scene.
    Default position is the origin and it is randomly rotated.

    @rtype: blender object
    @return: a blender torus that is added to the scene
    """
    bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0),
                                     rotation=(
                                         random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14))
                                     )
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = (random.random(), random.random(), random.random())
    c.active_material = mat
    return c


def fixed_torus(obj_name="torus", rotation=(1, 1, 1), color=(0.5, 0.5, 0.5)):
    """
    Adds a torus into the scene with fixed position and orientation.

    @type obj_name: string
    @param obj_name: name of the object, default: "torus"
    @type rotation: tuple
    @param rotation: rotation of the cube, default: (1,1,1)
    @type color: tuple
    @param color: color of the cube, default: (0.5,0.5,0.5)
    @rtype: blender object
    @return: a blender torus that is added to the scene
    """
    bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0), rotation=rotation)
    c = bpy.context.object
    mat = bpy.data.materials.new("Mat1")
    mat.diffuse_color = color
    c.active_material = mat
    c.name = obj_name
    return c


def random_object():
    """
    Adds a random object into the scene.

    @rtype: blender object
    @return: random cube, torus, cone or monkey
    """
    a = random.random()
    if a < 0.25:
        return random_cube()
    elif a < 0.50:
        return random_torus()
    elif a < 0.75:
        return randomCone()
    else:
        return randomMonkey()


def fixed_object(obj_name, rotation, color):
    """
    Adds a random object into the scene, with specific name, rotation and color parameters.

    @rtype: tuple(string, blender object)
    @return: type of an object and the object itself
    """
    a = random.random()
    if a < 0.25:
        return "cube", fixed_cube(obj_name=obj_name, rotation=rotation, color=color)
    elif a < 0.50:
        return "torus", fixed_torus(obj_name=obj_name, rotation=rotation, color=color)
    elif a < 0.75:
        return "cone", fixed_cone(obj_name=obj_name, rotation=rotation, color=color)
    else:
        return "monkey", fixed_monkey(obj_name=obj_name, rotation=rotation, color=color)


def random_lamp(obj_name, dist=7):
    """
    Adds a random light object into the scene.
    Default settings: point-type, ray_shadow, random energy between 0.5 and 3

    @type obj_name: string
    @param obj_name: name of the lamp
    @type dist: float
    @param dist: distance of the light from the origin, default: 7
    @rtype: lamp object
    @return: blender lamp object
    """
    position = random_sphere_position(dist)
    bpy.ops.object.lamp_add(type='POINT', location=position)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.energy = random.uniform(0.5, 3)
    bpy.context.object.name = obj_name


def fixed_lamp(obj_name="lamp", position=(0.5, 0.5, 0.5), lamp_energy=0.5):
    """
    Adds a light object into the scene with specific initial parameters.
    Default settings: point-type, ray_shadow.

    @type obj_name: string
    @param obj_name: name of the lamp
    @type position: tuple(3)
    @param position: position of the light, default: (0.5, 0.5, 0.5)
    @type lamp_energy: float
    @param lamp_energy: energy of the light, default: 0.5
    """
    bpy.ops.object.lamp_add(type='POINT', location=position)
    bpy.context.object.data.shadow_method = 'RAY_SHADOW'
    bpy.context.object.data.energy = lamp_energy
    bpy.context.object.name = obj_name


def random_camera(obj_name, dist):
    """
    Adds a random camera object into the scene.

    @type obj_name: string
    @param obj_name: name of the camera
    @type dist: float
    @param dist: distance of the camera from the origin
    """
    loc = random_sphere_position(dist)
    bpy.ops.object.camera_add(location=loc)
    bpy.context.object.name = obj_name
    camera = bpy.context.object
    looking_direction = mathutils.Vector(loc) - mathutils.Vector((0.0, 0.0, 0.0))
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat * mathutils.Vector((0.0, 0.0, random.uniform(10, 20))) + mathutils.Vector(
        [random.uniform(-3, 3), random.uniform(-3, 3), 0])
    bpy.context.scene.camera = camera


def fixed_camera(obj_name="cam", loc=(1, 1, 1)):
    """
    Adds a camera object into the scene with specific parameters.

    @type obj_name: string
    @param obj_name: name of the camera
    @type loc: tuple(3)
    @param loc: position of the camera, default: (1, 1, 1)
    """
    bpy.ops.object.camera_add(location=loc)
    bpy.context.object.name = obj_name
    camera = bpy.context.object
    looking_direction = mathutils.Vector(loc) - mathutils.Vector((0.0, 0.0, 0.0))
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    bpy.context.scene.camera = camera


def delete_all():
    """
    Deletes all objects from the scene: objects, lights and cameras.
    """
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
# Some mist option
world.mist_settings.depth = 15
world.mist_settings.height = 10

# Saving information about the generated configurations.
f = open("D:/kocka/images/test/data.txt", "w")

# Generates a list of name-rotation-color triples of objects.
list_objects_positions = []
for i in range(10):
    name = "obj" + str(i)
    rot = (random.uniform(0, math.pi), random.uniform(0, math.pi), random.uniform(0, math.pi))
    col = (random.random(), random.random(), random.random())
    list_objects_positions.append([name, rot, col])

# Generates a list of name-position-energy triples of lights
# then saves them into a data file just for information.
list_lights_positions = []
for i in range(10):
    name = "lamp" + str(i)
    pos = random_sphere_position(random.uniform(4, 7))
    energy = (i + 1)
    list_lights_positions.append([name, pos, energy])
    f.write(name + " -- position: " + str(pos) + ", energy: " + str(energy) + "\n")

# Generates a list of name-position pairs of cameras
# # then saves them into a data file just for information.
list_cameras_positions = []
for i in range(10):
    name = "cam" + str(i)
    pos = random_sphere_position(random.uniform(8, 15))
    list_cameras_positions.append([name, pos])
    f.write(name + " -- position: " + str(pos) + "\n")

# We generate all the possible object-camera-light configurations
# with 9 intensity of mist.
for obj in list_objects_positions:

    deleteAll()  # Clear the scene
    fix_obj = fixedObject(obj_name=obj[0], rot=obj[1], col=obj[2])  # Generate an object
    f.write(fix_obj[1].name + " -- type: "
            + fix_obj[0] + ", position: "
            + str(obj[1]) + ", color: "
            + str(obj[2]) + "\n")  # Write the data of the object into the data file.
    bpy.ops.mesh.primitive_plane_add(radius=10, location=absoluteLowestPoint())  # Default base plane

    for light in list_lights_positions:
        bpy.ops.object.select_by_type(type='LAMP')
        bpy.ops.object.delete(use_global=False)  # Clear all the existing lamps
        fixedLamp(obj_name=light[0], pos=light[1], ener=light[2])  # Create a new lamp in the scene

        for cam in list_cameras_positions:
            bpy.ops.object.select_by_type(type='CAMERA')
            bpy.ops.object.delete(use_global=False)  # Deletes all the existing camera
            fixedCamera(obj_name=cam[0], loc=cam[1])  # Creates a new camera

            # Render a picture with the specific object, lamp and camera (without mist).
            world.mist_settings.use_mist = False  # Mist is turn off, but the default is also off.
            bpy.context.scene.render.image_settings.file_format = 'PNG'
            bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_" \
                                                + cam[0] + "_mist0.png"
            bpy.context.scene.render.resolution_x = 200
            bpy.context.scene.render.resolution_y = 200
            bpy.ops.render.render(write_still=1)

            # Render a picture with the specific object, lamp and camera without shadow.
            bpy.data.objects[light[0]].data.shadow_method = 'NOSHADOW'
            bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_" \
                                                + cam[0] + "_mist0_noshadow.png"
            bpy.ops.render.render(write_still=1)

            # Render different pictures with the specific object, lamp, camera and several mist intensities.
            bpy.data.objects[light[0]].data.shadow_method = 'RAY_SHADOW'
            world.mist_settings.use_mist = True
            for j in range(9):
                world.mist_settings.intensity = (j + 1) / 10
                bpy.context.scene.render.filepath = "D:/kocka/images/test/" + light[0] + "_" + obj[0] + "_" \
                                                    + cam[0] + "_mist" + str(j + 1) + ".png"
                bpy.ops.render.render(write_still=1)

# Saves the information of the generated mists into the data file
for i in range(9):
    name = "mist" + str(i + 1)
    f.write(name + " -- intensity: " + str((i + 1) / 10) + "\n")
f.close()
