import qrcode

#1) Simple

# referral link
qr_code=qrcode.make("https://github.com/elizamin-orucov")

# save and filename
qr_code.save("QR-code-git.png")


#

#2) Professional

code = qrcode.QRCode(
    # the size of the QR Code. 1 to 40 range
    version=1,
    # checking the bug fix.(L-about 7% or less errors can be corrected.)
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    #  controls how many pixels each “box” of the QR code is.
    box_size=100,
    # controls how many boxes thick the border should be (default is 4, which is the minimum by properties)
    border=2
)
# referral link
code.add_data("https://www.linkedin.com/in/alizamin-orujzade/")
# automatically checks version size
code.make(fit=True)


# We can color our QR-code using RGB color bundles
# fill_color-painting color
# back_color-background
image = code.make_image(fill_color="yellow",back_color="black")

# save and filename
image.save("linkedin-QR-code.png")










