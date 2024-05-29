import pyshorteners
import tkinter as tk
from tkinter import ttk

def shorten_url():
    url = url_entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    result_label.config(text=f"Shortened URL: {short_url}")

root = tk.Tk()
root.title("URL Shortener")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(main_frame, text="Enter the URL:")
url_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))

url_entry = ttk.Entry(main_frame, width=50)
url_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

shorten_button = ttk.Button(main_frame, text="Shorten URL", command=shorten_url)
shorten_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

result_label = ttk.Label(main_frame, text="")
result_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)

root.mainloop()