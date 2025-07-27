# deteccion_matriculas
Proyecto de detección de matrículas de vehículos utilizando OpenCV para procesamiento de imágenes y Tesseract OCR para reconocimiento de texto
Sistema de Detección de Matrículas Automáticas  desarrollado en Python. Este proyecto utiliza:

OpenCV: Para cargar y manipular imágenes, incluyendo redimensionamiento, conversión a escala de grises, aplicación de filtros bilaterales para reducir ruido, detección de bordes con Canny, y localización de contornos rectangulares que podrían ser matrículas.

Tesseract OCR: Integrado para realizar el reconocimiento óptico de caracteres sobre la región detectada como matrícula.

El proceso incluye la segmentación de la matrícula, su aislamiento mediante máscaras y recortes, y finalmente la extracción del texto para su visualización

# Sistema de Reconocimiento de Matrículas Vehiculares

Este proyecto permite detectar y leer la matrícula de un vehículo desde una imagen usando OpenCV, NumPy, Imutils y Tesseract OCR.

## Requisitos

- Python 3.8 o superior
- Virtualenv
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado en el sistema

## Estructura esperada

```
matricula_rec/
│
├── img_Autos/
│   └── honda1.jpg        # Coloca aquí tus imágenes
├── detecta_matricula.py  # Script principal
├── requirements.txt
└── README.md
```

## Instalación y ejecución

```bash
git clone https://github.com/HGABRIEL19/detencion_matriculas.git
cd detencion_matriculas
python -m venv venv
venv\Scripts\activate        # En Windows (en Linux/Mac usar: source venv/bin/activate)
pip install -r requirements.txt
python detecta_matricula.py
```

> 💡 Asegurate de modificar la línea en `detecta_matricula.py` con la ruta correcta a Tesseract:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Librerías utilizadas

- opencv-python
- pytesseract
- numpy
- imutils

## Resultado esperado

- Muestra en pantalla la imagen original con la matrícula detectada marcada.
- Abre otra ventana con la matrícula recortada.
- Muestra en consola el texto reconocido por OCR, por ejemplo:

<img width="586" height="651" alt="image" src="https://github.com/user-attachments/assets/f51451a5-3e88-473c-8089-67638ef4f2fb" />


Matrícula detectada: KGC-830
```

## Notas

- El sistema puede fallar en imágenes con poca luz o si la matrícula está muy inclinada o sucia.
- Para mejores resultados, usar imágenes bien enfocadas del frente o parte trasera del vehículo.

## Licencia

Uso libre para fines educativos y personales.

