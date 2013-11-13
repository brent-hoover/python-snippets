for l, w, sort_command in lists:
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Button(frame, text=l, borderwidth=1, relief=RAISED,
                   command=sort_command).pack(fill=X)
