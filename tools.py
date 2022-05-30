import constants

def height_percentage(percentage):
    return (constants.HEIGHT // 100) * percentage

def width_percentage(percentage):
    return (constants.WIDTH // 100) * percentage

def button_width_percentage(percentage):
    return (constants.CELL_WIDTH // 100) * percentage

def button_height_percentage(percentage):
    return (constants.CELL_HEIGHT // 100) * percentage