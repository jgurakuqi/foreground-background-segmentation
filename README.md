# foreground_background_segmentation


## Table of Contents

- [Requirements](#Requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Requirements

The goal of this assignment is to perform automatic foreground/background segmentation to extract the silhouette of a target object from a video file, , using the given dataset of videos.
In the package can be found video sequences of 4 objects on a rotating turntable (obj1.mp4 . . . obj4.mp4).
The task is to create a Python program (or notebook) that:
- opens one of the video files cited above
- computes a binary thresholded image for each frame in which the white pixels correspond to the object in the turntable and the black pixels to the background.
- saves the thresholded images onto a video named obj1_mask.mp4, ..., obj4_mask.mp4.
- evaluates the results against a set of ground truth images.

## Implementation nodes:

**main_856180**:

- The user can choose at runtime both the segmentation technique and the video that should be segmented.

- The first chunk includes 2 version of the function that should be invoked to perform the segmentation,
  one parallelised through the python standard multiprocessing library and one without multiprocessing.
  The parallel one was chosen as default, as it allows to achieve way faster execution times: 1.47 seconds
  for the watershed segmentation on the Toucan video without paral., and 43 seconds with parallel on a 8-core
  Intel processor.
  The program was tested on both Linux and Windows systems withouth showing instabilities, but if any problem
  arises with the parallel function (i.e., `parallel_video_segmentation`), its invokation can be replaced 
  with the invokation of the non-parallel version (i.e., `video_segmentation`).

**watershed_segmentation**:

- This file includes two version of the segmentation function
    - One defined as simple function, invoked during tests and in the non-parallel `video_segmentation`.
    - One defines as an invokable object, defined in such a way to be called from the `multiprocessing.Pool.map`,
      allowing at the same time to pass further parameters to the function `watershed_segmentation`, without
      requiring the use of `multiprocessing.Pool.starmap`, which allows multiple arguments, but usually tends
      to introduce a slight overhead.

## Installation

In order to run this project it's required a Python 3 installation, along with the following python modules:
```bash
pip install matplotlib
pip install opencv-python
pip install numpy
```

In order to work, the program requires the related input videos, which must respect the [Requirements](#Requirements) in terms of format.
Also, the path to the package containing the videos is curretly hardcoded in the Jupyter Notebook, targeting as folder called "data", a folder sibling to the one containing the code, hence if required, the path can be updated to match any desired position for the package.

## Usage

To run the projects it's required an IDE suitable to run the Jupyter Notebook.

## Contributing

I implemented the code exploiting the problem-specific characteristics (e.g., semi-constant lightning, same shadow on the background fabric, ...), hence using image processing techniques specific wrt to it, at least for the custom segmentation, hence in order to readapt the custom segmentation algorithm many modifications might be required. On the other hand, the Watershed-based segmentation, followed a more generic approach, and it's easier to readapt to other problems.

```bash
git clone https://github.com/jgurakuqi/foreground_background_segmentation
```

## License

MIT License

Copyright (c) 2023 Jurgen Gurakuqi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
