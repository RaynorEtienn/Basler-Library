![pypylon](docs/images/Pypylon_grey_RZ_400px.png "pypylon")

The official python wrapper for the Basler pylon Camera Software Suite.

Background information about usage of pypylon, programming samples and jupyter notebooks can also be found at [pypylon-samples](https://github.com/basler/pypylon-samples).

**Please Note:**
This project is offered with no technical support by Basler AG.
You are welcome to post any questions or issues on [GitHub](https://github.com/basler/pypylon) or on [ImagingHub](https://www.imaginghub.com).

[![Build Status](https://github.com/basler/pypylon/workflows/build/badge.svg?branch=master)](https://github.com/basler/pypylon/actions)
[![Build Status](https://ci.appveyor.com/api/projects/status/45j4tydwdr0fv05p/branch/master?svg=true)](https://ci.appveyor.com/project/basler-oss/pypylon/branch/master)

# Getting Started

 * Install [pylon](https://www.baslerweb.com/pylon)
   This is strongly recommended but not mandatory. See [known issues](#known-issues) for further details.
 * Install pypylon: ```pip3 install pypylon```
   For more installation options and the supported systems please read the [Installation](#Installation) paragraph.
 * Look at [samples/grab.py](https://github.com/basler/pypylon/blob/master/samples/grab.py) or use the following snippet:

```python
from pypylon import pylon

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

# demonstrate some feature access
new_width = camera.Width.GetValue() - camera.Width.GetInc()
if new_width >= camera.Width.GetMin():
    camera.Width.SetValue(new_width)

numberOfImagesToGrab = 100
camera.StartGrabbingMax(numberOfImagesToGrab)

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data.
        print("SizeX: ", grabResult.Width)
        print("SizeY: ", grabResult.Height)
        img = grabResult.Array
        print("Gray value of first pixel: ", img[0, 0])

    grabResult.Release()
camera.Close()
```

# Installation
## Prerequisites
 * Installed [pylon](https://www.baslerweb.com/pylon)
   For the binary installation this is not mandatory but strongly recommended. See [known issues](#known-issues) for further details.
 * Installed [python](https://www.python.org/) with [pip](https://pip.pypa.io/en/stable/)

## Binary Installation
The easiest way to get pypylon is to install a prebuild wheel.
Binary releases for most architectures are available on [pypi](https://pypi.org)**.
To install pypylon open your favourite terminal and run:

```pip3 install pypylon```

The following versions are available on pypi:

 |                  | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
 |------------------|-----|-----|-----|-----|------|------|
 | Windows 64bit    | x   | x   | x   | x   |  x   |  x   |
 | Linux x86_64*    | x   | x   | x   | x   |  x   |  x   |
 | Linux armv7l*    | x   | x   | x   | x   |  x   |  x   |
 | Linux aarch64*   | x   | x   | x   | x   |  x   |  x   |
 | macOS x86_64**   | x   | x   | x   | x   |  x   |  x   |
 | macOS arm64**    |     |     | x   | x   |  x   |  x   |


> Additional Notes on binary packages:
> * (*) The linux binaries are manylinux_2_28 conformant.
    This is roughly equivalent to a minimum glibc version >= 2.28.
    :warning: You need at least pip 20.3 to install them.
> * (**) macOS binaries are built for macOS >= 11.0 (Big-Sur)

## Installation from Source
Building the pypylon bindings is supported and tested on Windows, Linux and macOS

You need a few more things to compile pypylon:
 * An installation of pylon SDK for your platform
 * A compiler for your system (Visual Studio on Windows, gcc on linux, xCode commandline tools on macOS)
 * Python development files (e.g. `sudo apt install python-dev` on linux)
 * [swig](http://www.swig.org) >= 4.0
   * For all 64bit platforms you can install the tool via `pip install swig`

To build pypylon from source:
```console
git clone https://github.com/basler/pypylon.git
cd pypylon
pip install .
```

If pylon SDK is not installed in a default location you have to specify the location from the environment
 * on Linux: `export PYLON_ROOT=<installation directory of pylon SDK>`
 * on macOS: `export PYLON_FRAMEWORK_LOCATION=<framework base folder that contains pylon.framework>`


# Development

Pull requests to pypylon are very welcome. To help you getting started with pypylon improvements, here are some hints:

## Starting Development
```console
python setup.py develop
```
This will "link" the local pypylon source directory into your python installation. It will not package the pylon libraries and always use the installed pylon.
After changing pypylon, execute `python setup.py build` and test...

## Running Unit Tests
> NOTE: The unit tests try to import `pypylon....`, so they run against the *installed* version of pypylon.
```console
pytest tests/....
```

# Known Issues
 * For USB 3.0 cameras to work on Linux, you need to install appropriate udev rules.
   The easiest way to get them is to install the official [pylon](http://www.baslerweb.com/pylon) package.
