
document
  .getElementById("choose-folder-button")
  .addEventListener("click", async () => {
    // Ensure the File System Access API is supported
    if ("showDirectoryPicker" in window) {
      try {
        const dirHandle = await window.showDirectoryPicker();
        document.getElementById("folder_path").value = dirHandle.name; // Display the selected directory name
        // Store the directory handle for later use
        window.selectedDirHandle = dirHandle;
      } catch (err) {
        console.error("Error selecting directory:", err);
      }
    } else {
      alert("Directory picker is not supported by this browser.");
    }
  });

document
  .getElementById("download-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission

    if (!window.selectedDirHandle) {
      alert("Please choose a directory first.");
      return;
    }

    const url = document.getElementById("url").value;
    const folderPath = document.getElementById("folder_path").value;
    document.getElementById("progress-container").style.display = "block";

    // Fetch video data and save it to the chosen directory
    try {
      const response = await fetch(url);
      const blob = await response.blob();
      const fileName = url.split("/").pop() + ".mp4"; // Extract a file name from the URL

      const fileHandle = await window.selectedDirHandle.getFileHandle(
        fileName,
        { create: true }
      );
      const writableStream = await fileHandle.createWritable();
      await writableStream.write(blob);
      await writableStream.close();

      alert("Download complete");
    } catch (error) {
      console.error("Error downloading video:", error);
    }
  });
