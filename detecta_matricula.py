import cv2
import pytesseract
import imutils
import numpy as np

# Ruta donde está instalado Tesseract en Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cargar imagen
imagen = cv2.imread("C:\\Users\\hgabr\\OneDrive\\Escritorio\\Deteccion_De_Matriculas\\img_Autos\\onix.jpeg")

if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Redimensionar para trabajar más rápido
imagen = imutils.resize(imagen, width=600)

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Filtro bilateral para reducir ruido y mantener bordes
filtrada = cv2.bilateralFilter(gris, 11, 17, 17)

# Detección de bordes
bordes = cv2.Canny(filtrada, 30, 200)

# Encontrar contornos
contornos = cv2.findContours(bordes.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contornos = imutils.grab_contours(contornos)
contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:10]

pantalla = None

# Buscar un contorno con forma rectangular
for c in contornos:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        pantalla = approx
        break

# Si se encontró un contorno rectangular
if pantalla is not None:
    # Dibujar contorno
    cv2.drawContours(imagen, [pantalla], -1, (0, 255, 0), 3)

    # Crear máscara para aislar la matrícula
    mascara = np.zeros(gris.shape, np.uint8)
    nueva_img = cv2.drawContours(mascara, [pantalla], 0, 255, -1)
    nueva_img = cv2.bitwise_and(imagen, imagen, mask=mascara)

    # Recortar la zona de la matrícula
    (x, y) = np.where(mascara == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    recorte = gris[topx:bottomx+1, topy:bottomy+1]

    # OCR sobre el recorte
    texto = pytesseract.image_to_string(recorte, config='--psm 8')

    print("Matrícula detectada:", texto.strip())

    # Mostrar imagen original con la detección
    cv2.imshow("Detección de Matrícula", imagen)
    cv2.imshow("Zona de Matrícula", recorte)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No se detectó ninguna matrícula.")
