#!/usr/bin python
import CoreGraphics
def pageCount(pdfPath):
    "Return the number of pages for the PDF document at the given path."
    pdf = CoreGraphics.CGPDFDocumentCreateWithProvider(
              CoreGraphics.CGDataProviderCreateWithFilename(pdfPath)
          )
    return pdf.getNumberOfPages()
if __name__ == '__main__':
    import sys
    for path in sys.argv[1:]:
        print pageCount(path)
