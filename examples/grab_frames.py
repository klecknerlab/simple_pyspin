from simple_pyspin import Camera
import time
from PIL import Image
import os

num_frames = 50

with Camera() as cam:
    # If this is a color camera, request the data in RGB format.
    if 'Bayer' in cam.PixelFormat:
        cam.PixelFormat = "RGB8"

    # Get images from the full sensor
    cam.OffsetX = 0
    cam.OffsetY = 0
    cam.Width = cam.SensorWidth
    cam.Height = cam.SensorHeight

    print('Opened camera: %s (#%s)' % (cam.DeviceModelName, cam.DeviceSerialNumber))

    print('Recording...')

    # Start recording
    cam.start()
    start = time.time()

    # Get 100 images as numpy arrays
    imgs = [cam.get_array() for n in range(num_frames)]

    # Stop recording
    el = time.time() - start
    cam.stop()

print('Acquired %d images in %.2f s (~ %.1f fps)' % (len(imgs), el, len(imgs)/el))

# Make a directory to save some images
output_dir = 'test_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print('Saving to "%s"' % output_dir)

# Save them
for n, img in enumerate(imgs):
    Image.fromarray(img).save(os.path.join(output_dir, '%08d.jpg' % n))



#     # cam.VideoMode = "Mode7"
#     # cam.PixelFormat = "RGB8"
#     # cam.OffsetX = 0
#     # cam.OffsetY = 0
#     # cam.Width = cam.WidthMax
#     # cam.Height = cam.HeightMax
#     # cam.OffsetX = (cam.WidthMax - cam.Width) // 2
#     # cam.OffsetY = (cam.HeightMax - cam.Height) // 2
#     # cam.ChunkModeActive = True
#     # cam.ChunkSelector = "FrameCounter"
#     # cam.ChunkEnable = True
#
#     print('Reported frame rate: %.2f Hz' % cam.AcquisitionFrameRate)
#     # print(cam.PayloadSize) # This seems to prevent a bug where sometimes the camera doesn't start
#
#     imgs = []
#     counts = []
#
#
#     tfc = cam.TransmitFailureCount
#     print('Failed transmissions since last reset: %d' % tfc)
#
#     num_frames = 10
#
#     cam.start()
#     start = time.time()
#
#     # time.sleep(5)
#     for n in range(num_frames):
#         try:
#             img, chunk = cam.get_array(get_chunk=True)
#             imgs.append(img)
#             counts.append(chunk.GetFrameID())
#             # if not (n%100): print(n, counts[-1])
#             ntfc = cam.TransmitFailureCount
#             if ntfc != tfc:
#                 print('!! detected failed transmission !!')
#                 tfc = ntfc
#         except:
#             print('Exception at %d frames' % n)
#             break
#
#     el = time.time() - start
#
#     cam.stop()
#
#     print('Acquired %d images in %.2f s (%.2f Hz).' % (len(imgs), el, len(imgs)/el))
#     print('Missed frames: %d' % (num_frames - 1 - counts[-1]))
#     # print(dir(chunks[0]))
#     # chunk = chunks[-1]
#     #
#     # for attr in dir(chunk):
#     #     if attr.startswith('Get'):
#     #         try:
#     #             val = getattr(chunk, attr)()
#     #             print('%s -> %s' % (attr, val))
#     #         except:
#     #             print('Error calling "%s"' % attr)
#
# # print(imgs[0])
