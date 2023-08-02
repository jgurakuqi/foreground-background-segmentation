import numpy as np
import cv2 as cv


def watershed_segmentation(frame: np.ndarray, object_indx: int) -> np.ndarray:
    """Perform an image segmentation on the input frame to separate the
    object+pedestal+table from the upper background.
    Such segmentation is performed extracting the different regions of the image
    (foreground, background and unknown), then used to find the connected components
    in the image, which eventually will be used to perform the watershed based
    segmentation.
    Any value chosen for thresholding and distances is chosen using the same technique
    seen in the "custom_segmentation" module with the "test_canny_values" function.

    Args:
        frame (np.ndarray): input image.
        object_indx (int): index of the video from which comes the frame.

    Returns:
        np.ndarray: segmented image.
    """
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # CONTRAST ENHANCEMENT with linear operation (* alpha + beta, but without beta).
    float_gray_img = gray_frame.astype("float32")
    float_gray_img = np.clip(float_gray_img * 1.2, 0, 255)
    gray_frame = (float_gray_img).astype("uint8")

    # Threshold the gray frame: in case of the Toucan video makes use of
    # manual thresholding with a threshold of 135, to keep the beak of the
    # bird, otherwise an OTSU thresholding.
    _, thresh = (
        cv.threshold(
            gray_frame,
            135,
            255,
            cv.THRESH_BINARY_INV,
        )
        if object_indx == 1
        else cv.threshold(
            gray_frame,
            0,
            255,
            cv.THRESH_BINARY_INV + cv.THRESH_OTSU,
        )
    )
    # Finding sure foreground area
    dist_transform = cv.distanceTransform(thresh, cv.DIST_L2, 5)

    # Compute the distance transform to extract the foreground.
    thresh_dist = 0.75 * dist_transform.max()
    _, sure_fg = cv.threshold(dist_transform, thresh_dist, 255, 0)

    sure_fg = np.uint8(sure_fg)
    # Finding unknown region.
    unknown = cv.subtract(thresh, sure_fg)

    # Marker labelling
    _, markers = cv.connectedComponents(sure_fg)

    # Add one to all labels so that the background (i.e., thresh) is not 0, but 1.
    markers = markers + 1

    # Now, mark the region of unknown with zero.
    markers[unknown == 255] = 0

    # Perform the segmentation based on the markers.
    markers = cv.watershed(frame, markers)

    # Use the markers to replicate the segmentation over the original
    # frame.
    frame[markers <= 1] = [255, 255, 255]
    frame[markers > 1] = [0, 0, 0]

    # Perform a morph OPEN to remove clutter in the Dinosaur background.
    frame = cv.morphologyEx(frame, cv.MORPH_OPEN, np.ones((3, 3)))

    return frame


class watershed_segmentation_co(object):
    """This technique is implemented as a callable object in order to make it callable
    by multiple processes without the need of a starmap function, which introduces a
    noticable overhead with respect to map.
    co stands for callable object.

    Args:
        object (object): father object, of type object.
    """

    def __init__(self, object_indx: int):
        """This __init__ method is devised to store the index of the chosen object,
        which will be used once that __call__ will be invoked.

        Args:
            object_indx (int): index of the chosen object/video.
        """
        self.object_indx = object_indx

    def __call__(self: watershed_segmentation, frame: np.ndarray) -> np.ndarray:
        """Perform an image segmentation on the input frame to separate the
        object+pedestal+table from the upper background.
        Such segmentation is performed extracting the different regions of the image
        (foreground, background and unknown), then used to find the connected components
        in the image, which eventually will be used to perform the watershed based
        segmentation.
        Any value chosen for thresholding and distances is chosen using the same technique
        seen in the "custom_segmentation" module with the "test_canny_values" function.

        Args:
            frame (np.ndarray): input image.

        Returns:
            np.ndarray: segmented image.
        """
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Contrast enhancment with linear operation (* alpha + beta, but without beta).
        float_gray_img = gray_frame.astype("float32")
        float_gray_img = np.clip(float_gray_img * 1.2, 0, 255)
        gray_frame = (float_gray_img).astype("uint8")

        # Threshold the gray frame: in case of the Toucan video makes use of
        # manual thresholding with a threshold of 135, to keep the beak of the
        # bird, otherwise an OTSU thresholding.
        _, thresh = (
            cv.threshold(
                gray_frame,
                135,
                255,
                cv.THRESH_BINARY_INV,
            )
            if self.object_indx == 1
            else cv.threshold(
                gray_frame,
                0,
                255,
                cv.THRESH_BINARY_INV + cv.THRESH_OTSU,
            )
        )
        # Finding sure foreground area
        dist_transform = cv.distanceTransform(thresh, cv.DIST_L2, 5)

        # Compute the distance transform to extract the foreground.
        thresh_dist = 0.75 * dist_transform.max()
        _, sure_fg = cv.threshold(dist_transform, thresh_dist, 255, 0)

        sure_fg = np.uint8(sure_fg)
        # Finding unknown region.
        unknown = cv.subtract(thresh, sure_fg)

        # Marker labelling
        _, markers = cv.connectedComponents(sure_fg)

        # Add one to all labels so that the background (i.e., thresh) is not 0, but 1.
        markers = markers + 1

        # Now, mark the region of unknown with zero.
        markers[unknown == 255] = 0

        # Perform the segmentation based on the markers.
        markers = cv.watershed(frame, markers)

        # Use the markers to replicate the segmentation over the original
        # frame.
        frame[markers <= 1] = [255, 255, 255]
        frame[markers > 1] = [0, 0, 0]

        # Perform a morph OPEN to remove clutter in the Dinosaur background.
        frame = cv.morphologyEx(frame, cv.MORPH_OPEN, np.ones((3, 3)))

        return frame
