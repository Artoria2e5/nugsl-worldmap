#!/usr/bin/env python

from distutils.core import setup

long_description = """

This program can be used to refactor a Robinson projection world map,
offered through the WikiMedia project, in several useful ways.  A
flattened version of the map can be produced, or the map can be
rotated to an arbitrary line of longitude.  Pinpoint marks can be
added at specific coordinates, and the stylesheet of the map can be
rewritten, giving full control over colours and other aspects of
the map's appearance.
""".strip()

data = []
data.append("data/BlankMap-World6.svg")

setup(
    name="nugsl-worldmap",
    version="1.16",
    description="WikiMedia world map tool",
    author="Frank Bennett",
    author_email="biercenator@gmail.com",
    maintainer="Frank Bennett",
    maintainer_email="biercenator@gmail.com",
    url="http://gsl-nagoya-u.net/",
    packages=[
        "nugsl_worldmap",
        "nugsl_worldmap.StyleSheet",
        "nugsl_worldmap.OutPut",
        "nugsl_worldmap.PinPoint",
        "nugsl_worldmap.HtmlMerge",
        "nugsl_worldmap.ImageMap",
        "nugsl_worldmap.ViewPort",
        "nugsl_worldmap.Convert",
        "nugsl_worldmap.Config",
        "nugsl_tagtool",
    ],
    provides=["nugsl_worldmap"],
    scripts=["scripts/nugsl-worldmap"],
    data_files=[("share/nugsl-worldmap/data", data)],
    long_description=long_description,
    platforms=["any"],
    license="http://www.gnu.org/copyleft/gpl.html",
)
