import pycuda.autoinit


# def allocate_buffers(engine):
#     inputs = []
#     outputs = []
#     bindings = []
#     stream = cuda.Stream()
#     for binding in engine:
#         size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
#         dtype = trt.nptype(engine.get_binding_dtype(binding))
#         # Allocate host and device buffers
#         host_mem = cuda.pagelocked_empty(size, dtype)
#         device_mem = cuda.mem_alloc(host_mem.nbytes)
#         # Append the device buffer to device bindings.
#         bindings.append(int(device_mem))
#         # Append to the appropriate list.
#         if engine.binding_is_input(binding):
#             inputs.append(HostDeviceMem(host_mem, device_mem))
#         else:
#             outputs.append(HostDeviceMem(host_mem, device_mem))
#     return inputs, outputs, bindings, stream

# trt_logger = trt.Logger()  # This logger is required to build an engine
# f = open("model.plan", "rb")
# runtime = trt.Runtime(trt_logger)
# net = runtime.deserialize_cuda_engine(f.read())
# # Create the context for this engine
# context = net.create_execution_context()
# 
# allocate_buffers(net)

print("cuda_test---")
