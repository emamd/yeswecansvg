import re
import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert an SVG's font declarations so that they open in Illustrator.")
    parser.add_argument('filename', help="Name of SVG file to be cleaned. Will output as filename_cleaned.svg")
    parser.add_argument('-f', '--font', default="\'FranklinITCStd-Light\'", help="Font to use for replacement. Defaults to 'FranklinITCStd-Light'.")
    parser.add_argument('-b', '--bold_font', default="\'FranklinITCStd-Bold\'", help="Bold font to use for replacement. Defaults to 'FranklinITCStd-Bold'.")
    args = parser.parse_args()
    convert_svg_for_illustrator(args.filename, args.font, args.bold_font)


def convert_svg_for_illustrator(filename, font="\'FranklinITCStd-Light\'", bold_font="\'FranklinITCStd-Bold\'"):
    """
    Convert all font definitions into something older versions of Illustrator will recognize and not crap out on.
    Defaults to fonts we use at The Washington Post - Franklin Light and Franklin Bold.
    Currently handles standard and bold fonts.
    """
    font_string = 'font-family:'
    bold_string = 'font-weight:700'
    bold_string_2 = 'font-weight:bold'

    with open(filename, 'r+') as f:
        outfilename = filename.replace(".svg", "")
        outfilename = "%s_cleaned.svg" % outfilename

        with open(outfilename, 'w+') as outfile:

            for line in f:
                isfont = re.search(font_string, line)
                isbold = re.search(bold_string, line)

                if isfont:
                    if isbold:
                        line = re.sub('<text', '<text font-family="%s"' % bold_font, line)
                    else:
                        line = re.sub('<text', '<text font-family="%s"' % font, line)

                    # Remove font-family declaration
                    line = re.sub('font-family:[A-Za-z \-]+;', '', line)
                    # Remove font-weight declaration
                    line = re.sub('font-weight:(\d+|\w+);', '', line)
                    # Remove font-style declaration
                    line = re.sub('font-style:\w+;', '', line)

                outfile.write(line)

            print("Exported cleaned file to %s" % outfilename)
