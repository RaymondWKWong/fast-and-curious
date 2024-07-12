import numpy as np

def calculate_uncertain_cuboid_statistics(n_sample, mean_length, mean_width, mean_height, range_length, range_width, range_height):
    '''
    Calculate the mean and standard deviation of the volume of a cuboid with uncertain dimensions.
    :param n_sample: int, The number of samples to take.
    :param mean_length: float, The mean length of the cuboid.
    :param range_length: float, The range of the length of the cuboid.
    :param mean_width: float, The mean width of the cuboid.
    :param range_width: float, The range of the width of the cuboid.
    :param mean_height: float, The mean height of the cuboid.
    :param range_height: float, The range of the height of the cuboid.
    :return: tuple, The mean volume and standard deviation of the volume of the cuboid.
    '''

    # Calculate the start and end of the ranges for the dimensions - avoids repeated calculations
    length_start = mean_length - range_length / 2
    length_end = mean_length + range_length / 2
    width_start = mean_width - range_width / 2
    width_end = mean_width + range_width / 2
    height_start = mean_height - range_height / 2
    height_end = mean_height + range_height / 2

    # Use numpy to generate random samples rather than random to allow for vectorized operations
    lengths = np.random.uniform(length_start, length_end, n_sample)
    widths = np.random.uniform(width_start, width_end, n_sample)
    heights = np.random.uniform(height_start, height_end, n_sample)

    # Calculate the volumes of the cuboids
    volumes = lengths * widths * heights

    # Calculate the mean and standard deviation of the volumes
    mean_volume = np.mean(volumes)
    std_volume = np.std(volumes)

    # Return the mean and standard deviation of the volumes
    return mean_volume, std_volume