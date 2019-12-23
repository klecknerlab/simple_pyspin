Point Grey Research Chameleon3 CM3-U3-31S4C
===========================================

*Version: FW:v1.10.3.00 FPGA:v2.02*

Attributes
----------

`AccessPrivilegeAvailable` : `bool`  
  Set if Heartbeat/Access Privilege is available.
  - default access: read only
  - default value: `False`

`AcquisitionFrameCount` : `int`  
  Number of frames to acquire in multi-frame acquisition mode.
  - default access: not available
  - default range: 1 - 65535

`AcquisitionFrameRate` : `float`  
  Controls the acquisition rate (in Hertz) at which the frames are captured.
  - default access: read only
  - default value: `55.51639938354492`
  - unit: Hz
  - default range: 1.0 - 55.5590705871582

`AcquisitionFrameRateAuto` : `enum`  
  Controls the mode for automatic frame rate adjustment.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values: `'Off'`, `'Once'`, `'Continuous'`

`AcquisitionFrameRateEnabled` : `bool`  
  Enables manual control of the camera frame rate.
  - default access: read/write
  - default value: `True`

`AcquisitionMode` : `enum`  
  Sets the acquisition mode of the device.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values: `'Continuous'`, `'SingleFrame'`, `'MultiFrame'`

`AcquisitionStatus` : `bool`  
  Reads the state of the internal acquisition signal selected using AcquisitionStatusSelector.
  - default access: read only
  - default value: `False`

`AcquisitionStatusSelector` : `enum`  
  Selects the internal acquisition signal to read using AcquisitionStatus.
  - default access: read/write
  - default value: `'FrameTriggerWait'`
  - possible values: `'FrameTriggerWait'`

`ActivePageNumber` : `int`  
  Control the number of the active data flash page.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4095

`ActivePageOffset` : `int`  
  Control the offset of the coefficient to access in the active data flash page.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 255

`ActivePageValue` : `int`  
  Returns the value at entry ActivePageOffset of the active data flash page.
  - default access: read/write
  - default value: `1363494992`
  - default range: 0 - 4294967295

`AutoExposureTimeLowerLimit` : `float`  
  Lower limit of the Auto Exposure (us) parameter
  - default access: read/write
  - default value: `11.38448715209961`
  - unit: us
  - default range: 0.0 - 17887.353897094727

`AutoExposureTimeUpperLimit` : `float`  
  Upper limit of the Auto Exposure (us) parameter
  - default access: read/write
  - default value: `17887.353897094727`
  - unit: us
  - default range: 11.38448715209961 - 93287.70637512207

`AutoFunctionAOIHeight` : `int`  
  Height of the auto function area of interest in pixels.
  - default access: not available
  - default range: 0 - 1536

`AutoFunctionAOIOffsetX` : `int`  
  Vertical offset from the origin to the auto function area of interest in pixels.
  - default access: not available
  - default range: 0 - 2048

`AutoFunctionAOIOffsetY` : `int`  
  Horizontal offset from the origin to the auto function area of interest in pixels.
  - default access: not available
  - default range: 0 - 1536

`AutoFunctionAOIWidth` : `int`  
  Width of the auto function area of interest in pixels.
  - default access: not available
  - default range: 0 - 2048

`AutoFunctionAOIsControl` : `enum`  
  ON or OFF for the feature of the Auto Function AOIs.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`AutoGainLowerLimit` : `float`  
  Lower limit of the Auto Gain (dB) parameter
  - default access: read/write
  - default value: `0.0`
  - unit: dB
  - default range: 0.0 - 47.994266510009766

`AutoGainUpperLimit` : `float`  
  Upper limit of the Auto Gain (dB) parameter
  - default access: read/write
  - default value: `47.994266510009766`
  - unit: dB
  - default range: 0.0 - 47.994266510009766

`BalanceRatio` : `float`  
  This value sets the selected balance ratio control as an integer.
  - default access: not available
  - default range: 0.25 - 4.0

`BalanceRatioSelector` : `enum`  
  Selects a balance ratio to configure. Once a balance ratio control has been selected.
  - default access: read/write
  - default value: `'Red'`
  - possible values:
    - `'Red'`: This enumeration value selects the red balance ratio control for adjustment.
    - `'Blue'`: This enumeration value selects the blue balance ratio control for adjustment.

`BalanceWhiteAuto` : `enum`  
  Balance White Auto is the 'automatic' counterpart of the manual white balance feature.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Disables the Balance White Auto function.
    - `'Once'`: Sets operation mode to 'once'.
    - `'Continuous'`: Sets operation mode to 'continuous'.

`BinningHorizontal` : `int`  
  Number of horizontal pixels to combine together.
  - default access: read only
  - default value: `1`
  - default range: 1 - 2

`BinningHorizontalLocked` : `int`  
  
  - default access: read/write
  - default value: `1`
  - default range: -9223372036854775808 - 9223372036854775807

`BinningVertical` : `int`  
  Number of vertical pixels to combine together.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 2

`BlackLevel` : `float`  
  Analog black level in percent.
  - default access: read/write
  - default value: `5.8349609375`
  - unit: %
  - default range: 0.0 - 12.4755859375

