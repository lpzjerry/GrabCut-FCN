# CS4186 Computer Vision
###### tags: `course`
## 1. Filter (Chapter 3.1-3.2)
- Intensity: brightness of a pixel
- Linear Filtering
    - Cross-correlation G = H ⨂ F
        - ![](https://i.imgur.com/GKSBO9D.png)
        - F: image, H: kernel
    - **Convolution** G = H * F
        - ![](https://i.imgur.com/9gkwiFs.png)
        - the kernel is "flipped" (horizontally and vertically) 
- Kernels
    - Blur: **Mean filtering**/Moving average
    - Sharpening: 2*original - blurred
    - Smooth: **Gaussian Filter** (Remove high-freq)
        - ![](https://i.imgur.com/u6pUhGE.png)
    - detail = original - smoothed
        - sharpening = origianl + detail
    - Thresholding
## 2. Edges (Chapter 4.2)
- Image derivatives
    - ![](https://i.imgur.com/1FH3qUH.png)
- Image gradient
    - Edge Strength 
        - ![](https://i.imgur.com/WywjQyl.png)
    - Gradient Direction
        - ![](https://i.imgur.com/wuvGvzh.png)
- Remove noise
    - Smooth before calculate gradient
    - f: signal with noise
    - h: gaussian kernel (to remove noise)
    - f * h: smoothed signal
    - differetiation in x direction: d/dx (f * h) = f * d/dx(h)
- 1st Derivative of gaussian
    - ![](https://i.imgur.com/O9zu3h7.png)
    - Sobel operator
        - $s_{x}$ = [[-1,0,1],[-2,0,2],[-1,0,1]]
        - $s_{y}$ = [[1,2,1],[0,0,0],[-1,-2,-1]]
- Laplacian of Gaussian (LoG) Filter
    - Second derivative of Gaussian
    - Effects
        - Zero far away from the edge
        - Positive on one side
        - Negative on the other side
        - Zero just at the edge
#### Canny edge detector
1. Filter image with derivative of Gaussian
2. Find magnitude and orientation of gradient
3. Non-maximum suppression (NMS, for thinning)
4. Linking and thresholding (hysteresis):
    - Define two thresholds: low and high
    - Use the high threshold to start edge curves and the low threshold to continue them
- Parameters
    - $\sigma$: large scale edges (L) / fine edges (S) 
    - $t_{low}$, $t_{high}$
## 3. Image Resampling
- Downsampling
    - Gaussian pre-filtering
    - Gaussian pyramids (4/3 of the original image)
- Upsampling
    - Image interpolation
        - Nearest-neighbor interpolation: II(x)
        - Linear interpolation: $\Lambda$(x)
        - Gaussian reconstruction: gauss(x)
## 4.1. Color
#### Color space
- **RGB**
- **HSI/HSV**: hue, saturation, intensity (conical)
    - H: color, S: level of colorfulness, V: brightness
    - Hue is encoded as an angle (0 to 2$\pi$)-type of color
    - Saturation is the distance to the vertical axis (0-grey to 1-color).
    - Intensity is the height along the vertical axis (0-black to 1-white).
- **YIQ**: Y: intensity, I: orange-blue color (human sensitive), Q: purple-green color
- **CIE**: L\*a\*b, L: intensity, a: green(-)-red(+), b: blue(-)-yellow(+) (spherical)
#### Histogram Equalization
𝐽(𝑥,𝑦)=𝒇(𝐹(𝑥,𝑦))
𝒇() is the target function. 𝒇() is monotonic
- Cumulative Distribution Function (CDF)
    - 𝐶(𝑖)= $∑_{𝑗≤𝑖}$ ℎ(𝑗)/𝑁
    - g is the new histogram after equalization
    - D is the CDF of g
    - C is the CDF of the original image F
        - Compute g
        - Compute CDF
        - For each pixel: k*C(i)
#### Color Histogram
r’ = r/(r+g+b)
g’ = g/(r+b+g)
b’ = b/(r+g+b)
b’ = 1-r’-g’, which can be ignored in representation 
- Swain and Ballard’s Histogram Matching
    - 2048 bins
        - wb = R + G + B (8, intensity)
        - rg = R - G (16)
        - by = 2B - R - G (16)
    - intersection(h(I),h(M)) = $\Sigma_{j=1,2048}$ min{h(I)[j],h(M)[j]}
    - match(h(I),h(M)) = intersection(h(I),h(M)) / $\Sigma_{j=1,2048}$ h(M)[j] $\Rightarrow$ normalization
    - Uses: basis for many content-based image retrieval systems

## 4.2. Texture
#### Texture measures (Segmenting out texels)
1. Edge Density and Direction
2. **LBP**: Local Binary Pattern
    - b~1~ - b~8~: adjacent px > central ? 1 : 0
    - ![](https://i.imgur.com/P0PpXGq.png)
    - g(): thresholding
3. Co-occurrence Matrix Features
    - $C(i,j)$ indicates how many times value $i$ co-occurs with value $j$ in a particular spatial relationship $d$.
    - Normalize by sum of matrix C~d~. Get N~d~.
- ![](https://i.imgur.com/sbr3cJ5.png)
    - **Energy**: measure uniformity
    - **Entropy**: measure of randomness
    - **Contrast**: Measures the local variations. (favors contribution of N(I,j) away from the diagonal.
    - **Homogeneity**: large if big value are on the diagonal (Contrast <-> Homogeneity)
    - **Correlation**: Measures the joint probability occurrence of the specified pixel pairs or how correlated a reference pixel to its neighbors
 
## 5. Corner (Chapter 4.1)
- Motivation: panorama stitching: extract features, match features, align images.
- **Invariant local features**: invariant to (geometric, photometric) invariance.
    - Locality, Quantity, Distinctiveness, Efficiency
- Approaches
    - **Detection**: Identify the interest points
    - **Description**: Extract vector feature descriptor
    - **Matching**
    - (Tracking)
#### Harris corner detection
- Shifting the window $W$ by $(u,v)$:
    - Sum of Square Difference (SSD error). Assume the offset $(u,v)$ is small.
    - Taylor Series expansion of I: ![](https://i.imgur.com/86sJ5hu.png)
    - $\Rightarrow E(u,v) \approx \Sigma_{(x,y)\in W}[I_{x}u+I_{y}v]^{2}$
    - where $I_{x}$ is the derivative in x direction
- $E(x,y) \approx Au^{2} + 2Buv + Cv^{2}$
    - $A = \Sigma I_{x}^{2}$
    - $B = \Sigma I_{x}I_{y}$
    - $C = \Sigma I_{y}^{2}$
    - ![](https://i.imgur.com/Qlmi33u.png)
- math
    - $Hx = \lambda x, Ax = \lambda x$
    - $X_{max}$: the direction that gives you the largest change (SSD difference)
    - $\lambda_{max}$: if you move via $X_{max}$, the amount of increase.
- intuition
    - Doing matrix decomposition, we will get the 4 values.
    - To detect the corners, we need **a large ${\lambda_{min}}$ value**.
    - Edge: large $\lambda_{max}$, small $\lambda_{min}$. Flat: both small
- Algorithm
    1. Compute the gradient at each point in the image
    2. Create the H matrix from the entries in the gradient
    3. Compute the eigenvalues. 
    4. Find points with large response ($\lambda_{min}$ > threshold)
    5. Choose those points where $\lambda_{min}$ is a local maximum as features (NMS)
- or a more simple version
    1. Edge detection
    2. Harris matrix decomposition (slow)
    3. Calc $\lambda$, select local maximum $\lambda_{min
- To simplify matrix decomposition:
    - Harris Corner Detector / Harris operator
    - $f = \frac{\lambda_{1}\lambda_{2}}{\lambda_{1}+\lambda_{2}} = \frac{determinant(H)}{trace(H)} \approx \lambda_{min}$ 
    - $trace(H) = h_{11} + h_{22}$
- In practice, also:
    - Weighting derivatives by its distance from the central pixel
    - ![](https://i.imgur.com/K7lnGL9.png)
- Finally, we get:
    1. Image derivatives (optionally, blur first)
    2. Square of derivatives ($I_{x}^{2}, I_{y}^{2}, I_{x}I_{y}$)
    3. Gaussian filter over suqres ($g(\sigma)$)
    4. Cornerness function: both eigenvalues $\lambda$ are strong
    5. NMS
