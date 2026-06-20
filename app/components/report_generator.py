"""
WineIQ Analytics — PDF Report Generator

Generates a one-page PDF summary of a prediction using ReportLab.
"""

import os
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "..", "data")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "wine_report.pdf")


def generate_pdf(prediction, details=None):
    """
    Build a short PDF report for a single prediction.

    prediction: 1 (high quality) or 0 (standard quality)
    details: optional dict of {label: value} feature rows to include
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf = SimpleDocTemplate(OUTPUT_PATH)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "WineIQTitle",
        parent=styles["Title"],
        textColor=colors.HexColor("#5c1a33"),
    )

    label = "Premium Quality" if prediction == 1 else "Standard Quality"

    content = [
        Paragraph("🍷 WineIQ Analytics — Prediction Report", title_style),
        Spacer(1, 12),
        Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]),
        Spacer(1, 12),
        Paragraph(f"<b>Predicted Class:</b> {label}", styles["Heading2"]),
        Spacer(1, 12),
    ]

    if details:
        table_data = [["Feature", "Value"]] + [[k, str(v)] for k, v in details.items()]
        table = Table(table_data, colWidths=[2.5 * inch, 2.5 * inch])
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#5c1a33")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8efe0")]),
                ]
            )
        )
        content.append(table)

    pdf.build(content)

    return OUTPUT_PATH