`CamRegBaseAddress` : `int`  
  
  - default access: read/write
  - default value: `281474724003840`
  - default range: -9223372036854775808 - 9223372036854775807

`ChunkBlackLevel` : `float`  
  Returns the black level used to capture the image.
  - default access: not available
  - default range: -3.4028234663852886e+38 - 3.4028234663852886e+38

`ChunkCRC` : `int`  
  Returns the CRC of the image payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkEnable` : `bool`  
  Enables the inclusion of the selected Chunk data in the payload of the image.
  - default access: read/write
  - default value: `False`

`ChunkExposureTime` : `float`  
  Returns the exposure time used to capture the image.
  - default access: not available
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkFrameCounter` : `int`  
  Returns the image count.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkGain` : `float`  
  Returns the gain used to capture the image.
  - default access: not available
  - default range: -3.4028234663852886e+38 - 3.4028234663852886e+38

`ChunkHeight` : `int`  
  Returns the height of the image.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkModeActive` : `bool`  
  Activates the inclusion of Chunk data in the payload of the image
  - default access: read/write
  - default value: `False`

`ChunkOffsetX` : `int`  
  Returns the Offset X of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkOffsetY` : `int`  
  Returns the Offset Y of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkPixelDynamicRangeMax` : `int`  
  Returns the Maximum range of the pixel
  - default access: not available
  - default range: 0 - 4294967295

`ChunkPixelDynamicRangeMin` : `int`  
  Returns the Minimum range of the pixel
  - default access: not available
  - default range: 0 - 4294967295

`ChunkPixelFormat` : `enum`  
  This enumeration lists the pixel formats that can be indicated by the pixel format chunk.
  - default access: not available
  - possible values:
    - `'Mono8'`: This enumeration value indicates that the pixel data in the acquired image is in the Mono 8 format.
    - `'Mono10'`: This enumeration value indicates that the pixel data in the acquired image is in the Mono 10 format.
    - `'Mono12'`: This enumeration value indicates that the pixel data in the acquired image is in the Mono 12 format.
    - `'Mono12Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the Mono 12 Packed format.
    - `'BayerGR8'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GR 8 format.
    - `'BayerRG8'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer RG 8 format.
    - `'BayerGB8'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GB 8 format.
    - `'BayerBG8'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer BG 8 format.
    - `'BayerGR12'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GR 12 format.
    - `'BayerRG12'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer RG 12 format.
    - `'BayerGB12'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GB 12 format.
    - `'BayerBG12'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GB 12 format.
    - `'YUV422Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the YUV 422 Packed format.
    - `'Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the YUV 422 (YUYV) Packed format.
    - `'BayerGB12Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GB 12 Packed  format.
    - `'BayerGR12Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer GR 12 Packed format.
    - `'BayerRG12Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer RG 12 Packed format.
    - `'BayerBG12Packed'`: This enumeration value indicates that the pixel data in the acquired image is in the Bayer BG 12 Packed format.

`ChunkSelector` : `enum`  
  Selects which chunk data to enable or control
  - default access: read/write
  - default value: `'FrameCounter'`
  - possible values: `'Image'`, `'CRC'`, `'FrameCounter'`, `'OffsetX'`, `'OffsetY'`, `'Width'`, `'Height'`, `'ExposureTime'`, `'Gain'`, `'BlackLevel'`, `'PixelFormat'`, `'DynamicPixelRangeMin'`, `'DynamicPixelRangeMax'`, `'TransmitFrameCount'`, `'Timestamp'`

`ChunkTimestamp` : `int`  
  Returns the Timestamp of the image.
  - default access: not available
  - default range: 0 - 9223372036854775807

`ChunkWidth` : `int`  
  Returns the width of the image.
  - default access: not available
  - default range: 0 - 4294967295

`DataFlashBaseAddress` : `int`  
  
  - default access: read only
  - default value: `4043309056`
  - default range: -9223372036854775808 - 9223372036854775807

`DataFlashPageCount` : `int`  
  Number of the data flash pages.
  - default access: read only
  - default value: `4096`
  - default range: -9223372036854775808 - 9223372036854775807

`DataFlashPageSize` : `int`  
  Size of the data flash page.
  - default access: read only
  - default value: `256`
  - default range: -9223372036854775808 - 9223372036854775807

`DecimationHorizontal` : `int`  
  Horizontal sub-sampling of the image. This reduces the horizontal resolution (width) of the image by the specified horizontal decimation factor. A value of 1 indicates that the camera performs no horizontal decimation.
  - default access: read only
  - default value: `1`
  - default range: 1 - 2

`DecimationHorizontalLocked` : `int`  
  
  - default access: read/write
  - default value: `1`
  - default range: -9223372036854775808 - 9223372036854775807

`DecimationVertical` : `int`  
  Vertical sub-sampling of the image. This reduces the vertical resolution (height) of the image by the specified vertical decimation factor. A value of 1 indicates that the camera performs no vertical decimation.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 2

`DeviceFamilyName` : `string`  
  Family name of the device.
  - default access: read only
  - default value: `'GEN2-USB'`

