from flask import Flask, render_template, request
from PyPDF2 import PdfMerger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('files')
    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)
    merged_pdf_path = 'merged.pdf'
    merger.write(merged_pdf_path)
    merger.close()
    return merged_pdf_path

if __name__ == '__main__':
    app.run(debug=True)
