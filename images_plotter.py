from __future__ import annotations
from matplotlib.pyplot import imshow, show, figure
from numpy import ndarray
from copy import deepcopy


"""The classes into this module were devised to allow an easy test of each segmentation
function (e.g., allowing to plot each image after each transformation).
"""


class images_plotter:
    """Store and plot in a unique sequence all the
    required images.
    """

    def __init__(self: images_plotter, images: list[ndarray] = None) -> None:
        """Initialise an empty list of images for the plotter if none is given,
        otherwise store the given one.

        Args:
            self (images_plotter): self instance.
            images (list[ndarray], optional): list of images. Defaults to None.
        """
        self.images = images if images != None and len(images) else []

    def push(self: images_plotter, image: ndarray) -> None:
        """Stores a copy of the given numpy image in order to plot it later.
        The deep copy avoids the possibility of the image being modified after
        it is stored.

        Args:
            self (images_plotter): self instance.
            image (ndarray): image to store.
        """
        self.images.append(deepcopy(image))

    def load_list(self: images_plotter, images: list[ndarray], copy=False) -> None:
        """It stores the given list of numpy images. If the images need to be
        modified after being stored, then it is advised to enable the deepcopy
        of them through the flag "copy".

        Args:
            self (images_plotter): self instance.
            images (list[ndarray]): list/array of numpy images.
            copy (bool, optional): flag which enables the deep copy. Defaults to False.
        """
        self.images = deepcopy(images) if copy else images

    def plot_images(self: images_plotter) -> None:
        """Plot the stored images, resizing the canvas according
        to the number of images.

        Args:
            self (images_plotter): self instance.
        """
        num_of_imgs = len(self.images)
        fig = figure(figsize=(15, int(num_of_imgs * 3.5)))
        for img_index, img in enumerate(self.images):
            fig.add_subplot(num_of_imgs, 3, img_index + 1)
            imshow(img)
        show()


class images_plotter_titled:
    """Store and plot in a unique sequence all the
    required images.
    """

    def __init__(self: images_plotter, images: list[ndarray] = None) -> None:
        """Initialise an empty list of images for the plotter if none is given,
        otherwise store the given one.

        Args:
            self (images_plotter): self instance.
            images (list[ndarray], optional): list of images. Defaults to None.
        """
        self.images = images if images != None and len(images) else []

    def push(self: images_plotter, image: ndarray, title: str) -> None:
        """Stores a copy of the given numpy image in order to
        plot it later along with the given title. The deep copy
        avoids the possibility of the image being modified after
        it is stored.

        Args:
            self (images_plotter): self instance.
            image (ndarray): image to store.
            title (str): title of the image.
        """
        self.images.append((deepcopy(image), title))

    def plot_images(self: images_plotter) -> None:
        """Plot the stored images, resizing the canvas according
        to the number of images, along with the related titles.

        Args:
            self (images_plotter): self instance.
        """
        num_of_imgs = len(self.images)
        fig = figure(figsize=(15, int(num_of_imgs * 3.5)))
        for img_index, img_and_title in enumerate(self.images):
            fig.add_subplot(num_of_imgs, 3, img_index + 1).title.set_text(
                img_and_title[1]
            )
            imshow(img_and_title[0])
        show()
