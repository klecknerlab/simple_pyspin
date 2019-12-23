from easy_pyspin import Camera

with Camera() as cam: # Initialize Camera
    cam.start() # Start recording
    imgs = [cam.get_array() for n in range(10)] # Get 10 frames
    cam.stop() # Stop recording

print(imgs[0].shape, imgs[0].dtype) # Each image is a numpy array!
