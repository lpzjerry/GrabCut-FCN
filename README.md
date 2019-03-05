# GrabCut-FCN
Improve the performance of traditional semi-automatic image segmentation algorithms (e.g. GrabCut) with Fully Convolutional Network (FCN).
- *This project serves as the final project for the course **[CS4186 Computer Vision and Image Processing](https://www.cityu.edu.hk/catalogue/ug/201819/course/CS4186.htm)** offered by [Prof. NGO Chong Wah](http://www.cs.cityu.edu.hk/~cwngo/).*

### TODOs
- [ ] Prepare the semi-automatic segmentation (SAS) dataset from VOC (Pengze)
- [ ] Try method A & B on the SAS dataset (Shuhan)
- [ ] Try method C on the SAS dataset (Pengze)
- [ ] Evaluate A, B & C. Compare the result of A, B & C on SAS. Ideally, **C > A && C > B**. (Shuhan)
- [ ] Test the generalization ability of C by replicating A, B and C on another dataset with different foreground objects. (Pengze)
- [ ] Set a threshold to extract C' from C. (Pengze)
- [ ] Use the result of C' as the foreground & background mask for A and B so as to improve the performance of A and B. (Shuhan)

- Methods to compare & improve:
  - A: [GrabCut](https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html)
  - B: [Binary Segmentation](https://github.com/TejasNaikk/Binary-Segmentation)
  - C: [FCN](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf)
