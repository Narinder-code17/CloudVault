from tkinter import *
import time
import math
from PIL import Image, ImageTk

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.root.resizable(0, 0)

        self.canvas = Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()

        self.center_x = 200
        self.center_y = 200
        self.clock_radius = 180

        self.update_clock()

    def draw_clock_face(self):
        self.canvas.delete("all")

        # Draw outer circle
        self.canvas.create_oval(
            self.center_x - self.clock_radius,
            self.center_y - self.clock_radius,
            self.center_x + self.clock_radius,
            self.center_y + self.clock_radius,
            outline="white", width=4
        )

        # Draw hour markers
        for i in range(12):
            angle = math.radians(i * 30)
            x_outer = self.center_x + self.clock_radius * 0.9 * math.sin(angle)
            y_outer = self.center_y - self.clock_radius * 0.9 * math.cos(angle)

            x_inner = self.center_x + self.clock_radius * 0.75 * math.sin(angle)
            y_inner = self.center_y - self.clock_radius * 0.75 * math.cos(angle)

            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="white", width=3)

            # Add numbers (3, 6, 9, 12)
            if i in [0, 3, 6, 9]:
                number = {0: "12", 3: "3", 6: "6", 9: "9"}[i]
                x_text = self.center_x + self.clock_radius * 0.6 * math.sin(angle)
                y_text = self.center_y - self.clock_radius * 0.6 * math.cos(angle)
                self.canvas.create_text(x_text, y_text, text=number, fill="white", font=("Arial", 16, "bold"))

    def draw_hand(self, angle_deg, length, width, color):
        angle_rad = math.radians(angle_deg)
        x = self.center_x + length * math.sin(angle_rad)
        y = self.center_y - length * math.cos(angle_rad)
        self.canvas.create_line(self.center_x, self.center_y, x, y, fill=color, width=width)

    def update_clock(self):
        self.draw_clock_face()

        # Get current time
        t = time.localtime()
        hour = t.tm_hour % 12
        minute = t.tm_min
        second = t.tm_sec

        # Calculate angles
        hour_angle = (hour + minute / 60) * 30
        minute_angle = (minute + second / 60) * 6
        second_angle = second * 6

        # Draw hands
        self.draw_hand(hour_angle, 60, 6, "white")
        self.draw_hand(minute_angle, 90, 4, "white")
        self.draw_hand(second_angle, 100, 2, "red")

        # Update every 1000 ms
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    clock = AnalogClock(root)
    root.mainloop()

