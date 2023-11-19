# manga-dl base project @ https://github.com/daijro/manga-dl.git by daijro
from PIL import Image
import os

def create_pdf_from_images(input_folder, output_pdf):
    # Get a list of subdirectories (assuming each subdirectory contains images)
    subdirectories = [d for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]

    if not subdirectories:
        print("No subfolders found.")
        return

    # Display available subfolders and prompt the user to choose one
    print("Available folders:")
    for i, subdirectory in enumerate(subdirectories):
        print(f"{i + 1}. {subdirectory}")

    try:
        choice = int(input("Enter the number of the folder you want to convert to PDF: ")) - 1
        selected_folder = subdirectories[choice]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return

    # Use the selected folder's name as the PDF name
    if output_pdf is None:
        output_pdf = f"{selected_folder}.pdf"

    print(f"Creating PDF '{output_pdf}' from images in '{selected_folder}'...")

    pageList = os.listdir(selected_folder)
    pageList.sort()
    print("pageList:", pageList)

    print("Pages:")
    pages = []
    for page in pageList:
        print(f'{selected_folder}/{page}')
        pages.append(Image.open(rf'./{selected_folder}/{page}'))
    
    print("Creating img list")
    pageImages = []
    firstImage = pages[0].convert('RGB')
    for img in pages[1:]:
        pageImages.append(img.convert('RGB'))

    print("Saving:")
    firstImage.save(rf'./{output_pdf}' , save_all=True , append_images = pageImages)

if __name__ == "__main__":
  input_folder = '.'

create_pdf_from_images(input_folder, None)
