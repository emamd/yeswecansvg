# yeswecansvg
Are you tired of Illustrator telling you it CANT open an SVG? Apparently, the bug is caused due to older versions of illustrator not knowing how to deal with fonts it doesn't recognize. `yeswecansvg` translates any font declarations into something Illustrator will know how to handle.

## Installation

You can install with pip.

```bash
$ pip install yeswecansvg
```

## Usage
Just type `yeswecansvg <svg_filename>`. The script returns a file named `<svg_filename>_cleaned.svg`, which you should be able to open in Illustrator.


## Additional options
`--font`, `-f` - What font to replace with. Currently this defaults to `FranklinITCStd-Light`, which we use at The Washington Post.

`--bold_font`, `-b` - Bold replacement font. This defaults to `FranklinITCStd-Bold`


## Bugs?
Line them up in the [issues](https://github.com/emamd/yeswecansvg/issues).