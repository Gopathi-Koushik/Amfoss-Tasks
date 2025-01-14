from PIL import Image, ImageDraw, ImageFont

# Create an image with an arithmetic expression
def create_image_with_expression(expression, filename="expression.png"):
    try:
        # Create a blank image
        width, height = 300, 100
        image = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(image)

        # Use a clear TrueType font
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Ensure this path exists
        font = ImageFont.truetype(font_path, size=40)

        # Calculate text position
        text_bbox = draw.textbbox((0, 0), expression, font=font)
        text_x = (width - (text_bbox[2] - text_bbox[0])) // 2
        text_y = (height - (text_bbox[3] - text_bbox[1])) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), expression, fill="black", font=font)

        # Save the image
        image.save(filename)
        print(f"Image created successfully as {filename}")
    except Exception as e:
        print(f"Failed to create image: {e}")

# Generate an image with "2 + 2"
create_image_with_expression("2 + 2")



