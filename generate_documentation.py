import pdoc
import os
import glob

context = pdoc.Context()
module = pdoc.Module('simple_pyspin', context=context)

with open(os.path.join('docs', 'simple_pyspin.md'), 'wt') as f:
    f.write(module.text())

cam_dir = os.path.join('docs', 'cameras')
cam_list = []
for cam in glob.glob(os.path.join(cam_dir, '*.md')):
    cam_list.append(os.path.split(cam)[-1])

with open(os.path.join('docs', 'index.md'), 'wt') as f:
    f.write('''
This page contains the documentation for the `simple_pyspin` Python library.
It is probably easiest to learn by example ([see below](An-instructive-example)), and by consulting the attributes for your specific camera.

  - [Automatically generated documentation of the python module can be found here.](simple_pyspin.md)
  - [Github Repository](https://github.com/klecknerlab/simple_pyspin)

## Documented cameras

{}

*If you have cameras you would like to add to this list, run `document_connect_camera.py` from the source code and send the resulting output in `docs/cameras` to `dkleckner@ucmerced.edu`.*

## An instructive example
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
'''.format('\n'.join('  - [%s](cameras/%s)' % (os.path.splitext(cam)[0].replace('_', ' '), cam) for cam in cam_list)))
