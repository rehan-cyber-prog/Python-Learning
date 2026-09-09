import qrcode
text = input("Enter text or URL: ")
img = qrcode.make(text)
img.save("my_qr.png")
print("QR Code Generated Successfully!")
print("Image Name: my_qr.png")





