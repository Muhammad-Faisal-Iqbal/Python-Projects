import qrcode

data = input("Enter the text or url: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size = 10, border = 4)

qr.add_data(data)

image = qr.make_image(file_color = "black", back_color = "white")
 
with open(filename, "wb") as file:
	image.save(file)

print(f"QR code saved as {filename}")
