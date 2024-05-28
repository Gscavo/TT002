from PIL import Image

img = Image.open("arvore.jpeg")

#img.show()

img.save("arvore2.jpeg")

#converter para png
img.save("arvore2.png")

#descobrir
print(img.size)

img_resized = img.resize((30,30))
img_resized.save("small.jpeg")

#img.rotate(45).show()
#img.rotate(45,expand=True).show()
#img.rotate(90).show()
#img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
#img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
#img.transpose(Image.Transpose.ROTATE_180).show()

pixeis = img_resized.load()

#numero de cores 256^3=16777216

R = 200
G = 200
B = 200

cor = (R,G,B)
pixeis[3,3] = cor

#img_resized.show()
largura = 300
altura = 200
img = Image.new('RGB',(largura,altura),(0,255,255))
img.show()