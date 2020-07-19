import ctypes
import os

lib_dir = os.path.dirname(os.path.realpath(__file__))

LIBRARIES = [
    'libutil.so.1',
    'libpcre.so.0',
    'libXau.so.6',
    'libxcb.so.1',
    'libX11.so.6',
    'libXext.so.6',
    'libXxf86vm.so.1',
    'libXfixes.so.3',
    'libXrender.so.1',
    'libfftw3.so.3',
    'libGLdispatch.so.0',
    'libGLX.so.0',
    'libGL.so.1',
    'libGLU.so.1',
    'libGLEW.so.2.2',
    'libosdCPU.so.3.4.0',
    'libosdGPU.so.3.4.0',
    'libHalf.so',
    'libIex.so',
    'libIexMath-2_4.so.24',
    'libImath.so',
    'libIlmThread.so',
    'libIlmImf-2_4.so.24',
    'libboost_filesystem.so.1.70.0',
    'libboost_regex.so.1.70.0',
    'libboost_thread.so.1.70.0',
    'libboost_date_time.so.1.70.0',
    'libboost_chrono.so.1.70.0',
    'libboost_wave.so.1.70.0',
    'libboost_system.so.1.70.0',
    'libpng12.so.0',
    'libjpeg.so.62',
    'libopenjpeg.so.2',
    'libjbig.so.2.0',
    'libtiff.so.5',
    'libfreetype.so.6',
    'libOpenImageIO.so',
    'libxml2.so.2',
    'liboslcomp.so.1.10',
    'liboslexec.so.1.10',
    'liboslquery.so.1.10',
    'libpython3.7m.so.1.0',
]

for lib in LIBRARIES:
    print(os.path.join(lib_dir, lib))
    ctypes.cdll.LoadLibrary(os.path.join(lib_dir, lib))

from . import bpy
