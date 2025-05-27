import io
import os

from django.http import HttpResponse
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_shopping_cart(ingredients_cart):
    buffer = io.BytesIO()
    pdf_file = canvas.Canvas(buffer)

    font_path = os.path.join(settings.BASE_DIR, 'recipes', 'fonts', 'DejaVuSans.ttf')
    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))

    pdf_file.setFont('DejaVuSans', 24)
    pdf_file.drawString(200, 800, 'Список покупок')

    pdf_file.setFont('DejaVuSans', 14)
    y_position = 750
    for idx, item in enumerate(ingredients_cart, start=1):
        line = f"{idx}. {item['ingredient__name']} — {item['ingredient_value']} {item['ingredient__measurement_unit']}"
        pdf_file.drawString(50, y_position, line)
        y_position -= 20
        if y_position <= 50:
            pdf_file.showPage()
            pdf_file.setFont('DejaVuSans', 14)
            y_position = 800

    pdf_file.save()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="shopping_cart.pdf"'
    return response