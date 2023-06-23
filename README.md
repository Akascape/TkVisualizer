# TkVisualizer
**Simple audio visualizer widget made with tkinter python.**

![Screenshot](https://github.com/Akascape/TkVisualizer/assets/89206401/5f16df2c-0dce-42a6-ac1c-78664314a35a)

## TkAudioVisualizer
### [<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Akascape/TkVisualizer?&color=white&label=Download%20Source%20Code&logo=Python&logoColor=yellow&style=for-the-badge"  width="400">](https://github.com/Akascape/TkVisualizer/archive/refs/heads/main.zip)
### Example:
```python
from TkVisualizer import TkAudioVisualizer
import customtkinter

root = customtkinter.CTk()
root.geometry("900x500")
viz = TkAudioVisualizer(root)
viz.pack(fill="both", expand=True, padx=10, pady=10)

customtkinter.CTkButton(root, text="Start", command=viz.start).pack(fill="x", expand=True, side="left", pady=10, padx=10)
customtkinter.CTkButton(root, text="Stop", command=viz.stop).pack(fill="x", expand=True, side="right", pady=10, padx=10)
root.mainloop()
```

**Valid arguments:** `master`, `bar_width`, `bar_color`, `gradient`, `width`, `height`

**Valid methods:** `.start()` and `.stop()`

Note: This widget is in beta stage, further development needed!
