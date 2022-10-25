from reportlab.pdfgen import canvas

my_canvas = canvas.Canvas("Report.pdf")
my_canvas.drawString(100, 750, "Analyze Report")
my_canvas.save()