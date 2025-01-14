import pytesseract
from PIL import Image

# Extract and evaluate the expression from an image
def evaluate_expression_from_image(filename="expression.png"):
    try:
        # Load the image
        image = Image.open(filename)

        # Use Tesseract OCR to extract text with better configuration
        extracted_text = pytesseract.image_to_string(image, config="--psm 7").strip()

        # Debug: Print the extracted text
        print(f"Extracted text: '{extracted_text}'")

        # Clean up the extracted text (remove unwanted characters)
        valid_chars = "0123456789+-*/.() "
        cleaned_text = ''.join(char for char in extracted_text if char in valid_chars)

        # Debug: Print the cleaned text
        print(f"Cleaned text: '{cleaned_text}'")

        # Evaluate the cleaned expression
        result = eval(cleaned_text)
        return result
    except Exception as e:
        return f"Error: {e}"

# Evaluate the expression from the image
result = evaluate_expression_from_image()
print(f"Evaluated result: {result}")



