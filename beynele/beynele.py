import requests
import base64
from PIL import Image
import io
import os

# --- Configuration ---
from config import API_MAIN_BEYNELE

def generate_image_with_beynele(
    prompt: str,
    api_key: str,
    steps: int = 30,
    guidance: float = 4.0,
    width: int = 1024,
    height: int = 1024,
    batch_size: int = 1
):
    """
    Generates an image from text using the Beynele API.

    :param prompt: Text describing the image (supports Kazakh, Russian, English).
    :param api_key: API key for the Beynele service.
    :param steps: Number of inference steps (affects image quality).
    :param guidance: Guidance scale (CFG), controls how closely the image matches the prompt.
    :param width: Image width in pixels.
    :param height: Image height in pixels.
    :param batch_size: Number of images to generate in a single request (1-4).
    :return: A list of Base64 encoded images, or None if an error occurs.
    """
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Error: Please set your API key in the API_MAIN_BEYNELE variable.")
        return None
        
    base_url = "https://beynele.nu.edu.kz/api/v1"
    endpoint = "/generate/batch"
    url = f"{base_url}{endpoint}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare parameters for the GET request
    params = {
        "prompt": prompt,
        "steps": steps,
        "guidance": guidance,
        "width": width,
        "height": height,
        "batchSize": batch_size
    }

    print("Sending request to generate image...")
    
    try:
        # The API can be slow, so a longer timeout is recommended
        response = requests.get(url, headers=headers, params=params, timeout=120)

        if response.status_code == 200:
            result = response.json()
            images_base64 = result.get("images")
            if images_base64:
                print("Images generated successfully!")
                return images_base64
            else:
                print("Error: No images found in the response.")
                return None
        else:
            print(f"Server Error: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None

def save_and_show_images(images_base64: list, prompt: str):
    """
    Saves and displays the Base64 images.
    """
    if not os.path.exists("generated_images"):
        os.makedirs("generated_images")

    for i, img_b64 in enumerate(images_base64):
        try:
            # Decode the Base64 string
            img_data = base64.b64decode(img_b64)
            
            # Generate a filename from the prompt
            safe_prompt = "".join(filter(str.isalnum, prompt))[:30]
            filename = f"generated_images/{safe_prompt}_{i + 1}.png"

            # Save the image to a file
            with open(filename, "wb") as f:
                f.write(img_data)
            print(f"Image saved to '{filename}'.")

            # Uncomment the lines below to automatically open the image
            # image = Image.open(io.BytesIO(img_data))
            # image.show()

        except Exception as e:
            print(f"Error saving image: {e}")

if __name__ == "__main__":
    # You can write a prompt on any topic, including Kazakhstan-related ones
    example_prompt = "Bayterek monument in Astana, cyberpunk style"
    
    # Generate images via the API
    generated_images = generate_image_with_beynele(
        prompt=example_prompt, 
        api_key=API_MAIN_BEYNELE,
        batch_size=1 # Set the number of images to generate (1-4)
    )

    # Process the result
    if generated_images:
        save_and_show_images(generated_images, example_prompt)