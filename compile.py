#!/usr/bin/env python3

import sys
import glob
import subprocess
import shutil

outdir = "bin/{}".format(sys.platform)
for solution in glob.glob("euler_*.py"):
    subprocess.call(["nuitka", solution, "--recurse-directory", ".",
                     "--output-dir={}".format(outdir), "--recurse-to=utils"])

for resource in glob.glob("*.txt"):
    shutil.copy(resource,outdir)