# Blender_batch_render_for_sprite_atlas
Simple script to automate rendering of animations at different angles

ImageMagick required!
https://imagemagick.org

Script must be loaded in blender Text editor.
After that fill your data in the lines with comments.
Script uses blender output path.

ImageMagick creates spritesheet horizontal line per rotation angle and vertical line per frame.
        Frame_01    Frame_02    Frame_03    Frame_04  etc
Angle_0
Angle_45
Angle_90
etc

If you want to rotate your camera around object then create Empty at rotation point, parent camera to that Empty and paste name of Empty to script
