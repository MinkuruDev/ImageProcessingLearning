# **TỔNG HỢP KIẾN THỨC**

|Thư viện/Hàm                                   |Chức năng                                                                      |
|---                                            |---                                                                            |
|***`PIL`***                                    |*[Documentation](https://pillow.readthedocs.io/en/stable/reference/index.html)*|
|`Image.open(path)`                             |Mở ảnh tại `path` và trả về một đối tượng của `PIL`|
|`im.show()`                                    |Hiển thị ảnh được gán vào `im` (`im` là một đối tượng ảnh của `PIL`)|
|`im.convert(mode)`                             |Chuyển `im` thành ảnh định dạng khác theo `mode`|
|`im.save(path)`                                |Lưu ảnh vào đường dẫn `path`|
|`Image.fromarray(im)`                          |Đọc ảnh `im` là mảng `numpy.ndarray` trả về đối tượng ảnh `PIL`|
|`im.crop(left,top,right,bottom)`               |Cắt ảnh|
|`im.resize(newsize,resampling)`                |Thay đổi kích thước ảnh thành `newsize` bằng thuật toán `resampling`|
|`im.point(func)`                               |Biến đổi từng pixel của ảnh theo hàm `func`|
|`im.transpose(method)`                         |Lật hoặc xoay ảnh theo `method`|
|`im.rotate(angle)`                             |Xoay ảnh `angle` độ|
|`im.transform(*args,**kwargs)`                 |Biến đổi ảnh|
|`im.putpixel(axis,value)`                      |Đổi giá trị pixel tại vị trí `axis` thành giá trị `value`|
|`im.copy()`                                    |Copy ảnh, trả về một `Image` là ảnh sao chép của `im`|
|`ImageDraw.Draw(im)`                           |Tạo một đối tượng `ImageDraw` để vẽ lên `im`|
|`ImageFont.truetype(font,size)`                |Tạo font để vẽ lên ảnh|
|`draw.text(axis,msg,font)`                     |Vẽ `msg` lên ảnh, phông chữ `font` bắt đầu từ toạ độ `axis` (`draw` là một `ImageDraw`)|
|`im.thumbnail(size)`                           |Tạo hình thu nhỏ của `im`, gán trực tiếp vào `im`|
|`im.patse(im1,axis)`                           |Dán đè `im1` lên `im` tại vị trí `axis`|
|`im.split()`                                   |Chia ảnh `im` thành 3 kênh màu R G B|
|`Image.merge(mode,bands)`                      |Gộp các kênh màu `bands` theo `mode`|
|`Image.blend(im1,im2,alpha)`                   |Trộn ảnh `im1` và `im2`, `alpha` cho độ đậm nhạt của `im2`|
|`ImageChops.difference(im1,im2)`               |Tính toán sự khác nhau giữa `im1` và `im2` có cùng kích thước (Không nên dùng ảnh RGBA)|
|`ImageChops.multiply(im1,im2)`                 |Chồng hai ảnh `im1` và `im2` lên nhau bằng cách nhân từng pixel cùng vị trí với nhau|
|`ImageChops.add(im1,im2)`                      |Cộng hai ảnh tại từng pixel|
|---|---|
|***`mathplotlib`***                            |*[Documentation](https://matplotlib.org/3.6.2/api/image_api.html)*|
|`import mathplotlib.image as mpimg`            |Gọi các hàm của `mathplotlib.image` bằng cách sử dụng `mpimg`|
|`import matplotlib.pylab as plt`               |Gọi các hàm của `mathplotlib.pylab` bằng cách sử dụng `plt`|
|`mpimg.imread(path)`                           |Đọc ảnh tại `path` và trả về một `numpy.ndarray`|
|`plt.figure(**kwargs)`                         |Tạo figure hoặc mở figure đã có|
|`plt.subplot(*args)`                           |Tạo hoặc tuỳ chỉnh figure mới có chia ô|
|`plt.imshow(im)`                               |Đặt `im` vào figure (`im` có thể là đối tượng của `numpy.ndarray` hoặc `PIL`)|
|`plt.imsave(path,im)`                          |Lưu `im` vào đường dẫn `path`|
|`plt.axis("off")`                              |Không hiện toạ độ đặt ảnh trước đó vào figure sử dụng `plt.imshow`|
|`plt.show()`                                   |Hiển thị tất cả figure đang được mở|
|`plt.savefig(path)`                            |lưu figure hiện tại vào đường dẫn `path`|
|---|---|
|***`skimage`***                                |*[Documentation](https://scikit-image.org/docs/stable/api/api.html)*|
|`io.imread(path)`                              |Đọc ảnh tại `path` và trả về một `numpy.ndarray`|
|`io.imshow(im)`                                |Hiển thị ảnh tại `im` (`im` là một đối tượng của `numpy.ndarray` hoặc đường dẫn đến ảnh)|
|`io.imread_collection(load_pattern)`           |Đọc các ảnh của `load_pattern` trả về một `ImageCollection`|
|`io.imshow_collection(ic)`                     |Hiển thị các ảnh trong `ic` (`ic` là `ImageCollection` trả về bởi `imread_collection`)|
|`color.rgb2hsv(im)`                            |Chuyển ảnh `im` là ảnh rgb thành hsv (rgb và hsv đều lưu dạng mảng `numpy.ndarray`)|
|`color.hsv2rgb(im)`                            |Chuyển ảnh `im` là ảnh hsv thành rgb|
|`color.rgb2gray(im)`                           |Chuyển ảnh `im` là ảnh rgb thành ảnh grayscale|
|`data.astronaut()`                             |Đọc dữ liệu astronaut có sẵn dưới dạng `numpy.ndarray`|
|`transform.SimilarityTransform(**kwargs)`      |Tính toán và trả về ma trận biến đổi để sử dụng trong hàm `wrap`|
|`transform.wrap(im,tform)`                     |Biến đổi `im` theo ma trận `tform`|
|`transform.swirl(im,**kwargs)`                 |Biến đổi xoáy `im` theo các tham số `**kwargs`|
|`util.random_noise(im,**kwargs)`               |Tạo nhiễu lên `im`|
|---|---|
|***`scipy`***                                  |*[Documentation](https://docs.scipy.org/doc/scipy-1.9.3/reference/index.html)*|
|`misc.imread(path)`                            |Đọc ảnh tại `path` và trả về một `numpy.ndarray`|
|`misc.face()`                                  |Đọc dữ liệu raccon có sẵn dưới dạng `numpy.ndarray`|
|`misc.imsave(path,im)`                        |Lưu ảnh `im` vào đường dẫn `path`|
|---|---|
|***`numpy`***                                  |*[Documentation](https://numpy.org/doc/stable/reference/index.html)*|
|`array(im)`                                    |Đọc `im` là một đối tượng ảnh `PIL`, trả về ảnh là `ndarray`|

