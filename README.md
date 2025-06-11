# daily_file_sorter
A Python script that automatically sorts files into folders by type every day using Task Scheduler.
# 🗂️ Daily File Sorter Automation Script

This project is a Python automation script that **sorts files by type** (e.g., documents, images, videos, etc.) from a specified folder (`imp docs`) into categorized subfolders. It is scheduled to **run daily** using Windows Task Scheduler.

---

## 📁 Project Objective

To automatically organize files into relevant folders based on file extensions in the `imp docs` directory. This helps maintain a clean, organized workspace without manual effort.

---

## 📸 Before Sorting

Below is an example of the `imp docs` folder **before** the script runs:

![Before Sorting](https://github.com/user-attachments/assets/8addc17e-f6d4-4d6c-90ee-a9e117955d21)


---

## 🛠️ What the Script Does

1. **Checks for required subfolders** inside `imp docs`:
   - `docs files`
   - `image files`
   - `video files`
   - `audio files`
   - `excel files`
   - `pdf files`
   - `csv files`

2. **Moves files based on their extensions** to the relevant folder:
   - `.docx` → `docs files`
   - `.jpg`, `.png` → `image files`
   - `.mp4` → `video files`
   - `.mp3` → `audio files`
   - `.xlsx` → `excel files`
   - `.pdf` → `pdf files`
   - `.csv` → `csv files`

3. **Runs automatically every day** using Windows Task Scheduler.

---

## 📂 Folder Structure After Sorting

Once the script runs, your `imp docs` folder will be organized as shown below:

![After Sorting](https://github.com/user-attachments/assets/3d35127b-dc50-44ad-9355-1dd2244093bc)


Each file type is placed neatly in its respective subfolder.

---

## ⏰ Automation Setup (Windows Task Scheduler)

The script is scheduled to run **once every 24 hours** using Windows Task Scheduler. Here's a snapshot of the task summary:

![Task Scheduler](https://github.com/user-attachments/assets/75efa2d0-dc60-4671-b393-2ca73db9f280)


**Basic Setup Instructions:**
1. Open **Task Scheduler** and create a new task.
2. Set the trigger to run **daily**.
3. Set the action to run:
   - **Program/script**: `C:\Users\Pratibha Rai\AppData\Local\Programs\Python\Python313\python.exe`
   - **Add arguments**: `"C:\Users\Pratibha Rai\Desktop\automation project\daily_file_sorter.py"`
   - **Start in**: `C:\Users\Pratibha Rai\Desktop\automation project`

---

## 📝 How to Run Manually

If needed, you can manually run the script using your terminal:

```bash
cd "C:/Users/Pratibha Rai/Desktop/automation project"
python daily_file_sorter.py
