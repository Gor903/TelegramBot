import easyocr


def read_text(photo):
    photo_bytes = photo.read()
    reader = easyocr.Reader(['en', 'ru'])
    text = reader.readtext(photo_bytes, detail=0, paragraph=True)
    return '\n'.join(text)
