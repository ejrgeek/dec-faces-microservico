import cv2

from service import send_image


def main():
    camera = cv2.VideoCapture(0)

    img_path = "capturas/imagem.png"

    while True:

        retval, img = camera.read()
        cv2.imshow('TIRAR FOTO:  S - SALVAR   |   ESC - SAIR', img)

        k = cv2.waitKey(100)

        if k == 27:
            break

        elif k == ord('s'):
            cv2.imwrite(img_path, img)
            send_image(img_path=img_path)
            break

    cv2.destroyAllWindows()
    camera.release()
    return


if __name__ == '__main__':
    main()
