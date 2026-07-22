import tkinter as tk

root = tk.Tk()
root.title("lyrics")
root.withdraw()
active_boxes = 0


def box(x, xpos, ypos, delay):
    global active_boxes
    active_boxes += 1

    def spawn():
        bOl = tk.Toplevel(root)
        bOl.title(":(")
        bOl.geometry(f"420x470+{xpos}+{ypos}")

        lyric = tk.Text(
            bOl,
            font=("Arial Narrow", 90),
            wrap="word",
            spacing3=20,
            bg=root.cget("bg"),
            bd=0,
            highlightthickness=0,
        )
        bOl.protocol("WM_DELETE_WINDOW", root.destroy)
        lyric.insert("1.0", x)
        lyric.config(state="disabled")
        lyric.pack(side="left", anchor="w", padx=20, fill="both", expand=True)
        yposrn = ypos

        def slide():
            nonlocal yposrn
            global active_boxes
            yposrn += 5
            bOl.geometry(f"420x470+{xpos}+{yposrn}")
            if yposrn < 1080:
                bOl.after(10, slide)
            else:
                bOl.destroy()
                active_boxes -= 1
                if active_boxes == 0:
                    root.destroy()

        slide()

    root.after(int(delay * 1000), spawn)


box("kung ako lang", 100, -500, 1)
box("kung ako lang", 600, -500, 4)
box("ay d ko", 900, -500, 6)
box("sasabihin", 200, -500, 8)
box("para sayo", 400, -500, 14)
box("para sayo", 700, -500, 17)
box("kailangan kang", 200, -500, 19)
box("limutin", 500, -500, 23)
"""
def lyric(x):
    root.title("Lyrics")
    root.geometry("420x470")
    lyrics=tk.Text(root,
                font=("Arial Narrow", 90),
                wrap="word",
                spacing3=20,
                bg=root.cget("bg"),
                bd=0,
                highlightthickness=0
    )
    lyrics.insert("1.0", x)
    lyrics.config(state="disabled")
    lyrics.pack(side="left", anchor="w", padx=20, fill="both", expand=True)
lyric()
"""
root.mainloop()