`DeviceFirmwareVersion` : `string`  
  Version of the firmware in the device.
  - default access: read only
  - default value: `'1.10.3.00'`

`DeviceGenCPVersionMinor` : `int`  
  Minor version of the GenCP protocol supported by the device.
  - default access: read only
  - default value: `0`
  - default range: 0 - 65535

`DeviceGenCpVersionMajor` : `int`  
  Major version of the GenCP protocol supported by the device.
  - default access: read only
  - default value: `1`
  - default range: 0 - 65535

`DeviceID` : `string`  
  Device identifier (serial number).
  - default access: read only
  - default value: `'16306035'`

`DeviceLinkThroughputLimit` : `int`  
  Limits the maximum bandwidth of data that will be streamed out by the device.
  - default access: read/write
  - default value: `177408000`
  - default range: 3168000 - 177408000

`DeviceMaxThroughput` : `int`  
  Maximum bandwidth of the data  that can be streamed out of the device.
  - default access: read only
  - default value: `177408000`
  - default range: 3168000 - 177408000

`DeviceModelName` : `string`  
  Model name of the device.
  - default access: read only
  - default value: `'Chameleon3 CM3-U3-31S4C'`

`DeviceSVNVersion` : `string`  
  SVN Version of the device.
  - default access: read only
  - default value: `'FW:257755 FPGA:257685'`

`DeviceScanType` : `enum`  
  Scan type of the sensor.
  - default access: read only
  - default value: `'Areascan'`
  - possible values: `'Areascan'`

`DeviceSerialNumber` : `string`  
  Device serial number. This string is a unique identifier of the device.
  - default access: read only
  - default value: `'16306035'`

`DeviceTemperature` : `float`  
  Device temperature in degrees Celcius (C).
  - default access: read only
  - default value: `25.650000000000034`
  - unit: °C
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`DeviceUserID` : `string`  
  User Defined Name.
  - default access: read/write
  - default value: `''`

`DeviceVendorName` : `string`  
  Name of the manufacturer of the device.
  - default access: read only
  - default value: `'Point Grey Research'`

`DeviceVersion` : `string`  
  Version of the device.
  - default access: read only
  - default value: `'FW:v1.10.3.00 FPGA:v2.02'`

`EndianessRegistersSupported` : `bool`  
  Set if the device supports the Protocol Endianess and Implementation Endianess registers.
  - default access: read only
  - default value: `True`

`EventAcquisitionEnd` : `int`  
  Returns the unique identifier of the AcquisitionEnd type of Event.
  - default access: not available
  - default range: 0 - 65535

`EventAcquisitionEndFrameID` : `int`  
  Returns the unique Identifier of the Frame (or image) that generated the AcquisitionEnd Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventAcquisitionEndTimestamp` : `int`  
  Returns the Timestamp of the AcquisitionEnd Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventAcquisitionStart` : `int`  
  Returns the unique identifier of the AcquisitionStart type of Event.
  - default access: not available
  - default range: 0 - 65535

`EventAcquisitionStartFrameID` : `int`  
  Returns the unique Identifier of the Frame (or image) that generated the AcquisitionStart Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventAcquisitionStartTimestamp` : `int`  
  Returns the Timestamp of the AcquisitionStart Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureEnd` : `int`  
  Returns the unique identifier of the ExposureEnd type of Event.
  - default access: not available
  - default range: 0 - 65535

`EventExposureEndFrameID` : `int`  
  Returns the unique Identifier of the Frame (or image) that generated the ExposureEnd Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureEndTimestamp` : `int`  
  Returns the Timestamp of the ExposureEnd Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureStart` : `int`  
  Returns the unique identifier of the ExposureStart type of Event.
  - default access: not available
  - default range: 0 - 65535

`EventExposureStartFrameID` : `int`  
  Returns the unique Identifier of the Frame (or image) that generated the ExposureStart Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureStartTimestamp` : `int`  
  Returns the Timestamp of the ExposureStart Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventNotification` : `enum`  
  Enables/Disables event.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'On'`, `'Off'`

`EventSelector` : `enum`  
  Selects which Event to enable or control
  - default access: read/write
  - default value: `'ExposureEnd'`
  - possible values: `'AcquisitionStart'`, `'AcquisitionEnd'`, `'ExposureEnd'`

`EventTest` : `int`  
  Returns the unique identifier of the ExposureEnd type of Event.
  - default access: not available
  - default range: 0 - 65535

`EventTestFrameID` : `int`  
  Returns the unique Identifier of the Frame (or image) that generated the Test Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventTestTimestamp` : `int`  
  Returns the Timestamp of the ExposureEnd Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`ExposureAuto` : `enum`  
  Sets the automatic exposure mode when Exposure Mode is Timed.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Exposure set to manual control.
    - `'Once'`: Exposure is automatically adjusted once, then returns to Off.
    - `'Continuous'`: Exposure is automatically adjusted by the camera

`ExposureMode` : `enum`  
  Sets the operation mode of the Exposure (or shutter).
  - default access: read/write
  - default value: `'Timed'`
  - possible values: `'Timed'`, `'TriggerWidth'`

