from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(prediction):
    pdf = SimpleDocTemplate("wine_report.pdf")

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            f"Prediction: {prediction}",
            styles["Title"]
        )
    ]

    pdf.build(content)

    return "wine_report.pdf"