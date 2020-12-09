import cv2


class Deteccao:

    def __init__(self, img_path):
        self.__img = cv2.imread(img_path)
        self.__padrao_rostos = cv2.CascadeClassifier('apps/detection/cascades/haarcascade_frontalface_default.xml')
        self.__imagem_cinza = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)

    def detectar_rostos(self) -> int:
        """
        Detecta rostos nas fotos e retorna o total encontrado
        """
        face_detect = self.__padrao_rostos.detectMultiScale(
            self.__imagem_cinza,
            scaleFactor=1.2,
            minNeighbors=3,
            minSize=(30, 30)
        )

        print("Total de faces > ", len(face_detect))

        print("Matriz da posicao das faces \n|  x  |  y  |  l  |  a  |\n-----------------------|")

        for (x, y, l, a) in face_detect:
            print("|", x, "|", y, "|", l, "|", a, "|", )
            # cv2.rectangle(self.__img, (x, y), (x + l, y + a), (255, 0, 255), 2)
            print("--------------------")

        print("x > Coordenada X\ny > Coordenada Y\nl > Largura\na > Altura")

        return len(face_detect)