`ExposureTime` : `float`  
  Exposure time in microseconds when Exposure Mode is Timed and ExposureAuto is Off.
  - default access: read only
  - default value: `13124.942779541016`
  - unit: us
  - default range: 11.38448715209961 - 17887.353897094727

`ExposureTimeAbs` : `float`  
  Exposure time in microseconds when Exposure Mode is Timed and ExposureAuto is Off.
  - default access: read only
  - default value: `13124.942779541016`
  - unit: us
  - default range: 11.38448715209961 - 17887.353897094727

`FamilyRegisterAvailable` : `bool`  
  Set if the device supports the Family Name register.
  - default access: read only
  - default value: `True`

`Fmt7RegBaseAddress` : `int`  
  
  - default access: read only
  - default value: `281474724006400`
  - default range: -9223372036854775808 - 9223372036854775807

`GPIOCtrlPinRegBaseAddress` : `int`  
  
  - default access: read only
  - default value: `281474724008208`
  - default range: -9223372036854775808 - 9223372036854775807

`Gain` : `float`  
  Gain applied to the image in dB.
  - default access: read only
  - default value: `0.0`
  - unit: dB
  - default range: 0.0 - 47.994266510009766

`GainAuto` : `enum`  
  Sets the automatic gain control (AGC) mode.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Gain is User controlled using Gain.
    - `'Once'`: Gain is automatically adjusted once by the device. Once it has converged, it automatically returns to the Off state.
    - `'Continuous'`: Gain is constantly adjusted by the device.

`GainSelector` : `enum`  
  Selects which Gain is controlled by the various Gain features.
  - default access: read only
  - default value: `'All'`
  - possible values:
    - `'All'`: Gain will be applied to all channels or taps.

`Gamma` : `float`  
  Controls the gamma correction of pixel intensity.
  - default access: read only
  - default value: `1.0`
  - default range: 0.5 - 3.9990234375

`GammaEnabled` : `bool`  
  Enables/disables gamma correction.
  - default access: not available

`Height` : `int`  
  Height of the image provided by the device (in pixels).
  - default access: read/write
  - default value: `1536`
  - default range: 2 - 1536

`HeightMax` : `int`  
  Maximum height of the image (in pixels).
  - default access: read only
  - default value: `1536`
  - default range: 0 - 65535

`Hue` : `float`  
  Hue of the image in degrees.
  - default access: read only
  - default value: `0.0`
  - unit: °
  - default range: -180.0 - 179.912109375

`HueEnabled` : `bool`  
  Enables/disables hue adjustment.
  - default access: not available

`LUTEnable` : `bool`  
  Activates the selected LUT.
  - default access: read/write
  - default value: `False`

`LUTIndex` : `int`  
  Control the index (offset) of the coefficient to access in the selected LUT.
  - default access: not available
  - default range: 0 - 511

`LUTRegBankBaseAddress` : `int`  
  
  - default access: read only
  - default value: `4042785792`
  - default range: -9223372036854775808 - 9223372036854775807

`LUTRegBaseAddress` : `int`  
  
  - default access: read only
  - default value: `4042784768`
  - default range: -9223372036854775808 - 9223372036854775807

`LUTRegChannelBaseAddress` : `int`  
  
  - default access: read only
  - default value: `4042785792`
  - default range: -9223372036854775808 - 9223372036854775807

`LUTSelector` : `enum`  
  This enumeration the lookup table (LUT) to configure. Once a LUT has been selected, all changes to the LUT settings will be applied to the selected LUT.
  - default access: read/write
  - default value: `'Luminance'`
  - possible values:
    - `'Luminance'`: Selects the Luminace LUT.
    - `'Red'`: Selects the Red LUT.
    - `'Green'`: Selects the Green LUT.
    - `'Blue'`: Selects the Blue LUT.

`LUTValue` : `int`  
  Returns the Value at entry LUTIndex of the LUT selected by LUTSelector.
  - default access: not available
  - default range: 0 - 511

`LineDebouncerTimeRaw` : `int`  
  Sets the raw value of the selected line debouncer time in microseconds.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 1048575

`LineInverter` : `bool`  
  Controls the inversion of the signal of the selected input or output line.
  - default access: not available

`LineMode` : `enum`  
  Controls whether the physical Line is used to Input or Output a signal.
  - default access: read/write
  - default value: `'Input'`
  - possible values: `'Input'`, `'Output'`

`LineSelector` : `enum`  
  Selects the physical line (or pin) of the external device connector to configure.
  - default access: read/write
  - default value: `'Line0'`
  - possible values: `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`

`LineSource` : `enum`  
  Selects which internal acquisition or I/O source signal to output on the selected line.
  - default access: not available
  - possible values: `'ExposureActive'`, `'ExternalTriggerActive'`, `'UserOutput1'`, `'UserOutput2'`, `'UserOutput3'`

`LineStatus` : `bool`  
  Returns the current status of the selected input or output Line.
  - default access: read only
  - default value: `False`

`LineStatusAll` : `int`  
  Returns the current status of all available Line signals at time of polling in a single bitfield.
  - default access: read only
  - default value: `14`
  - default range: 0 - 15

