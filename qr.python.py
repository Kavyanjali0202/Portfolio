import qrcode

# Define the website URL
url = "https://kavyanjali0202.github.io/Portfolio/"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=5,  # Controls the size of the QR Code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)

# Add URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Generate the QR code without a logo
qr_img = qr.make_image(fill="black", back_color="white")

# Save the final QR code
qr_img.save("custom_qr.png")

print("QR code generated successfully! Check your project folder for 'custom_qr.png'.")
