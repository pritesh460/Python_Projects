import pyscreenshot
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
# image = pyscreenshot.grab()
image.show()
image.save("screenshot.png")