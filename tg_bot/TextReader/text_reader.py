import easyocr


def read_text(photo, language: str) -> str:
    photo_bytes = photo.read()
    reader = easyocr.Reader([*language])
    text = reader.readtext(photo_bytes, detail=0, paragraph=True)
    return '\n'.join(text)
