import numpy as np
def detect_color_boundaries(espacio, tolerance=20):
    espacio = np.array(espacio)
    height, width, _ = espacio.shape
    sample_pixel = espacio[height // 2, width // 2]
    lower_color = np.maximum(sample_pixel - tolerance, 0)
    upper_color = np.minimum(sample_pixel + tolerance, 255)
    return lower_color, upper_color
def calculate_average_color(matrix):
    matrix = np.array(matrix)
    height, width, _ = matrix.shape
    total_r = np.sum(matrix[:, :, 0])
    total_g = np.sum(matrix[:, :, 1])
    total_b = np.sum(matrix[:, :, 2])
    total_pixels = height * width
    average_r = total_r / total_pixels
    average_g = total_g / total_pixels
    average_b = total_b / total_pixels
    return (average_b, average_g, average_r)