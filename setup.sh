#!/bin/bash

sudo apt update
sudo apt upgrade -y

sudo apt install -y \
ffmpeg \
libpango1.0-dev \
xvfb \
libgl1-mesa-dev \
libegl1-mesa-dev \
texlive-science \
texlive-fonts-extra \
texlive-latex-extra

python3 -m venv master
source master/bin/activate

git clone https://github.com/3b1b/manim.git manim

cd manim
python3 -m pip install -U pip
python3 -m pip install -e .
cd ..
pip install setuptools
pip install trimesh
pip install pywavefront
pip install PyOpenGL==3.1.1a1
ldconfig -p | grep libGL
ldconfig -p | grep libEGL

echo '

x() {

    xvfb-run manimgl test.py -sw 1080x1080

}

' >> ~/.bashrc

source ~/.bashrc

echo "Setup Complete ✅"