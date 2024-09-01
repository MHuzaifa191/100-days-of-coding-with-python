import requests
import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text

def convert_text_to_speech(text, output_file):
    url = "http://api.voicerss.org/"
    parameters = {
        "key": f"{os.environ['voicerss_api']}",
        "src": text,
        "hl": "en-us"
    }

    response = requests.post(url, params=parameters)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {output_file}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    pdf_path = "resume.pdf" 
    api_key = os.environ['voicerss_api']
    output_file = "output.mp3"

    pdf_text = extract_text_from_pdf(pdf_path)
    print(type(pdf_text))
    convert_text_to_speech(pdf_text, output_file)
