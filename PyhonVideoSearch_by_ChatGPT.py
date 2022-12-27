import os
import html
import humanize

def search_files(folder, file_types):
  # Search for all files of the specified types in the selected folder and its subfolders
  for root, dirs, files in os.walk(folder):
      for file in files:
          for file_type in file_types:
              if file.endswith(file_type):
                  # Get the file size and parent directory name
                  file_size = humanize.naturalsize(os.path.getsize(os.path.join(root, file)))
                  parent_dir = os.path.basename(os.path.normpath(root))
                  # Create a hyperlink to the file in the manifest.html file
                  with open("manifest.html", "a") as f:
                      f.write(f'<a href="{html.escape(os.path.join(root, file))}">{html.escape(file)} ({file_size}) [{parent_dir}]</a><br>\n')

# Prompt the user to enter the path of the folder
folder = input("Enter the path of the folder: ")

# Define a list of video file types
video_file_types = [".mp4", ".avi", ".mkv", ".mov"]

# Create the manifest.html file if it doesn't exist
if not os.path.exists("manifest.html"):
    with open("manifest.html", "w") as f:
        f.write("<html><body>\n")

# Call the search_files function with the specified folder and file types
search_files(folder, video_file_types)

# Close the HTML tags in the manifest.html file
with open("manifest.html", "a") as f:
    f.write("</body></html>")

print("Done!")