`MessageChannelSupported` : `bool`  
  Set if the device supports a Message Channel.
  - default access: read only
  - default value: `True`

`OffsetX` : `int`  
  Vertical offset from the origin to the AOI (in pixels).
  - default access: read/write
  - default value: `0`
  - default range: 0 - 0

`OffsetY` : `int`  
  Horizontal offset from the origin to the AOI (in pixels).
  - default access: read/write
  - default value: `0`
  - default range: 0 - 0

`ParameterSelector` : `enum`  
  Selects which parameter whose limit will be removed.
  - default access: read/write
  - default value: `'Gain'`
  - possible values: `'Gain'`

`PayloadSize` : `int`  
  Number of bytes transferred for each image or chunk on the stream channel.
  - default access: read only
  - default value: `3145728`
  - default range: 0 - 4294967295

`PixelCoding` : `enum`  
  Coding of the pixels in the image.
  - default access: read only
  - default value: `'Raw'`
  - possible values: `'Mono'`, `'MonoSigned'`, `'RGBPacked'`, `'YUV411Packed'`, `'YUV422Packed'`, `'YUV444Packed'`, `'Raw'`

`PixelColorFilter` : `enum`  
  Type of color filter that is applied to the image.
  - default access: read only
  - default value: `'BayerRG'`
  - possible values: `'BayerRG'`, `'BayerGB'`, `'BayerGR'`, `'BayerBG'`, `'None'`

`PixelDefectCoordinateRegAddress` : `int`  
  
  - default access: read only
  - default value: `281474724007424`
  - default range: -9223372036854775808 - 9223372036854775807

`PixelDynamicRangeMax` : `int`  
  Indicates the maximum pixel value transferred from the camera.
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`PixelDynamicRangeMin` : `int`  
  Indicates the minimum pixel value transferred from the camera.
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`PixelFormat` : `enum`  
  Format of the pixel data.
  - default access: read/write
  - default value: `'BayerRG8'`
  - possible values:
    - `'Mono8'`: Pixel format set to Mono 8.
    - `'Mono12Packed'`: Pixel format set Mono 12 IIDC-msb Packed.
    - `'Mono12p'`: Pixel format set to 12-bit monochrome pixel lsb packed.
    - `'Mono16'`: Pixel format set to Mono 16.
    - `'BayerGR8'`: Pixel format set to Bayer GR 8.
    - `'BayerRG8'`: Pixel format set to Bayer RG 8.
    - `'BayerGB8'`: Pixel format set to Bayer GB 8.
    - `'BayerBG8'`: Pixel format set to Bayer BG 8.
    - `'BayerGR12p'`: Pixel format set to 12-bit bayer GR lsb packed.
    - `'BayerRG12p'`: Pixel format set to 12-bit bayer RG lsb packed.
    - `'BayerGB12p'`: Pixel format set to 12-bit bayer GB lsb packed.
    - `'BayerBG12p'`: Pixel format set to 12-bit bayer BG lsb packed.
    - `'BayerGR12Packed'`: Pixel format set BayerGR 12 IIDC-msb Packed.
    - `'BayerRG12Packed'`: Pixel format set BayerRG 12 IIDC-msb Packed.
    - `'BayerGB12Packed'`: Pixel format set BayerGB 12 IIDC-msb Packed.
    - `'BayerBG12Packed'`: Pixel format set BayerBG 12 IIDC-msb Packed.
    - `'BayerGR16'`: Pixel format set BayerGR 16.
    - `'BayerRG16'`: Pixel format set BayerRG 16.
    - `'BayerGB16'`: Pixel format set BayerGB 16.
    - `'BayerBG16'`: Pixel format set BayerBG 16.
    - `'CbYYCrYY'`: Pixel format set to 8-bit YCbCr 4:1:1 (CbYYCrYY).
    - `'CbYCrY'`: Pixel format set to 8-bit Y'CbCr 4:2:2 (CbYCrY).
    - `'CbYCr'`: Pixel format set to 8-bit YCbCr 4:4:4 (CbYCr).
    - `'RGB8'`: Pixel format set RGB 8.

`PixelSize` : `enum`  
  Size of a pixel in bits.
  - default access: read only
  - default value: `'Bpp8'`
  - possible values: `'Bpp8'`, `'Bpp10'`, `'Bpp12'`, `'Bpp16'`, `'Bpp24'`, `'Bpp32'`

`RemoveLimits` : `bool`  
  Specifies whether or not the parameter limit is removed.
  - default access: read/write
  - default value: `False`

`ReverseX` : `bool`  
  Flip horizontally the image sent by the device. The AOI is applied after the flip.
  - default access: read/write
  - default value: `False`

`SBRMOffset` : `int`  
  
  - default access: read/write
  - default value: `2097152`
  - default range: -9223372036854775808 - 9223372036854775807

`SBRMSupported` : `bool`  
  Set if the device supports a SBRM.
  - default access: read only
  - default value: `True`

`Saturation` : `float`  
  Saturation of the image in percent.
  - default access: read only
  - default value: `100.0`
  - unit: %
  - default range: 0.0 - 399.90234375

