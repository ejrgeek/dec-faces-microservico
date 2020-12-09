import io
from PIL import Image
from starlette.responses import JSONResponse

from apps.detection.deteccao import Deteccao


async def detectar(request):

    form = await request.form()

    print(dict(form))

    bytes_imagem = await form['imagem'].read()

    image_stream = io.BytesIO(bytes_imagem)

    image = Image.open(image_stream).convert("RGBA")

    image_stream.close()
    image.save('apps/detection/image.png')

    deteccao = Deteccao(img_path='apps/detection/image.png')
    total_rostos = deteccao.detectar_rostos()

    return JSONResponse({
        'total_rostos': total_rostos,
    })
