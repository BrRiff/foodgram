import io

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer, Table,
    TableStyle
)


def create_shopping_cart(ingredients_cart):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Список покупок", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    data = [["№", "Ингредиент", "Количество", "Ед. измерения"]]
    for i, item in enumerate(ingredients_cart, start=1):
        data.append([
            str(i),
            item["ingredient__name"],
            str(item["ingredient_value"]),
            item["ingredient__measurement_unit"],
        ])

    table = Table(data, colWidths=[30, 200, 100, 100])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    response = HttpResponse(buffer.read(), content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="shopping_cart.pdf"'
    )
    buffer.close()
    return response
