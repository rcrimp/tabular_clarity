from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.misc.transform import Transform
# import Identity
from fontTools.misc.transform import Identity
import os

def make_monospaced(font_path, output_path):
    font = TTFont(font_path)

    # Get the advance widths for the numeric characters (0-9)
    digit_glyphs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

    # Find maximum advance width of digits
    digit_advance_widths = [font["hmtx"].metrics[glyph][0] for glyph in digit_glyphs if glyph in font["hmtx"].metrics]
    if not digit_advance_widths:
        print(f"No numeric characters found in {font_path}")
        return

    max_advance_width = max(digit_advance_widths)

    for digit in digit_glyphs:
        if digit in font["hmtx"].metrics:
            old_width = font["hmtx"].metrics[digit][0]
            offset = (max_advance_width - old_width) // 2  # Calculate centering offset

            # print(max_advance_width, old_width, offset)

            # Update horizontal metrics (advance width)
            font["hmtx"].metrics[digit] = (max_advance_width, font["hmtx"].metrics[digit][1])

            glyph = font["glyf"][digit]

            # get vector points 
            glyph_points = glyph.getCoordinates(font["glyf"])
            # get glyph bounding box
            # xMin, yMin, xMax, yMax = glyph.getBoundingBox(font["glyf"])
            # get glyph width
            # glyph_width = xMax - xMin

            new_points = []
            for p in glyph_points[0]:
                x, y = p
                x += offset
                y += 0.5
                p = (x, y)
                # save p in glyph
                new_points.append(p)
            glyph_points = (new_points, glyph_points[1], glyph_points[2])
        

            # save
            font["glyf"][digit] = glyph

            

            # if False and not glyph.isComposite():
            #     # Get the existing glyph bounding box
            #     xMin, xMax = glyph.xMin, glyph.xMax
            #     glyph_width = xMax - xMin

            #     # Calculate the actual offset to center the glyph within the new width
            #     center_offset = (max_advance_width - glyph_width) // 2 - xMin

            #     # Apply the offset to the glyph outlines
            #     glyphPen = TTGlyphPen(font.getGlyphSet())
            #     transformPen = TransformPen(glyphPen, Transform(1, 0, 0, 1, 0, 0))
            #     print(digit, offset)
            #     glyph.draw(transformPen, font["glyf"])

            #     # Save the transformed glyph back to the font
            #     font["glyf"][digit] = glyphPen.glyph()

    # Update font metadata for monospacing digits
    # font["OS/2"].panose.bProportion = 9  # Monospaced
    # font["OS/2"].xAvgCharWidth = max_advance_width
    # font["post"].isFixedPitch = 1

    # Update the font properties for monospacing digits
    # font["OS/2"].panose.bProportion = 3  # 9 is monospace, 3 is "modern"
    # font["OS/2"].xAvgCharWidth = max_advance_width
    # font["post"].isFixedPitch = 0

    # Save the modified font
    font.save(output_path)

dir_in = "./ClarityCity"
dir_out = "./TabularClarityCity"

# Replace with your input and output file paths
for file in os.listdir(dir_in):
    input_file = os.path.join(dir_in, file)
    output_file = os.path.join(dir_out, f'Tabular_{file}')
    make_monospaced(input_file, output_file)
