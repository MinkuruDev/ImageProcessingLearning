# for inline image display inside notebook
# % matplotlib inline
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mpimg
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
from scipy import misc

def PILImage():
    # PIL Image
    im = Image.open("../images/Thorns Head.png")
    # im.show()

    im_g = im.convert('L') # convert the RGB color image to a grayscale image
    im_g.save('../images/thorns_gray.png') # save the image to disk
    Image.open("../images/thorns_gray.png").show() 

def mpl():
    im = mpimg.imread("../images/Headhunt10.png") 
    print(im.shape, im.dtype, type(im)) 
    # plt.figure(figsize=(10,10))
    # plt.imshow(im) # display the image

    # im1 = im
    # im1[im1 < 0.5] = 0 # make the image look darker
    # plt.imshow(im1)

    methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'lanczos']
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(50, 100), subplot_kw={'xticks': [], 'yticks': []})
    fig.subplots_adjust(hspace=0.05, wspace=0.05)
    for ax, interp_method in zip(axes.flat, methods):
        ax.imshow(im, interpolation=interp_method)
        ax.set_title(str(interp_method), size=20)

    # plt.axis('off')
    plt.tight_layout()
    plt.show()

def skImage():
    im = imread("../images/rick.png") 
    im = data.astronaut()
    # hsv = color.rgb2hsv(im) # from RGB to HSV color space
    # hsv[:, :, 1] = 0.5 # change the saturation 
    # im1 = color.hsv2rgb(hsv) # from HSV back to RGB
    # imsave('../images/rick_hsv.png', im1) # save image to disk
    # im = imread("../images/rick_hsv.png")
    plt.axis('off'), imshow(im), show()
    viewer = viewer.ImageViewer(im)
    viewer.show()

def main():
    
    # PILImage()

    # mpl()

    skImage()

if __name__ == "__main__":
    main()
