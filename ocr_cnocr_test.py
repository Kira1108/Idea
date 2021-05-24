from cnocr import CnOcr
import matplotlib.pyplot as plt


ocr = CnOcr()
res = ocr.ocr('ocr_imgs/testocr.png')



plt.imshow(plt.imread('ocr_imgs/testocr.png'))
plt.show()
print([''.join(l) for l in res])