from __future__ import absolute_import
import pycuda.driver as cuda

# Initialize CUDA
cuda.init()

from pycuda.tools import make_default_context
global context
context = make_default_context()
device = context.get_device()

context.pop()
context = None

