# simple_pyspin
A Pythonic class-based wrapper for the FLIR PySpin Library.

More documentation can be found on [Github Pages](https://klecknerlab.github.io/simple_pyspin/), and the source can be found on [Github](https://github.com/klecknerlab/simple_pyspin).

# Why?
Why does this even exist, as the PySpin module already exists?  Because it's a pain to use, and difficult to wrap your head around basic operations.  For example, on some camera manually setting frame rate requires accessing methods by finding nodes, which is quite complicated.  This library makes it incredibly simple, and can also auto-document all the features of your *specific* cameras for easy reference.  

# Installation
1. If you don't already have them, I would recommend installing Numpy and the Python Imaging Library.  The easiest way to do this is to install a scientific Python distribution like [Anaconda](https://www.anaconda.com/distribution/).
2. [Install Spinnaker and PySpin from FLIR.](https://www.flir.com/products/spinnaker-sdk/)  
    - You will likely need to follow several manual steps after the Spinnaker installation to get PySpin ([Mac Instructions](https://www.flir.com/support-center/iis/machine-vision/application-note/getting-started-with-spinnaker-sdk-on-macos/,))
3. Install simple_pyspin module:
    - Install from PyPi: `pip install simple-pyspin`.
    - Download source from GitHub and use `setup.py`.

# Usage
See the examples directory of the source for these examples and more.

## Basic Usage
```python
# dead_simple.py

from simple_pyspin import Camera

with Camera() as cam: # Acquire and initialize Camera
    cam.start() # Start recording
    imgs = [cam.get_array() for n in range(10)] # Get 10 frames
    cam.stop() # Stop recording

print(imgs[0].shape, imgs[0].dtype) # Each image is a numpy array!
```
Note that as long as you open the camera using a `with` clause, you don't need to worry about initialization or cleanup of the camera -- the module handles this for you!

Equivalently, you can do this manually; the following code is functionally identical to the above:
```python
from simple_pyspin import Camera

cam = Camera() # Acquire Camera
cam.init() # Initialize camera

cam.start() # Start recording
imgs = [cam.get_array() for n in range(10)] # Get 10 frames
cam.stop() # Stop recording

cam.close() # You should explicitly clean up

print(imgs[0].shape, imgs[0].dtype) # Each image is a numpy array!
```

## Changing Camera Settings
Here is a more complicated example, which manual changes a number of settings, and saves a number of images using PIL.
```python
# manual_setup.py

from simple_pyspin import Camera
from PIL import Image
import os

with Camera() as cam: # Initialize Camera
    # Set the area of interest (AOI) to the middle half
    cam.Width = cam.SensorWidth // 2
    cam.Height = cam.SensorHeight // 2
    cam.OffsetX = cam.SensorWidth // 4
    cam.OffsetY = cam.SensorHeight // 4

    # If this is a color camera, get the image in RGB format.
    if 'Bayer' in cam.PixelFormat:
        cam.PixelFormat = "RGB8"

    # To change the frame rate, we need to enable manual control
    cam.AcquisitionFrameRateAuto = 'Off'
    cam.AcquisitionFrameRateEnabled = True
    cam.AcquisitionFrameRate = 20

    # To control the exposure settings, we need to turn off auto
    cam.GainAuto = 'Off'
    # Set the gain to 20 dB or the maximum of the camera.
    gain = min(20, cam.get_info('Gain')['max'])
    print("Setting gain to %.1f dB" % gain)
    cam.Gain = gain
    cam.ExposureAuto = 'Off'
    cam.ExposureTime = 10000 # microseconds

    # If we want an easily viewable image, turn on gamma correction.
    # NOTE: for scientific image processing, you probably want to
    #    _disable_ gamma correction!
    try:
        cam.GammaEnabled = True
        cam.Gamma = 2.2
    except:
        print("Failed to change Gamma correction (not avaiable on some cameras).")

    cam.start() # Start recording
    imgs = [cam.get_array() for n in range(10)] # Get 10 frames
    cam.stop() # Stop recording

# Make a directory to save some images
output_dir = 'test_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Saving images to: %s" % output_dir)

# Save them
# NOTE: images may be very dark or bright, depending on the camera lens and
#   room conditions!
for n, img in enumerate(imgs):
    Image.fromarray(img).save(os.path.join(output_dir, '%08d.png' % n))
```

# License

Copyright 2019 Dustin Kleckner

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
