# def check_libraries(libs):
#     for lib in libs:
#         try:
#             __import__(lib)
#             print(f"{lib} 已安装")
#         except ModuleNotFoundError:
#             print(f"{lib} 未安装")
#
#
# libraries = ['numpy', 'matplotlib', 'pandas', 'sklearn', 'pytorch', 'opencv', 'tensorflow']
# check_libraries(libraries)
#
# import torch
#
# print(torch.__version__)

# import tensorflow as tf
# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 不显示等级2以下的提示信息
#
# print('GPU', tf.test.is_gpu_available())
#
# a = tf.constant(2.0)
# b = tf.constant(4.0)
# print(a + b)

# import tensorflow as tf
# import os
# #os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# a = tf.constant(1.)
# b = tf.constant(2.)
# print(a+b)
# print(tf.__version__)
# print('GPU:', tf.config.list_physical_devices('GPU'))
# print(tf.test.is_gpu_available())
import torch
flag = torch.cuda.is_available()
print(flag)

ngpu= 1
# Decide which device we want to run on
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
print(device)
print(torch.cuda.get_device_name(0))
print(torch.rand(3,3).cuda())
