import bpy, math, subprocess, os

ModelName = "Skele"
KeepLastFrame = True

Paths = []
Hor_paths = []
output_folder = bpy.context.scene.render.filepath
cache_outfolder = output_folder

_scene = bpy.context.scene
target_obj = bpy.data.objects["rig"]
target_obj.rotation_mode = 'XYZ'

app = 'magick.exe'
appPath = os.path.join("D:/Programy/ImageMagick/", app)

rotate_by = 45
angle = 0
target_obj.rotation_euler = ( 0, 0, math.radians(angle))

for x in range(0,int(360/rotate_by)):
    for f in range(_scene.frame_start, _scene.frame_end+KeepLastFrame):
        _scene.frame_set(f)
        _scene.render.filepath = output_folder + "\{0}_{1}_{2}.png".format(angle,ModelName, f)
        Paths.append(_scene.render.filepath)
        bpy.ops.render.render(write_still=True, use_viewport=True)
        
    commandLine = [app, "convert", "+append"]
    commandLine.extend(Paths)
    commandLine.extend([output_folder+"\{0}-line_{1}.png".format(ModelName ,angle)])
    Hor_paths.append(output_folder+"\{0}-line_{1}.png".format(ModelName ,angle))
    Paths.clear()
    angle += 45
    target_obj.rotation_euler = ( 0, 0, math.radians(angle))
    subprocess.call(commandLine, executable=appPath)

commandLine = [app, "convert", "-append"]
commandLine.extend(Hor_paths)
commandLine.extend([output_folder+"\{0}.png".format(ModelName)])
subprocess.call(commandLine, executable=appPath)

_scene.render.filepath = cache_outfolder
