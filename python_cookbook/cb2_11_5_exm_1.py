def test():
    frame = Frame()
    frame.pack(fill=BOTH, expand=YES)
    if os.name == "nt":
        frame.option_add("*font", "Tahoma 8")    # Win default, Tk uses other
    # The editors
    entry = DiacriticalEntry(frame)
    entry.pack(fill=BOTH, expand=YES)
    text = DiacriticalText(frame, width=76, height=25, wrap=WORD)
    if os.name == "nt":
        text.config(font="Arial 10")
    text.pack(fill=BOTH, expand=YES)
    text.focus()
    frame.master.title("Diacritical Editor")
    frame.mainloop()
if __name__ == "__main__":
    test()
