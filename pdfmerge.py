from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ['CalculusVolume2-OP.pdf', 'linear algebra textbook.pdf']:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()