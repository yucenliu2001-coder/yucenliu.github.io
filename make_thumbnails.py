from pathlib import Path
from PIL import Image

# Original photos
source_dir = Path("static/photos")

# Thumbnail destination
output_dir = source_dir / "thumbnails"
output_dir.mkdir(parents=True, exist_ok=True)

MAX_WIDTH = 1600
QUALITY = 85

for image_path in source_dir.glob("*"):
    if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    # Don't process images inside the thumbnails folder
    if image_path.parent == output_dir:
        continue

    try:
        with Image.open(image_path) as img:

            # Keep original proportions
            width, height = img.size

            if width > MAX_WIDTH:
                new_height = int(height * MAX_WIDTH / width)
                img = img.resize(
                    (MAX_WIDTH, new_height),
                    Image.Resampling.LANCZOS
                )

            output_path = output_dir / image_path.name

            # Convert PNG/RGBA to RGB for JPEG
            if output_path.suffix.lower() in [".jpg", ".jpeg"]:
                if img.mode != "RGB":
                    img = img.convert("RGB")

                img.save(
                    output_path,
                    "JPEG",
                    quality=QUALITY,
                    optimize=True
                )
            else:
                img.save(output_path, optimize=True)

            print(f"Created: {output_path}")

    except Exception as e:
        print(f"Could not process {image_path}: {e}")

print("\nDone!")