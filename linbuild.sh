echo "Building: $1"
nuitka $1 --recurse-directory . --output-dir=bin/lin --recurse-to=utils
