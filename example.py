from TkVisualizer import TkAudioVisualizer
import customtkinter

root = customtkinter.CTk()
root.geometry("900x500")
viz = TkAudioVisualizer(root)
viz.pack(fill="both", expand=True, padx=10, pady=10)

customtkinter.CTkButton(root, text="Start", command=viz.start).pack(fill="x", expand=True, side="left", pady=10, padx=10)
customtkinter.CTkButton(root, text="Stop", command=viz.stop).pack(fill="x", expand=True, side="right", pady=10, padx=10)
root.mainloop()
