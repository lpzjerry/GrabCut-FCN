# GrabCut-UNet
Improve the performance of traditional semi-automatic image segmentation algorithms (e.g. GrabCut) with [U-Net](https://arxiv.org/pdf/1505.04597.pdf).
- *This project serves as the final project for the course **[CS4186 Computer Vision and Image Processing](https://www.cityu.edu.hk/catalogue/ug/201819/course/CS4186.htm)** offered by [Prof. NGO Chong Wah](http://www.cs.cityu.edu.hk/~cwngo/).*

- Methods to compare & improve:
  - A: [GrabCut](https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html)
  - B: [Binary Segmentation](https://github.com/TejasNaikk/Binary-Segmentation)
  - C: [U-Net](https://github.com/milesial/Pytorch-UNet)

- Dataset
  - [Geodesic Star Convexity for Interactive Image Segmentation (by VGG)](http://www.robots.ox.ac.uk/~vgg/data/iseg/)
  
- Result

| Method   | Input    | IoU      |
| -------- | -------- | -------- |
| GrabCut | Image     | 0.1950   |
| GrabCut | Image + Box | 0.4096 |
| GrabCut | Image + Box + Raw Annotation | 0.4217 |
| Binary Segmentation | Image + Raw Annotation | 0.4408 |
| U-Net | Image + Box | **0.5527** |

### Important Dates
- **03/08/2019**: Proposal deadline
- **04/16/2019**: Project presentation
- **04/27/2019**: Final report submission
