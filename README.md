# ManimGL on Termux + Ubuntu (ARM64) — Installation & Troubleshooting

A practical checklist for installing ManimGL in Ubuntu running inside Termux/proot on Android ARM64, especially when using Python 3.14.

> **Important:** Package names, compiler paths, and Python versions can differ across Ubuntu releases. These notes reflect one setup where Ubuntu's native `gcc` worked, while `aarch64-linux-gnu-gcc` resolved to a Termux Clang wrapper.

## 1. Install system dependencies

Inside the Ubuntu environment:

```bash
sudo apt update
sudo apt install build-essential gcc g++ python3.14-dev libpython3.14-dev libc6-dev
```

If your Ubuntu release uses a different Python version, replace `python3.14-dev` and `libpython3.14-dev` with the matching packages available for that release.

## 2. Enter the project and activate the virtual environment

Adjust the environment path if yours is named differently:

```bash
cd ~/manim
source bin/activate
```

## 3. Install ManimPango using Ubuntu's native compiler

In the setup documented here, the following command successfully installed `manimpango`:

```bash
CC=/usr/bin/gcc CXX=/usr/bin/g++ \
LDSHARED="/usr/bin/gcc -shared" \
python -m pip install --no-cache-dir manimpango
```

Then install the current project in editable mode:

```bash
python -m pip install -e .
```

Check that ManimGL starts:

```bash
manimgl --help
```

## 4. Troubleshooting common errors

### Error: `aarch64-linux-gnu-gcc` not found

Check which compiler is being used:

```bash
which aarch64-linux-gnu-gcc
which gcc
gcc --version
gcc -dumpmachine
gcc -print-search-dirs
```

Install standard build tools if needed:

```bash
sudo apt install build-essential gcc g++
```

**Note:** In the documented setup, `/usr/local/bin/aarch64-linux-gnu-gcc` was a Termux-provided Clang wrapper, while `gcc` was Ubuntu's native GCC. Do not assume both names point to the same compiler.

### Error: `Python.h` or `pyconfig.h` not found

Install Python development headers matching the Python interpreter used in the virtual environment:

```bash
sudo apt install python3.14-dev libpython3.14-dev
```

Inspect the installed configuration headers:

```bash
dpkg -L libpython3.14-dev | grep pyconfig.h
```

For this setup, the headers included:

```text
/usr/include/aarch64-linux-gnu/python3.14/pyconfig.h
/usr/include/python3.14/pyconfig.h
```

### Error: `bits/wordsize.h` not found

Reinstalling Ubuntu's C library development headers may help if files are missing:

```bash
sudo apt install --reinstall libc6-dev
```

If the error persists, check which compiler is running and whether it is using Ubuntu's system include paths. In the documented setup, reinstalling `libc6-dev` alone did **not** fix the problem.

## 5. Test whether native GCC can read Python headers

Create a tiny test source file:

```bash
cat > /tmp/testpython.c <<'EOF'
#include <Python.h>
int main(void) { return 0; }
EOF
```

Compile it using Ubuntu's native GCC:

```bash
gcc -I/usr/include/python3.14 \
  -c /tmp/testpython.c \
  -o /tmp/testpython.o
```

If this finishes without output or errors, the header compilation test succeeded. If your Python version is different, update the include path accordingly.

## 6. Quick recovery sequence

After dependencies are installed and the virtual environment is activated, try:

```bash
cd ~/manim
CC=/usr/bin/gcc CXX=/usr/bin/g++ \
LDSHARED="/usr/bin/gcc -shared" \
python -m pip install --no-cache-dir manimpango

python -m pip install -e .
manimgl --help
```

If any command fails, copy the **last 20–30 lines** of the error output before changing compiler symlinks or deleting system files.

## Notes

- Run Ubuntu `apt` commands **inside Ubuntu**, not at the Termux shell prompt.
- `sudo` may be unnecessary if your Ubuntu proot session is already running as root.
- Use `python -m pip` so pip is tied to the currently active Python interpreter.
- Do not blindly replace or symlink `aarch64-linux-gnu-gcc`; first inspect what it points to.
- This is a troubleshooting guide for one ARM64 setup, not a guarantee that every ManimGL dependency supports every Python version.
