import qrcode
url = input("Enter URL : ").strip()
filename = input('Enter yur filename: ').strip()
qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(url)
qr.make(fit = True)
image = qr.make_image(fill_color = 'black',back_color = 'white')
image.save(filename)
print(f'QR code saved as {filename}.')
