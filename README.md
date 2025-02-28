# Alrayah Market Price Checker

The **Alrayah Market Price Checker** is a simple web application designed to check product prices in Alrayah Market using barcode scanning. The application uses barcode scanning technology to display product details (name, price and inventory) in real-time.

---

## Features

- Scan barcodes to display product details (name, price and inventory).
- Simple and user-friendly interface.
- Displays "Product not found" if the product is not in the database.
- Modern design with attractive visual effects.
- Works on any computer with a camera or scanner.

---

## How to Use

1. **Run the Application**:
   - Ensure all requirements are installed (see [Requirements](#requirements)). 
   `pip install -r requirements.txt`
   - Run the `app.py` file to start the Flask server.
   - Run the `scanner.py` file to start the barcode scanner.

2. **Access the Web Interface**:
   - Open your browser and go to `http://127.0.0.1:5000`.
   - The Price Checker interface will be displayed.

3. **Scan a Barcode**:
   - Use the Scanner to scan a product barcode.
   - If the product is found in the database, its name and price will be displayed.
   - If the product is not found, a "Product not found" message will appear.

---

## Requirements

To run this project, you need the following:

- Python 3.x
- Flask (`pip install flask`)
- Subprocess (`pip install subprocess`)
- Logging (`pip install logging`)
- SQLite3 (included with Python)
- keyboard (`pip install keyboard`)
- Requests (`pip install requests`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bodawy/Price-Checker.git
   cd alrayah-price-checker
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
3. Set up the database:
Ensure the `products.db` SQLite database is in the `DataBases` folder.

	The database should contain a table named `products` with columns: `barcode`, `product_name`, `price`, `previous_price` and `inventory`.     

4. Run the application:	
	```bash
	python app.py
	python scanner.py	
## Project Structure

`app.py`: The main Flask application that handles the web server and API.

`scanner.py`: The barcode scanner script that captures barcodes and sends them to the server.

`index.html`: The main HTML file for the web interface.

`style.css`: The CSS file for styling the web interface.

`DataBases/products.db`: The SQLite database containing product information.

`static/data.json`: Temporary JSON file used to pass product data to the frontend.

## License
This project is licensed under the MIT License. See the LICENSE file for details. [MIT License](LICENSE)

## Contact
For any questions or feedback, feel free to contact:
- **Email**: bodawy.dev@gmail.com
- **Developer**: Bodawy_Dev
