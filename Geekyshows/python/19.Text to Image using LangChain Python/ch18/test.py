from decouple import config

import base64
from io import BytesIO

from PIL import Image
from langchain_community.llms.edenai import EdenAI


def print_base64_image(base64_string):
    # Decode the base64 string into binary data
    decoded_data = base64.b64decode(base64_string)

    # Create in-memory stream to read the binary data
    image_stream = BytesIO(decoded_data)

    # Open the image using PIL
    image = Image.open(image_stream)

    # Display the image
    image.show()


SECRET_KEY = config("EDEN_API_KEY")
text2image = EdenAI(
    edenai_api_key=SECRET_KEY,
    feature="image",
    provider="openai",
    resolution="512x512",
)
image_output = text2image.invoke("A dog riding a motorcycle")
print_base64_image(image_output)
