Module simple_pyspin
====================

Functions
---------

    
`list_cameras()`
:   Return a list of Spinnaker cameras.  Also initializes the PySpin
    `System`, if needed.  (See PySpin documentation for more info.)

Classes
-------

`Camera(index=0, lock=True)`
:   A class used to encapsulate a PySpin camera.
    
    Attributes
    ----------
    cam : PySpin Camera
    running : bool
        True if acquiring images
    camera_attributes : dictionary
        Contains links to all of the camera nodes which are settable
        attributes.
    camera_methods : dictionary
        Contains links to all of the camera nodes which are executable
        functions.
    camera_node_types : dictionary
        Contains the type (as a string) of each camera node.
    lock : bool
        If True, attribute access is locked down; after the camera is
        initialized, attempts to set new attributes will raise an error.  This
        is to prevent setting misspelled attributes, which would otherwise
        silently fail to acheive their intended goal.
    intialized : bool
        If True, init() has been called.
    
    In addition, many more virtual attributes are created to allow access to
    the camera properties.  A list of available names can be found as the keys
    of `camera_attributes` dictionary, and a documentation file for a specific
    camera can be genereated with the `document` method.
    
    Methods
    -------
    init()
        Initializes the camera.  Automatically called if the camera is opened
        using a `with` clause.
    close()
        Closes the camera and cleans up.  Automatically called if the camera
        is opening using a `with` clause.
    start()
        Start recording images.
    stop()
        Stop recording images.
    get_image()
        Return an image using PySpin's internal format.
    get_array()
        Return an image as a Numpy array.
    get_info(node)
        Return info about a camera node (an attribute or method).
    document()
        Create a Markdown documentation file with info about all camera
        attributes and methods.
    
    Parameters
    ----------
    index : int or str (default: 0)
        If an int, the index of the camera to acquire.  If a string,
        the serial number of the camera.
    lock : bool (default: True)
        If True, setting new attributes after initialization results in
        an error.

    ### Methods

    `close(self)`
    :   Closes the camera and cleans up.  Automatically called if the camera
        is opening using a `with` clause.

    `document(self)`
    :   Creates a MarkDown documentation string for the camera.

    `get_array(self, wait=True, get_chunk=False)`
    :   Get an image from the camera, and convert it to a numpy array.
        
        Parameters
        ----------
        wait : bool (default: True)
            If True, waits for the next image.  Otherwise throws an exception
            if there isn't one ready.
        get_chunk : bool (default: False)
            If True, returns chunk data from image frame.
        
        Returns
        -------
        img : Numpy array
        chunk : PySpin (only if get_chunk == True)

    `get_image(self, wait=True)`
    :   Get an image from the camera.
        
        Parameters
        ----------
        wait : bool (default: True)
            If True, waits for the next image.  Otherwise throws an exception
            if there isn't one ready.
        
        Returns
        -------
        img : PySpin Image

    `get_info(self, name)`
    :   Gen information on a camera node (attribute or method).
        
        Parameters
        ----------
        name : string
            The name of the desired node
        
        Returns
        -------
        info : dict
            A dictionary of retrieved properties.  *Possible* keys include:
                - `'access'`: read/write access of node.
                - `'description'`: description of node.
                - `'value'`: the current value.
                - `'unit'`: the unit of the value (as a string).
                - `'min'` and `'max'`: the min/max value.

    `init(self)`
    :   Initializes the camera.  Automatically called if the camera is opened
        using a `with` clause.

    `start(self)`
    :   Start recording images.

    `stop(self)`
    :   Stop recording images.

`CameraError(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException