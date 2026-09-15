import qrcode  # Main library responsible for creating QR codes
from qrcode.constants import ERROR_CORRECT_L


# Main class for generating QR codes
class QRCodeGenerator:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename + ".png"

    # Generates a QR code image
    def generate(self):
        """Generates a QR code image"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        return img

    # Saves the QR code image to a file
    def save(self):
        """Saves the QR code image to a file"""
        img = self.generate()
        img.save(self.filename)


# Main function to run the QR code generator.
def main():
    """Main function to run the QR code generator."""
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")

    qr_generator = QRCodeGenerator(data, filename)
    qr_generator.save()


# Entry point for the application
if __name__ == "__main__":
    main()
