from utils import *

# 测试A、M、P、RGB四个波段图像shape
imageId = '6120_2_2'
a = A(imageId)
m = M(imageId)
p = P(imageId)
rgb = RGB(imageId)
print('A-shape:', a.shape, 'dtype:', a.dtype, 'M-shape:', m.shape, 'dtype:', m.dtype, 'P-shape:',
      p.shape, 'dtype:', p.dtype, 'RGB-shape:', rgb.shape, 'dtype:', rgb.dtype)
# 测试不同波段组合显示的图像
display_img(a)
display_img(m)
display_img(p)
display_img(rgb)
# M段的图尺寸都为(837, 851, 8)
image = np.zeros((837, 851, 3))
# 从M段中取出RGB波段组合成图像
image[:, :, 0] = m[:, :, 4]  # red
image[:, :, 1] = m[:, :, 2]  # green
image[:, :, 2] = m[:, :, 1]  # blue
# 对比原图与做过对比度加强的图像，原图其实与RGB段的图是一样的
display_img(image)
# 测试线性拉伸
display_img(stretch_n(image))
