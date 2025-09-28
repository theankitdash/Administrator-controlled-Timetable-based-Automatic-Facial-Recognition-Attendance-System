# Admin Controlled Automatic Smart Attendance Recognition System

Python-based facial recognition system for automated, subject-wise student attendance tracking using computer vision algorithms to enhance accuracy and efficiency.

---

## 📖 Project Overlook

1. Admin User Interface  
2. Data managed by **MySQL database**  
3. **OpenCV Frontalface Algorithm** for recognition  
4. **Timetable-based Attendance Management**  

---

## 📝 Project Brief

This project is designed to **ease faculty workload** and **automate attendance tracking** using a timetable-based approach.  

Key Highlights:  
- Built with **Python (Tkinter GUI)**, **ESP32-CAM**, and **ILI9341 display**  
- Uses **MySQL database** for secure and scalable data management  
- Attendance is automatically recorded **within the first 10 minutes of each lecture**  
- Absent students are marked automatically if not detected in that window  
- **OpenCV with LBP Histogram** ensures accurate facial recognition  
- Admins have **full control** to add new users, manage timetable, and monitor attendance  

### Hardware Integration
- **ESP32-CAM**: low-power camera module with Wi-Fi, Bluetooth, and microSD support  
- **ILI9341 TFT Display**: used for user-friendly display output  
- **Arduino Board**: connects and manages hardware components  

---

## 🚀 Features

- Fully automated **smart attendance system**  
- **Subject-wise and timetable-aware attendance**  
- Easy **admin management** for users & schedules  
- **Accurate recognition** using OpenCV + LBP Histogram  
- Scalable for **schools, offices, and institutions**  

---

## 🛠️ Tech Stack

- **Python** (Tkinter GUI)  
- **OpenCV** (Facial Recognition)  
- **MySQL** (Database & Authentication)  
- **ESP32-CAM** + **Arduino**  
- **ILI9341 Display**  

---

## 📦 Setup Instructions

### Prerequisites
- Python **>= 3.8**  
- MySQL Server installed  
- ESP32-CAM + Arduino IDE configured  

### Installation
```bash
git clone https://github.com/theankitdash/Smart-Attendance-System.git
cd Smart-Attendance-System
pip install -r requirements.txt