`SaturationAuto` : `enum`  
  Controls the mode for automatic saturation adjustment.
  - default access: not available
  - possible values: `'Off'`, `'Once'`, `'Continuous'`

`SaturationEnabled` : `bool`  
  Enables/disables saturation adjustment.
  - default access: not available

`SensorHeight` : `int`  
  Effective height of the sensor in pixels.
  - default access: read only
  - default value: `1536`
  - default range: 0 - 65535

`SensorWidth` : `int`  
  Effective width of the sensor in pixels.
  - default access: read only
  - default value: `2048`
  - default range: 0 - 65535

`Sharpness` : `int`  
  Sharpness of the image.
  - default access: read only
  - default value: `1024`
  - default range: 0 - 4095

`SharpnessAuto` : `enum`  
  Controls the mode for automatic sharpness adjustment.
  - default access: not available
  - possible values: `'Off'`, `'Once'`, `'Continuous'`

`SharpnessEnabled` : `bool`  
  Enables/disables sharpness adjustment.
  - default access: not available

`SingleFrameAcquisitionMode` : `enum`  
  Selects type of single acquisition mode
  - default access: read/write
  - default value: `'FreeRunning'`
  - possible values: `'FreeRunning'`, `'Triggered'`

`StringEncoding` : `int`  
  String Encoding of the BRM.
  - default access: read only
  - default value: `0`
  - default range: 0 - 15

`StrobeDelay` : `float`  
  Sets the duration (in microseconds) of the delay before starting the Strobe Signal.
  - default access: not available
  - unit: us
  - default range: 0.0 - 65535.0

`StrobeDuration` : `float`  
  Sets the duration (in microseconds) of the Strobe Signal.
  - default access: not available
  - unit: us
  - default range: 0.0 - 65535.0

`StrobeLineCnt16Address` : `int`  
  
  - default access: read only
  - default value: `4042266368`
  - default range: -9223372036854775808 - 9223372036854775807

`StrobeLineCntCtrlAddress` : `int`  
  
  - default access: read only
  - default value: `4042266112`
  - default range: -9223372036854775808 - 9223372036854775807

`StrobeRegBaseAddress` : `int`  
  
  - default access: read only
  - default value: `4042265344`
  - default range: -9223372036854775808 - 9223372036854775807

`TLParamsLocked` : `int`  
  
  - default access: read/write
  - default value: `0`
  - default range: 0 - 1

`TestImageSelector` : `enum`  
  Selects the type of test image that is sent by the camera.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'TestImage1'`, `'TestImage2'`

`TestPattern` : `enum`  
  Selects the type of test pattern that is generated by the device as image source.
  - default access: read/write
  - default value: `'Off'`
  - possible values:
    - `'Off'`: Image is coming from the sensor.
    - `'TestImage1'`
    - `'TestImage2'`

`TestPendingAck` : `int`  
  Test PENDING_ACK feature.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 500

`Timestamp` : `int`  
  Reports the current value of the device timestamp counter (ns).
  - default access: read only
  - default value: `0`
  - default range: 0 - 9223372036854775807

`TimestampIncrement` : `int`  
  Indicates the timestamp increment in ns/tick.
  - default access: read only
  - default value: `125000`
  - default range: 0 - 9223372036854775807

`TimestampSupported` : `bool`  
  Set if the device supports a timestamp register.
  - default access: read only
  - default value: `True`

`TransmitFailureCount` : `int`  
  Number of failed frame transmissions that have occurred since the last reset.
  - default access: read only
  - default value: `0`
  - default range: 0 - 2147483647

`TriggerActivation` : `enum`  
  Specifies the activation mode of the trigger.
  - default access: read/write
  - default value: `'FallingEdge'`
  - possible values: `'RisingEdge'`, `'FallingEdge'`

`TriggerDelay` : `float`  
  Specifies the delay (in microseconds) to apply after the trigger reception before activating it.
  - default access: read/write
  - default value: `0.0`
  - unit: us
  - default range: 0.0 - 18012.642860412598

`TriggerDelayEnabled` : `bool`  
  Specifies whether or not the Trigger Delay is enabled.
  - default access: read/write
  - default value: `False`

`TriggerMode` : `enum`  
  Controls whether or not the selected trigger is active.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`TriggerOverlap` : `enum`  
  Specifies the type trigger overlap permitted with the previous frame.
  - default access: not available
  - possible values:
    - `'Off'`: No trigger overlap is permitted.
    - `'ReadOut'`: Trigger is accepted immediately after the exposure period.

`TriggerSelector` : `enum`  
  Selects the type of trigger to configure.
  - default access: read/write
  - default value: `'FrameStart'`
  - possible values: `'FrameStart'`, `'ExposureActive'`

`TriggerSource` : `enum`  
  Specifies the internal signal or physical input line to use as the trigger source. The selected trigger must have its TriggerMode set to On.
  - default access: read/write
  - default value: `'Line0'`
  - possible values: `'Software'`, `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`

`U3VAccessPrivilege` : `int`  
  Access Privilege.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VCPCapability` : `int`  
  Indicates additional features on the control channel.
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`U3VCPCapabilityHigh` : `int`  
  Indicates additional features on the control channel.
  - default access: read only
  - default value: `0`
  - default range: 0 - 536870911

