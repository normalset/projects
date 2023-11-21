from PIL import Image
import os

def save_pdf(firstImage , output_pdf , pdf_created , chapters_counter, pageImages):
    firstImage.save(rf'./{pdf_created * 50 + 1}-{pdf_created * 50 + chapters_counter} | {output_pdf}' , save_all=True , append_images = pageImages)

def create_pdf_from_images_multifolder(input_folder, output_pdf):
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

    #get folders

    #? Variables used
    pageImages = []
    first_folder = True
    chapters_done = 0
    chapters_counter = 0
    pdf_created = 0
    tot_chapters = 0


    folderList = os.listdir(selected_folder)
    folderList.sort()
    tot_chapters = len(folderList)
    print("folderList:" , folderList)
    for folder in folderList:
        path = f'{selected_folder}/{folder}'
        print("defined path: ", path)
       # #getImages
        pageList = os.listdir(path)
        pageList.sort()
        print("pageList:", pageList)

        print("Pages:")
        pages = []
        for page in pageList:
            print(f'{path}/{page}')
            pages.append(Image.open(rf'./{path}/{page}'))
        
        print("Creating img list")
        if first_folder:
          firstImage = pages[0].convert('L')
          first_folder = False
          for img in pages[1:]:
              pageImages.append(img.convert('L'))
        else:
          for img in pages:
              pageImages.append(img.convert('L'))

        chapters_done += 1
        chapters_counter += 1
        if chapters_counter >= 50 or chapters_done == tot_chapters:
            print(f'Saving: {pdf_created * 50 + 1}-{pdf_created * 50 + chapters_counter} | {output_pdf}')

            save_pdf(firstImage , output_pdf , pdf_created , chapters_counter ,pageImages)
            pageImages = []
            first_folder = True
            chapters_counter = 0 
            pdf_created += 1

    # print("Saving:")
    # save_pdf(firstImage , output_pdf , pdf_created , pageImages)
    

if __name__ == "__main__":
  input_folder = '.'

create_pdf_from_images_multifolder(input_folder, None)
