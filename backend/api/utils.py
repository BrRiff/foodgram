import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def generate_shopping_pdf(ingredients):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)

    pdfmetrics.registerFont(TTFont('CustomArial', 'data/arial.ttf'))

    pdf.setFont('CustomArial', 20)
    pdf.drawString(200, 800, 'Shopping List')

    pdf.setFont('CustomArial', 10)
    vertical_offset = 750
    max_height = 50

    for idx, ingredient in enumerate(ingredients, start=1):
        item_name = ingredient['ingredient__name']
        quantity = ingredient['ingredient_value']
        unit = ingredient['ingredient__measurement_unit']
        line_text = f"{idx}. {item_name}: {quantity} {unit}"

        pdf.drawString(50, vertical_offset, line_text)
        vertical_offset -= 18

        if vertical_offset <= max_height:
            pdf.showPage()
            pdf.setFont('CustomArial', 10)
            vertical_offset = 750

    pdf.save()

    buffer.seek(0)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="shopping_list.pdf"'
    response.write(buffer.read())
    buffer.close()

    return response
