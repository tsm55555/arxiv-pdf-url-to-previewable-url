def pdf_to_previewable():
    arxix_pdf_url = input("input your arxiv pdf url: ")
    previewable_url = arxix_pdf_url.replace(".pdf", "")
    previewable_url = previewable_url.replace("pdf", "abs")

    print("previewable url: ",previewable_url)

if __name__ == "__main__":
    pdf_to_previewable()