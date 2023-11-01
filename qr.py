import qrcode
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=2,
)
qr.add_data(input("Enter the data to be made into qr : "))
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save("qr.png")