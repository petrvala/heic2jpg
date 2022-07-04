from pathlib import Path
import re

from wand.image import Image


p = Path()
base_dir = p.resolve()
source_dir = p.joinpath(base_dir, "heic")
target_dir = p.joinpath(base_dir, "jpg")

for source_file in source_dir.iterdir():
    if source_file.name.lower().endswith(".heic"):
        insensitive_extension = re.compile(re.escape(".heic"), re.IGNORECASE)
        target_file_name = insensitive_extension.sub(".jpg", source_file.name)
        target_file = p.joinpath(target_dir, target_file_name)
        print(f"Converting {source_file} -> {target_file}")
        img = Image(filename=source_file)
        img.format = 'jpg'
        img.save(filename=target_file)
        img.close()
    else:
        print(f"Not HEIC file: {source_file}")
