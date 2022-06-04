import constants

def heightPercentage(percentage):
    return (constants.HEIGHT // 100) * percentage

def widthPercentage(percentage):
    return (constants.WIDTH // 100) * percentage

def buttonWidthPercentage(percentage):
    return (constants.CELL_WIDTH // 100) * percentage

def buttonHeightPercentage(percentage):
    return (constants.CELL_HEIGHT // 100) * percentage