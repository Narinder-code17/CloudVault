import tkinter as tk
import random

# Game configuration
WIDTH = 600
HEIGHT = 400
SIZE = 20
INITIAL_DELAY = 200  # Initial speed: higher means slower
SPEED_INCREMENT = -10  # Reduce delay by 10ms after each food (speed increases)
MIN_DELAY = 50  # Set a minimum speed limit

# Direction vectors
DIRS = {
    "Left": (-1, 0),
    "Right": (1, 0),
    "Up": (0, -1),
    "Down": (0, 1)
}

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.reset()

        self.master.bind("<Key>", self.on_key_press)
        self.game_loop()

    def reset(self):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = DIRS["Right"]
        self.spawn_food()
        self.game_over = False
        self.score = 0
        self.delay = INITIAL_DELAY  # Initialize delay

    def spawn_food(self):
        x = random.randrange(0, WIDTH, SIZE)
        y = random.randrange(0, HEIGHT, SIZE)
        self.food = (x, y)

    def on_key_press(self, event):
        if event.keysym in DIRS:
            new_dir = DIRS[event.keysym]
            if (new_dir[0] + self.direction[0] != 0) or (new_dir[1] + self.direction[1] != 0):
                self.direction = new_dir

    def game_loop(self):
        if not self.game_over:
            self.update_snake()
            self.draw_objects()
            self.master.after(self.delay, self.game_loop)
        else:
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2,
                text="GAME OVER", fill="red",
                font=("Arial", 30)
            )

    def update_snake(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx * SIZE, head_y + dy * SIZE)

        # Wall collision
        if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            self.game_over = True
            return

        # Self collision
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # Food eaten
        if new_head == self.food:
            self.spawn_food()
            self.score += 1

            # Speed up the snake
            self.delay = max(self.delay + SPEED_INCREMENT, MIN_DELAY)
        else:
            self.snake.pop()

    def draw_objects(self):
        self.canvas.delete("all")

        # Draw food
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx + SIZE, fy + SIZE, fill="red")

        # Draw snake
        for i, (sx, sy) in enumerate(self.snake):
            color = "green" if i == 0 else "light green"
            self.canvas.create_rectangle(sx, sy, sx + SIZE, sy + SIZE, fill=color)

        # Draw eyes
        head_x, head_y = self.snake[0]
        eye_size = 4
        offset = 4
        if self.direction in [DIRS["Left"], DIRS["Right"]]:
            eye1_x = head_x + offset
            eye1_y = head_y + offset
            eye2_x = head_x + offset
            eye2_y = head_y + SIZE - offset - eye_size
        else:
            eye1_x = head_x + offset
            eye1_y = head_y + offset
            eye2_x = head_x + SIZE - offset - eye_size
            eye2_y = head_y + offset

        self.canvas.create_oval(eye1_x, eye1_y, eye1_x + eye_size, eye1_y + eye_size, fill="white")
        self.canvas.create_oval(eye2_x, eye2_y, eye2_x + eye_size, eye2_y + eye_size, fill="white")

        # Draw score
        self.canvas.create_text(10, 10, anchor="nw", fill="white",
                                font=("Arial", 16), text=f"Score: {self.score}")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