`U3VCPCapabilityLow` : `int`  
  Indicates additional features on the control channel.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`U3VCPConfigurationHigh` : `int`  
  Configure additional features on the control channel.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VCPConfigurationLow` : `int`  
  Configures additional features on the control channel.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VCPEIRMAvailable` : `bool`  
  Set if the device supports at least one device event interface.
  - default access: read only
  - default value: `True`

`U3VCPIIDC2Available` : `bool`  
  Set if the device supports IIDC2 register map.
  - default access: read only
  - default value: `False`

`U3VCPSIRMAvailable` : `bool`  
  Set if the device supports at least one device streaming interface.
  - default access: read only
  - default value: `True`

`U3VCurrentSpeed` : `enum`  
  Specifies the current speed of the USB link.
  - default access: read only
  - default value: `'SuperSpeed'`
  - possible values: `'LowSpeed'`, `'FullSpeed'`, `'HighSpeed'`, `'SuperSpeed'`

`U3VDeviceConfigurationHigh` : `int`  
  Describes Device Configuration.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VDeviceConfigurationLow` : `int`  
  Describes Device Configuration.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VMaxAcknowledgeTransferLength` : `int`  
  Specifies the max suuported ack transfer length of the device.
  - default access: read only
  - default value: `1024`
  - default range: 0 - 4294967295

`U3VMaxCommandTransferLength` : `int`  
  Specifies the max suuported command transfer length of the device.
  - default access: read only
  - default value: `1024`
  - default range: 0 - 4294967295

`U3VMaxDeviceResponseTime` : `int`  
  Max Resonse Time in ms.
  - default access: read only
  - default value: `480`
  - default range: 0 - 4294967295

