import tkinter as tk
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
import pygame  # Import pygame for audio playback

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file from the working directory
siren_sound = pygame.mixer.Sound("police-siren.mp3")

app = tk.Tk()
app.geometry("600x600")
app.title("Driver Drowsiness Detector.v.01.04")
ctk.set_appearance_mode("dark")

vidFrame = tk.Frame(height=480, width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()

counter = 0
last_played_counter = 0
counterLabel = ctk.CTkLabel(master=app, text=counter, height=40, width=120, font=("Arial", 20), text_color="white", fg_color=("teal", "black"))
counterLabel.pack(pady=10)

def reset_counter():
    global counter, last_played_counter
    counter = 0
    last_played_counter = 0
    counterLabel.configure(text=counter)

resetButton = ctk.CTkButton(master=app, text="Reset Counter", command=reset_counter, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="teal")
resetButton.pack()

model = YOLO("runs/detect/train/weights/best.pt")  # Load the model directly from the file
cap = cv2.VideoCapture(0)

def detect():
    global counter, last_played_counter
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)  # Get results from the model
    
    # Debugging: Print the results
    print("Results:", results)

    if results and results[0].boxes:
        result = results[0]
        img = result.plot()  # Visualize the results

        for box in result.boxes:
            dconf = box.conf
            dclass = box.cls
            
            print(f"Detected class: {dclass}, Confidence: {dconf}")

            if dconf > 0.60:
                if dclass == 0: 
                    print("Detected: Awake")
                elif dclass == 1:
                    print("Detected: Drowsy")
                    # Increment counter
                    counter += 1

                    # Check if counter is a multiple of 5 and greater than the last played counter
                    if counter // 2 > last_played_counter // 2:
                        # Play the police siren sound
                        siren_sound.play()
                        last_played_counter = counter

        imgarr = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(imgarr)
        vid.imgtk = imgtk
        vid.configure(image=imgtk)
        counterLabel.configure(text=counter)

    vid.after(10, detect)

detect()
app.mainloop()
