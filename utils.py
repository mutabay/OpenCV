from matplotlib import pyplot as plt
import cv2


def plot_opencv_image(image, title='image'):
    # Converting BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.title(title)
    plt.imshow(rgb_image)
    plt.show()
