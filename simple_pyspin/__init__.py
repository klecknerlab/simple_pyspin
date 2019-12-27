#
# Copyright 2019 Dustin Kleckner
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import PySpin

class CameraError(Exception):
    pass

_SYSTEM = None

def list_cameras():
    '''Return a list of Spinnaker cameras.  Also initializes the PySpin
    `System`, if needed.  (See PySpin documentation for more info.)'''

    global _SYSTEM

    if _SYSTEM is None:
        _SYSTEM = PySpin.System.GetInstance()

    return _SYSTEM.GetCameras()


class Camera:
    '''
    A class used to encapsulate a PySpin camera.

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
    '''

    def __init__(self, index=0, lock=True):
        '''
        Parameters
        ----------
        index : int or str (default: 0)
            If an int, the index of the camera to acquire.  If a string,
            the serial number of the camera.
        lock : bool (default: True)
            If True, setting new attributes after initialization results in
            an error.
        '''
        super().__setattr__("camera_attributes", {})
        super().__setattr__("camera_methods", {})
        super().__setattr__("camera_node_types", {})
        super().__setattr__("initialized", False)
        super().__setattr__("lock", lock)

        cam_list = list_cameras()
        # if debug: print('Found %d camera(s)' % cam_list.GetSize())
        if not cam_list.GetSize():
            raise CameraError("No cameras detected.")
        if isinstance(index, int):
            self.cam = cam_list.GetByIndex(index)
        elif isinstance(index, str):
            self.cam = cam_list.GetBySerial(index)
        cam_list.Clear()
        self.running = False

    _rw_modes = {
        PySpin.RO: "read only",
        PySpin.RW: "read/write",
        PySpin.WO: "write only",
        PySpin.NA: "not available"
    }

    _attr_types = {
        PySpin.intfIFloat: PySpin.CFloatPtr,
        PySpin.intfIBoolean: PySpin.CBooleanPtr,
        PySpin.intfIInteger: PySpin.CIntegerPtr,
        PySpin.intfIEnumeration: PySpin.CEnumerationPtr,
        PySpin.intfIString: PySpin.CStringPtr,
    }

    _attr_type_names = {
        PySpin.intfIFloat: 'float',
        PySpin.intfIBoolean: 'bool',
        PySpin.intfIInteger: 'int',
        PySpin.intfIEnumeration: 'enum',
        PySpin.intfIString: 'string',
        PySpin.intfICommand: 'command',
    }

    def init(self):
        '''Initializes the camera.  Automatically called if the camera is opened
        using a `with` clause.'''

        self.cam.Init()

        for node in self.cam.GetNodeMap().GetNodes():
            pit = node.GetPrincipalInterfaceType()
            name = node.GetName()
            self.camera_node_types[name] = self._attr_type_names.get(pit, pit)
            if pit == PySpin.intfICommand:
                self.camera_methods[name] = PySpin.CCommandPtr(node)
            if pit in self._attr_types:
                self.camera_attributes[name] = self._attr_types[pit](node)

        self.initialized = True

    def __enter__(self):
        self.init()
        return self

    def close(self):
        '''Closes the camera and cleans up.  Automatically called if the camera
        is opening using a `with` clause.'''

        self.stop()
        del self.cam
        self.camera_attributes = {}
        self.camera_methods = {}
        self.camera_node_types = {}
        self.initialized = False
        # self.system.ReleaseInstance()

    def __exit__(self, type, value, traceback):
        self.close()

    def start(self):
        'Start recording images.'
        if not self.running:
            self.cam.BeginAcquisition()
            self.running = True

    def stop(self):
        'Stop recording images.'
        if self.running:
            self.cam.EndAcquisition()
        self.running = False

    def get_image(self, wait=True):
        '''Get an image from the camera.

        Parameters
        ----------
        wait : bool (default: True)
            If True, waits for the next image.  Otherwise throws an exception
            if there isn't one ready.

        Returns
        -------
        img : PySpin Image
        '''
        return self.cam.GetNextImage(PySpin.EVENT_TIMEOUT_INFINITE if wait else PySpin.EVENT_TIMEOUT_NONE)

    def get_array(self, wait=True, get_chunk=False):
        '''Get an image from the camera, and convert it to a numpy array.

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
        '''

        img = self.cam.GetNextImage(PySpin.EVENT_TIMEOUT_INFINITE if wait else PySpin.EVENT_TIMEOUT_NONE)

        if get_chunk:
            return img.GetNDArray(), img.GetChunkData()
        else:
            return img.GetNDArray()

    def __getattr__(self, attr):
        if attr in self.camera_attributes:

            prop = self.camera_attributes[attr]
            if not PySpin.IsReadable(prop):
                raise CameraError("Camera property '%s' is not readable" % attr)

            if hasattr(prop, "GetValue"):
                return prop.GetValue()
            elif hasattr(prop, "ToString"):
                return prop.ToString()
            else:
                raise CameraError("Camera property '%s' is not readable" % attr)
        elif attr in self.camera_methods:
            return self.camera_methods[attr].Execute
        else:
            raise AttributeError(attr)


    def __setattr__(self, attr, val):
        if attr in self.camera_attributes:

            prop = self.camera_attributes[attr]
            if not PySpin.IsWritable(prop):
                raise CameraError("Property '%s' is not currently writable!" % attr)

            if hasattr(prop, 'SetValue'):
                prop.SetValue(val)
            else:
                prop.FromString(val)

        elif attr in self.camera_methods:
            raise CameraError("Camera method '%s' is a function -- you can't assign it a value!" % attr)
        else:
            if attr not in self.__dict__ and self.lock and self.initialized:
                raise CameraError("Unknown property '%s'." % attr)
            else:
                super().__setattr__(attr, val)


    def get_info(self, name):
        '''Gen information on a camera node (attribute or method).

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
        '''
        info = {'name': name}

        if name in self.camera_attributes:
            node = self.camera_attributes[name]
        elif name in self.camera_methods:
            node = self.camera_methods[name]
        else:
            raise ValueError("'%s' is not a camera method or attribute" % name)

        info['type'] = self.camera_node_types[name]

        if hasattr(node, 'GetAccessMode'):
            access = node.GetAccessMode()
            info['access'] = self._rw_modes.get(access, access)
            # print(info['access'])
            if isinstance(info['access'], str) and 'read' in info['access']:
                info['value'] = getattr(self, name)

        # print(info)
        if info.get('access') != 0:
            for attr in ("description", "unit", "min", "max"):
                fname = "Get" + attr.capitalize()
                f = getattr(node, fname, None)
                if f:
                    info[attr] = f()
            if hasattr(node, 'GetEntries'):
                entries = []
                entry_desc = []
                has_desc = False
                for entry in node.GetEntries():
                    entries.append(entry.GetName().split('_')[-1])
                    entry_desc.append(entry.GetDescription().strip())
                    if entry_desc[-1]: has_desc = True
                info['entries'] = entries
                if has_desc:
                    info['entry_descriptions'] = entry_desc

        return info


    def document(self):
        '''Creates a MarkDown documentation string for the camera.'''
        lines = [self.DeviceVendorName.strip() + ' ' + self.DeviceModelName.strip()]
        lines.append('=' * len(lines[-1]))
        lines.append('')
        lines.append('*Version: %s*' % getattr(self, 'DeviceVersion', '?'))
        lines.append('')

        lines.append('Attributes')
        lines.append('-' * len(lines[-1]))
        lines.append('')

        for attr in sorted(self.camera_attributes.keys()):
            if '_' in attr:
                continue
            # print(attr)
            info = self.get_info(attr)
            if not info.get('access', 0):
                continue
            lines.append('`%s` : `%s`  ' % (attr, info.get('type', '?')))
            lines.append('  ' + info.get('description', '(no description provided)'))
            lines.append('  - default access: %s' % info.get('access', '?'))
            if 'value' in info:
                lines.append('  - default value: `%s`' % repr(info['value']))
            if 'unit' in info and info['unit'].strip():
                lines.append('  - unit: %s' % info['unit'])
            if 'min' in info and 'max' in info:
                lines.append('  - default range: %s - %s' % (info['min'], info['max']))
            if 'entries' in info:
                if 'entry_descriptions' in info:
                    lines.append('  - possible values:')
                    for e, ed in zip(info['entries'], info['entry_descriptions']):
                        if ed:
                            lines.append("    - `'%s'`: %s" % (e, ed))
                        else:
                            lines.append("    - `'%s'`" % e)
                else:
                    lines.append('  - possible values: %s' % (', '.join("`'%s'`" % e for e in info['entries'])))

            lines.append('')

        lines.append('Commands')
        lines.append('-' * len(lines[-1]))
        lines.append('')
        lines.append('**Note: the camera recording should be started/stopped using the `start` and `stop` methods, not any of the functions below (see simple_pyspin documentation).**')
        lines.append('')

        for attr in sorted(self.camera_methods.keys()):
            if '_' in attr:
                continue
            # print(attr)
            info = self.get_info(attr)
            lines.append('`%s()`:  ' % (attr))
            lines.append('  ' + info.get('description', '(no description provided)'))
            lines.append('  - default access: %s' % info.get('access', '?'))
            lines.append('')

        return '\n'.join(lines)


    # def method_info(self, depth=1):
    #     '''Dump a string containing info about all the dynamically generated
    #     camera methods.
    #
    #     Attributes
    #     ----------
    #     depth : int (default: 1)
    #         * 0: Return names.
    #         * 1: Also return descriptions.
    #
    #     Returns
    #     -------
    #     info : str
    #         A string containing the requested attribute info.
    #         '''
    #
    #     lines = []
    #
    #     for name, attr in sorted(self.camera_methods.items()):
    #         # prop = getattr(self.cam, attr)
    #
    #         if not hasattr(attr, "GetAccessMode"):
    #             continue
    #
    #         mode = attr.GetAccessMode()
    #         # if not (mode == PySpin.WO or mode == PySpin.RW):
    #             # continue
    #         # print(attr, mode)
    #
    #         lines.append(name + '()')
    #
    #         if depth >= 1:
    #             if hasattr(attr, 'GetDescription'):
    #                 desc = attr.GetDescription().strip()
    #                 if desc:
    #                     lines[-1] += ':'
    #                     lines.append('    ' + desc)
    #             lines.append('')
    #
    #     return '\n'.join(lines)
    #
    # def attribute_info(self, depth=2, suppress_underscore=True):
    #     '''Dump a string containing info about all the dynamically generated
    #     camera attributes.
    #
    #     Attributes
    #     ----------
    #     depth : int (default: 2)
    #         * 0: Return names, r/w access, and current value.
    #         * 1: Also return descriptions.
    #         * 2: Also return valid values.
    #         * 3: Also return description of values (when available).
    #     suppress_underscore : bool (default: True)
    #         If True, doesn't produce output for any attribute with an
    #         underscore in it.  This suppress all the sub-attributes from the
    #         output, which is usually desirable.
    #
    #     Returns
    #     -------
    #     info : str
    #         A string containing the requested attribute info.
    #         '''
    #
    #     lines = []
    #
    #     for name, attr in sorted(self.camera_attributes.items()):
    #     # for attr in dir(self.cam):
    #     #     if attr.startswith('_'):
    #     #         continue
    #         #
    #         # prop = getattr(self.cam, attr)
    #         # if not hasattr(prop, "GetAccessMode"):
    #         #     continue
    #
    #
    #         # print(name)
    #         if suppress_underscore and '_' in name:
    #             continue
    #
    #         mode = self._rw_modes.get(attr.GetAccessMode(), None)
    #
    #         if not mode:
    #             continue
    #
    #         if 'read' in mode:
    #
    #             try:
    #                 val = getattr(self, name)
    #                 # if hasattr(attr, "GetEntries"):
    #                 #     val = repr(attr.ToString())
    #                 # else:
    #                 #     val = repr(attr.GetValue())
    #             except:
    #                 val = '-- error reading value --'
    #
    #         lines.append("%s (current access: %s%s)" % (name, mode,
    #             (", value: %s" % val) if 'read' in mode else ''))
    #
    #         if depth < 1:
    #             # lines.append('')
    #             continue
    #         lines[-1] += ':'
    #
    #         desc = attr.GetDescription()
    #         if desc:
    #             lines.append('    ' + desc)
    #
    #         if depth < 2 or 'write' not in mode:
    #             lines.append('')
    #             continue
    #
    #
    #         if hasattr(attr, "GetEntries"):
    #             entries = [
    #                 "'%s'" % entry.GetName().split('_')[-1]
    #                 for entry in attr.GetEntries()]
    #
    #             if depth < 3:
    #                 lines.append('    Possible values: ' + ', '.join(entries))
    #             else:
    #                 has_desc = False
    #                 descs = []
    #                 for entry in attr.GetEntries():
    #                     if hasattr(entry, 'GetDescription'):
    #                         desc = entry.GetDescription().strip()
    #                         if desc:
    #                             has_desc = True
    #                             descs.append(desc)
    #                         else:
    #                             descs.append('(no description)')
    #                     else:
    #                         descs.append('(no description)')
    #
    #                 if has_desc:
    #                     lines.append('    Possible values:')
    #                     for name, desc in zip(entries, descs):
    #                         lines.append('      * %s: %s' % (name, desc))
    #                 else:
    #                     lines.append('    Possible values: ' + ', '.join(entries))
    #         elif hasattr(attr, "GetMin") and hasattr(attr, "GetMax"):
    #             lines.append('    Range: %s - %s' % (attr.GetMin(), attr.GetMax()))
    #             if hasattr(attr, "GetUnit"):
    #                 unit = attr.GetUnit().strip()
    #                 if unit: lines[-1] += ' (%s)' % attr.GetUnit()
    #         lines.append('')
    #
    #     return '\n'.join(lines)