`U3VMessageChannelID` : `int`  
  Channel ID Used For The Message Channel.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VNumberOfStreamChannels` : `int`  
  Number of Stream Channels and its Corresponding Streaming Interface Register Maps.
  - default access: read only
  - default value: `1`
  - default range: 0 - 4294967295

`U3VVersionMajor` : `int`  
  U3V Version.
  - default access: read only
  - default value: `1`
  - default range: 0 - 65535

`U3VVersionMinor` : `int`  
  U3V Version.
  - default access: read only
  - default value: `0`
  - default range: 0 - 65535

`USB3LinkRecoveryCount` : `int`  
  USB3 Link Recovery Count.
  - default access: read only
  - default value: `0`
  - default range: 0 - 32767

`UserDefinedValue` : `int`  
  User defined value.
  - default access: read/write
  - default value: `0`
  - default range: -2147483648 - 2147483647

`UserDefinedValueSelector` : `enum`  
  Used to select from a set of user defined values
  - default access: read/write
  - default value: `'Value1'`
  - possible values:
    - `'Value1'`: User defined value1.
    - `'Value2'`: User defined value2.
    - `'Value3'`: User defined value3.
    - `'Value4'`: User defined value4.
    - `'Value5'`: User defined value5.

`UserNameAvailable` : `bool`  
  Set if User Defined Name available.
  - default access: read only
  - default value: `True`

`UserOutputPinRegBaseAddress` : `int`  
  
  - default access: read only
  - default value: `281474724008224`
  - default range: -9223372036854775808 - 9223372036854775807

`UserOutputSelector` : `enum`  
  Selects the physical line (or pin) of the external device connector to configure.
  - default access: read/write
  - default value: `'UserOutputValue1'`
  - possible values: `'UserOutputValue1'`, `'UserOutputValue2'`, `'UserOutputValue3'`

`UserOutputValue` : `bool`  
  Sets the value of the bit to be output to the selected line.
  - default access: not available

`UserSetCurrent` : `int`  
  Indicates the user set that is currently in use.  At initialization time, the camera loads the most recently saved user set.
  - default access: read only
  - default value: `0`
  - default range: 0 - 15

`UserSetDefault` : `enum`  
  Selects the feature User Set to load and make active by default when the device is reset.
  - default access: read/write
  - default value: `'Default'`
  - possible values:
    - `'Default'`: Select the factory setting user set.
    - `'UserSet1'`: Select the user set 1.
    - `'UserSet2'`: Select the user set 2.

`UserSetDefaultSelector` : `enum`  
  Selects the feature User Set to load, save or configure.
  - default access: read/write
  - default value: `'Default'`
  - possible values:
    - `'Default'`: Factory default settings.
    - `'UserSet1'`
    - `'UserSet2'`

`UserSetSelector` : `enum`  
  Selects the feature User Set to load, save or configure.
  - default access: read/write
  - default value: `'Default'`
  - possible values:
    - `'Default'`: Factory default settings.
    - `'UserSet1'`: Selects the user set 1.
    - `'UserSet2'`: Selects the user set 2.

`VideoMode` : `enum`  
  Current video mode.
  - default access: read/write
  - default value: `'Mode0'`
  - possible values: `'Mode0'`, `'Mode1'`, `'Mode2'`, `'Mode3'`, `'Mode4'`, `'Mode5'`, `'Mode6'`, `'Mode7'`, `'Mode8'`, `'Mode9'`, `'Mode10'`, `'Mode11'`, `'Mode12'`, `'Mode13'`, `'Mode14'`, `'Mode15'`

`Width` : `int`  
  Width of the image provided by the device (in pixels).
  - default access: read/write
  - default value: `2048`
  - default range: 8 - 2048

`WidthMax` : `int`  
  Maximum width of the image (in pixels).
  - default access: read only
  - default value: `2048`
  - default range: 0 - 65535

`WrittenLengthFieldSupported` : `bool`  
  Set to 1 if the device sends the length_written field in the SCD section of the WriteMemAck command.
  - default access: read only
  - default value: `True`

`pgrAutoExposureCompensationLowerLimit` : `float`  
  Lower limit of the auto exposure compensation value(EV) parameter
  - default access: read/write
  - default value: `0.4150390625`
  - unit: EV
  - default range: -70.0849609375 - 2.0

`pgrAutoExposureCompensationUpperLimit` : `float`  
  Upper limit of the auto exposure compensation value(EV) parameter
  - default access: read/write
  - default value: `2.0`
  - unit: EV
  - default range: 0.4150390625 - 4.41473388671875

`pgrCurrentCorrectedPixelCount` : `int`  
  Current number of pixels that are being corrected.
  - default access: read/write
  - default value: `2`
  - default range: 0 - 127

`pgrCurrentCorrectedPixelIndex` : `int`  
  Control the index of the defected pixels to be corrected.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 1

`pgrCurrentCorrectedPixelOffsetX` : `int`  
  Control the X offset of the defect pixel specified by the index.
  - default access: read/write
  - default value: `1604`
  - default range: 0 - 2047

`pgrCurrentCorrectedPixelOffsetY` : `int`  
  Control the Y offset of the defect pixel specified by the index.
  - default access: read/write
  - default value: `268`
  - default range: 0 - 1535

`pgrDefectPixelCorrectionEnable` : `bool`  
  Enable or disable pixel correction.
  - default access: read/write
  - default value: `True`

`pgrDefectPixelCorrectionTestMode` : `enum`  
  Controls whether or not the defect pixel correction test mode is active.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`pgrDefectPixelCorrectionType` : `enum`  
  Specifies the current defect pixel correction type.
  - default access: read only
  - default value: `'FPGACorrection'`
  - possible values: `'FPGACorrection'`, `'SensorCorrection'`

`pgrDeviceUptime` : `int`  
  Time since the device was powered up.
  - default access: read only
  - default value: `5`
  - default range: 0 - 4294967295

`pgrExposureCompensation` : `float`  
  The measured or target image plane illuminance in EV.
  - default access: read only
  - default value: `1.4150390625`
  - unit: EV
  - default range: -7.5849609375 - 2.41363525390625

`pgrExposureCompensationAuto` : `enum`  
  Sets the automatic exposure compensation value mode.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values: `'Off'`, `'Once'`, `'Continuous'`

`pgrHDRImageSelector` : `enum`  
  Selects the HDR image.
  - default access: not available
  - possible values:
    - `'Image1'`: HDR image 1.
    - `'Image2'`: HDR image 2.
    - `'Image3'`: HDR image 3.
    - `'Image4'`: HDR image 4.

`pgrHDRModeEnabled` : `bool`  
  Specifies whether or not the High Dynamic Range mode is enabled.
  - default access: read/write
  - default value: `False`

`pgrSensorDescription` : `string`  
  Description of the sensor of the device.
  - default access: read only
  - default value: `'Sony IMX265 (1/1.8" Color CMOS)'`

Commands
--------

**Note: the camera recording should be started/stopped using the `start` and `stop` methods, not any of the functions below (see easy_pyspin documentation).**

`AcquisitionStart()`:  
  Starts the Acquisition of the device.
  - default access: write only

`AcquisitionStop()`:  
  Stops the acquisition of the device at the end of the current frame.
  - default access: write only

`ActivePageSave()`:  
  Save the data in the active page to the data flash.
  - default access: write only

`DeviceReset()`:  
  This is a command that immediately resets and reboots the device.
  - default access: write only

`TimestampLatch()`:  
  Latches the curretn device time into the timstamp register.
  - default access: write only

`TransmitFailureCountReset()`:  
  Reset the transmit failure count.
  - default access: write only

`TriggerEventTest()`:  
  This command sends a test event.
  - default access: write only

`TriggerSoftware()`:  
  Generates an internal trigger if Trigger Source is set to Software.
  - default access: not available

`UserSetLoad()`:  
  Loads the User Set specified by UserSetSelector to the device and makes it active.
  - default access: write only

`UserSetSave()`:  
  Save the User Set specified by UserSetSelector to the non-volatile memory of the device.
  - default access: not available

`pgrCurrentCorrectedPixelSave()`:  
  Save the Current Corrected Pixels to the non-volatile memory of the device.
  - default access: write only
