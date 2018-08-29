import os
from PIL import Image, ImageChops, ImageStat


def get_images(directory):
    images = [
        f.name
        for f in (f for f in os.scandir(directory) if f.is_file())
        if os.path.splitext(f.name)[1] in ('.jpg', '.jpeg', '.png')
           and not f.name.startswith('.')
    ]
    images.sort()
    return images


class IthinProcessor:
    def __init__(self, threshold, size):
        self.threshold = threshold
        self.size = size
        self.groups = [[]]
        self.last_image = None

    def process_file(self, name, filename):
        image = Image.open(filename).resize((self.size, self.size), Image.LANCZOS).convert('RGB')
        if self.last_image:
            delta = ImageChops.difference(image, self.last_image)
            delta_stat = ImageStat.Stat(delta)
            mean = sum(delta_stat.mean) / len(delta_stat.mean) / 255
            if mean > self.threshold:
                self.start_new_group()
        else:
            delta_stat = mean = None
        self.groups[-1].append({
            'image': image,
            'name': name,
            'delta_stat': delta_stat,
            'mean': mean,
        })
        self.last_image = image

    def start_new_group(self):
        self.groups.append([])
