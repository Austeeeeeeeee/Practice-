import random
from dataclasses import dataclass

@dataclass
class ZOOM_TYPES:
    MINIMUM = 0
    RANDOM = 1
    MAXIMUM = 2

def set_max_zoom() -> int:
    maximum_value = 30000
    return maximum_value

def unique_random_zoom_generator(start=2000, end=30000):
    zoom_values = list(range(start, end + 1))
    random.shuffle(zoom_values)
    for zoom in zoom_values:
        yield zoom

def set_random_zoom_value(zoom_value: int) -> None:
    print(f"Setting random zoom to {zoom_value}")

def check_zoom_after_reboot(zoom_generator, zoom_type=ZOOM_TYPES.RANDOM):
    if zoom_type == ZOOM_TYPES.MAXIMUM:
        max_zoom = set_max_zoom()
        print(f"Setting max zoom: {max_zoom}")
    else:
        random_zoom_value = next(zoom_generator)
        set_random_zoom_value(random_zoom_value)

# Create generator once
zoom_gen = unique_random_zoom_generator()

# Call with zoom_gen and zoom_type
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)
check_zoom_after_reboot(zoom_gen, zoom_type=ZOOM_TYPES.RANDOM)











import random
from dataclasses import dataclass

@dataclass
class ZOOM_TYPES:
    MINIMUM = 0
    RANDOM = 1
    MAXIMUM = 2

def set_max_zoom() -> int:
    maximum_value = 30000
    return maximum_value

def unique_random_zoom_generator(start=0, end=100):
    zoom_values = list(range(start, end + 1))
    random.shuffle(zoom_values)
    for zoom in zoom_values:
        yield zoom

def set_random_zoom_value(zoom_value: int) -> None:
    print(f"Setting random zoom to {zoom_value}")

def check_zoom_after_reboot(zoom_type=ZOOM_TYPES.RANDOM):
    if zoom_type == ZOOM_TYPES.MAXIMUM:
        max_zoom = set_max_zoom()
        print(f"Setting max zoom: {max_zoom}")
    else:
        zoom_generator = unique_random_zoom_generator()
        random_zoom_value = next(zoom_generator)
        set_random_zoom_value(random_zoom_value)

check_zoom_after_reboot(ZOOM_TYPES.RANDOM)