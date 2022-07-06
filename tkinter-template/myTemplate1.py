import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

class myTemplate1():

    def __init__(self):
        self.root = tk.Tk()

        # ウィンドウ
        self.root.title('myTemplate1')
        self.root.geometry('1000x700+50+50')
        self.root.resizable(width=False, height=False)
        self.root.attributes('-alpha', 0.95)

        # ファイル選択
        self.label_txtFile = ttk.Label(self.root, text='文章ファイル', anchor=tk.CENTER)
        self.label_txtFile.place(x=0, y=0, width=75, height=25)
        self.entry_txtFile = ttk.Entry(self.root)
        self.entry_txtFile.place(x=75, y=0, width=375, height=25)
        self.button_txtFile = ttk.Button(self.root, text='選択', command=self.txtFile_clicked)
        self.button_txtFile.place(x=450, y=0, width=50, height=25)

        self.label_valFile = ttk.Label(self.root, text='変数ファイル', anchor=tk.CENTER)
        self.label_valFile.place(x=0, y=25, width=75, height=25)
        self.entry_valFile = ttk.Entry(self.root)
        self.entry_valFile.place(x=75, y=25, width=375, height=25)
        self.button_valFile = ttk.Button(self.root, text='選択', command=self.valFile_clicked)
        self.button_valFile.place(x=450, y=25, width=50, height=25)

        self.label_arrow = ttk.Label(self.root, text='▶', anchor=tk.CENTER)
        self.label_arrow.place(x=500, y=0, width=25, height=50)

        self.button_verify = ttk.Button(self.root, text='検証')
        self.button_verify.place(x=525, y=0, width=75, height=50)

        # プレビュー
        self.preview = scrolledtext.ScrolledText(self.root)
        self.preview.place(x=0, y=50, width=600, height=600)

        self.button_prev = ttk.Button(self.root, text='<')
        self.button_prev.place(x=0, y=650, width=50, height=25)
        self.button_next = ttk.Button(self.root, text='>')
        self.button_next.place(x=50, y=650, width=50, height=25)

        self.label_idxVar = tk.StringVar()
        self.label_idx = ttk.Label(self.root, textvariable=self.label_idxVar, anchor=tk.CENTER)
        self.label_idx.place(x=100, y=650, width=160, height=25)

        # ボタン群
        self.button_again = ttk.Button(self.root, text='ファイルを再選択')
        self.button_again.place(x=260, y=650, width=120, height=25)
        self.button_exec = ttk.Button(self.root, text='メールの送信開始')
        self.button_exec.place(x=380, y=650, width=120, height=25)
        self.button_cancel = ttk.Button(self.root, text='送信を中止')
        self.button_cancel.place(x=510, y=650, width=90, height=25)
        
        # ガイド
        self.label_guideVar = tk.StringVar()
        self.label_guide = ttk.Label(self.root, textvariable=self.label_guideVar)
        self.label_guide.place(x=0, y=675, width=600, height=25)

        # アクティビティ
        self.activity = scrolledtext.ScrolledText(self.root)
        self.activity.place(x=600, y=0, width=400, height=675)
        
        # プログレスバー
        self.progbarVal = tk.IntVar(value=0)
        self.progBar = ttk.Progressbar(self.root, orient='horizontal', variable=self.progbarVal, length=300, mode='determinate')
        self.progBar.place(x=600, y=675, width=400, height=25)

    def txtFile_clicked(self):
        path = filedialog.askopenfilename(filetypes=[('文章ファイル','*.txt')])
        self.entry_txtFile.delete(0, tk.END)
        self.entry_txtFile.insert(tk.END, path)

    def valFile_clicked(self):
        path = filedialog.askopenfilename(filetypes=[('変数ファイル','*.xlsx; *.xls')])
        self.entry_valFile.delete(0, tk.END)
        self.entry_valFile.insert(tk.END, path)

    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    myTemplate1().main()