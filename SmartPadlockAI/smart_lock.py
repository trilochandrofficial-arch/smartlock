import tkinter as tk
from tkinter import ttk
import time


def generate_pins():
    result_box.delete(1.0, tk.END)

    try:
        target = int(sum_entry.get())
    except:
        result_box.insert(tk.END, "Please enter a valid number!")
        return

    even = [0, 2, 4, 6, 8]
    candidates = []

    start = time.time()

    # Heuristic Search
    for a in even:
        if a > target:
            continue

        for b in even:
            if a + b > target:
                continue

            for c in even:
                if a + b + c > target:
                    continue

                d = target - (a + b + c)

                if d in even:
                    candidates.append(f"{a}{b}{c}{d}")

    end = time.time()

    result_box.insert(
        tk.END,
        f"AI Smart Padlock Search\n"
    )
    result_box.insert(
        tk.END,
        f"Target Sum = {target}\n\n"
    )

    for i, pin in enumerate(candidates, 1):
        result_box.insert(tk.END, f"{i}. {pin}\n")

    result_box.insert(
        tk.END,
        f"\nTotal Valid PINs: {len(candidates)}"
    )

    result_box.insert(
        tk.END,
        f"\nExecution Time: {(end-start):.6f} seconds"
    )


# Window
root = tk.Tk()
root.title("AI Smart Padlock Security Tool")
root.geometry("700x600")

title = tk.Label(
    root,
    text="AI Smart Padlock Security Testing Tool",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(
    frame,
    text="Enter Required Sum:"
).pack(side=tk.LEFT, padx=5)

sum_entry = tk.Entry(frame, width=10)
sum_entry.insert(0, "16")
sum_entry.pack(side=tk.LEFT)

btn = tk.Button(
    frame,
    text="Generate PINs",
    command=generate_pins
)
btn.pack(side=tk.LEFT, padx=10)

result_box = tk.Text(
    root,
    width=70,
    height=25
)
result_box.pack(pady=15)

scroll = ttk.Scrollbar(
    root,
    command=result_box.yview
)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

result_box.config(
    yscrollcommand=scroll.set
)

root.mainloop()