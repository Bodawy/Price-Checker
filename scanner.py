import keyboard
import requests

# Flask API endpoint
API_URL = "http://127.0.0.1:5000/scan"

# Buffer to store the barcode
barcode_buffer = ""

def handle_key_event(event):
    global barcode_buffer

    # Check if the event is a key press (down)
    if event.event_type == "down":
        # If the key is "enter", process the barcode
        if event.name == "enter":
            if barcode_buffer:
                print(f"✅ Scanned Barcode: {barcode_buffer.strip()}")
                send_barcode(barcode_buffer.strip())  # Send the barcode to the API
                barcode_buffer = ""  # Clear the buffer after sending
        else:
            # Append the key to the barcode buffer
            barcode_buffer += event.name

def send_barcode(barcode):
    """
    Send the barcode to the Flask API.
    """
    try:
        response = requests.post(API_URL, json={"barcode": barcode})
        if response.status_code == 200:
            print(f"📡 Product Found: {response.json()}")
        else:
            print("❌ Product not found.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send barcode: {e}")

if __name__ == "__main__":
    print("🔍 Waiting for barcode scan... (Press 'Esc' to exit)")

    # Hook into global keyboard events
    keyboard.hook(handle_key_event)

    # Keep the script running
    keyboard.wait("esc")  # Exit when the "Esc" key is pressed