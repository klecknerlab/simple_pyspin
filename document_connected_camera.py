from simple_pyspin import Camera, list_cameras
import os
import time
import gc


output_dir = os.path.join('docs', 'cameras')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


with Camera() as cam:
    print('Resetting camera...')
    cam.DeviceReset()


print('Waiting 5 seconds for it to wake up...')
time.sleep(5)

for n in range(10):
    cl = list_cameras()
    n_cam = cl.GetSize()
    cl.Clear()
    if n_cam:
        break
    time.sleep(1)


print('Reconnecting camera...')
with Camera() as cam:
    cam_name = cam.DeviceVendorName.strip() + ' ' + cam.DeviceModelName.strip()
    ofn = os.path.join(output_dir, cam_name.replace(' ', '_') + '.md')
    print('Generating documentation in file: %s' % ofn)

    with open(ofn, 'wt') as f:
        f.write(cam.document())
