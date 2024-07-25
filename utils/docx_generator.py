# utils/docx_generator.py
from docx import Document

def populate_template(template_path, data):
    doc = Document(template_path)
    for p in doc.paragraphs:
        for key, value in data.items():
            if key in p.text:
                p.text = p.text.replace(f'{{{key}}}', str(value))
    output_path = template_path.replace('.docx', '_populated.docx')
    doc.save(output_path)
    return output_path
