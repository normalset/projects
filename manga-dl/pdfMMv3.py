from PIL import Image
import os

def save_pdf(firstImage, output_pdf, start_chapter, end_chapter, pageImages):
    firstImage.save(
        rf'./{output_pdf} | {start_chapter}-{end_chapter}',
        save_all=True,
        append_images=pageImages
    )

def create_pdf_from_images_multifolder(input_folder, output_pdf):
    subdirectories = [d for d in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, d))]

    if not subdirectories:
        print("No subfolders found.")
        return

    print("Available folders:")
    for i, subdirectory in enumerate(subdirectories):
        print(f"{i + 1}. {subdirectory}")

    try:
        choice = int(input("Enter the number of the folder you want to convert to PDF: ")) - 1
        selected_folder = subdirectories[choice]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return

    if output_pdf is None:
        output_pdf = f"{selected_folder}.pdf"

    print(f"Creating PDF '{output_pdf}' from images in '{selected_folder}'...")

    # Prompt the user for the range of chapters to convert
    try:
        start_chapter = int(input("Enter the starting chapter number (1-based index): "))
        end_chapter = int(input("Enter the ending chapter number: "))
    except ValueError:
        print("Invalid input. Exiting.")
        return

    pageImages = []
    first_folder = True
    chapters_done = 0
    pdf_created = 0
    tot_chapters = 0

    folderList = os.listdir(selected_folder)
    folderList.sort()
    tot_chapters = len(folderList)
    print("folderList:", folderList)
    for folder in folderList:
        chapter_number = float(folder.split(' ')[3])  # Extract chapter number from folder name

        # Check if the chapter is within the specified range
        # Chapter data 
        # print("Chapt data",start_chapter , chapter_number , end_chapter, folder)
        if start_chapter <= chapter_number <= end_chapter:
            path = f'{selected_folder}/{folder}'
            print("defined path:", path)

            pageList = os.listdir(path)
            pageList.sort()
            print("pageList:", pageList)

            print("Pages:")
            pages = [Image.open(f'{path}/{page}') for page in pageList]

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
            

            if chapters_done >= 50 or chapters_done == (end_chapter - start_chapter)+1:
                print(f'Chapters done: {chapters_done}, chapters left: {end_chapter - start_chapter -chapters_done}')

                print(f'{start_chapter}-{end_chapter} | {output_pdf}')
                save_pdf(firstImage, output_pdf, start_chapter, end_chapter, pageImages)
                pageImages = []
                first_folder = True
                chapters_counter = 0
                pdf_created += 1

if __name__ == "__main__":
    input_folder = '.'

create_pdf_from_images_multifolder(input_folder, None)
