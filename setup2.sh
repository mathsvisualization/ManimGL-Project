#!/bin/bash

sudo apt update
python3 -m venv master
source master/bin/activate
cd manim
pip install -e .
cd ..
pip install trimesh
pip install pywavefront
pip install PyOpenGL==3.1.1a1
ldconfig -p | grep libGL
ldconfig -p | grep libEGL

echo '

x() {

    xvfb-run manimgl "$1" -sw -r 1080x1080

}

' >> ~/.bashrc

source ~/.bashrc

echo "Setup Complete ✅"