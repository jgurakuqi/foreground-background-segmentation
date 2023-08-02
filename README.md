# REQUIREMENTS

The folder `data` and `assignment1_test_dataset` should both be place in the folder which contains the code folder.

    E.g.: code in ".../assignment_1/code/main_856180.ipynb", hence ".../assignment_1/data/..." and the
          same applies for assignment1_test_dataset

# PROGRAM FILES

 * `main_856180.ipynb` is the Jupyter file which contains the main program which should be runned to 
   accomplish the required tasks.

 * `watershed_segmentation.py` contains the segmentation implemented through watershed.

 * `custom_segmentation.py` contains the custom implementation, achieved using hsv conversion and
   edge detection.

 * `images_plotter` contains some utility classes used to test the whole segmentation process in each
   step of both the two techniques.

# NOTES ABOUT main_856180

 * The user can choose at runtime both the segmentation technique and the video that should be segmented.

 * The first chunk includes 2 version of the function that should be invoked to perform the segmentation,
   one parallelised through the python standard multiprocessing library and one without multiprocessing.
   The parallel one was chosen as default, as it allows to achieve way faster execution times: 1.47 seconds
   for the watershed segmentation on the Toucan video without paral., and 43 seconds with parallel on a 8-core
   Intel processor.
   The program was tested on both Linux and Windows systems withouth showing instabilities, but if any problem
   arises with the parallel function (i.e., `parallel_video_segmentation`), its invokation can be replaced 
   with the invokation of the non-parallel version (i.e., `video_segmentation`).

# NOTES ABOUT watershed_segmentation

 * This file includes two version of the segmentation function:

    * One defined as simple function, invoked during tests and in the non-parallel `video_segmentation`.

    * One defines as an invokable object, defined in such a way to be called from the `multiprocessing.Pool.map`,
      allowing at the same time to pass further parameters to the function `watershed_segmentation`, without
      requiring the use of `multiprocessing.Pool.starmap`, which allows multiple arguments, but usually tends
      to introduce a slight overhead.