import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox




def complete():
    tkinter.messagebox.showinfo("성공", "해당 경로의 모든 파일명이 변경되었습니다.")

def do_change(prefix, suffix, path):
    file_path = path
    file_names = os.listdir(file_path)

    index = 1

    for name in file_names:
        former = os.path.join(file_path, name)
        new = prefix + str(index) + '.' + suffix
        new = os.path.join(file_path, new)
        os.rename(former, new)
        index = index + 1

    complete()



def main():
    win = Tk()

    win.geometry("1000x500")
    win.title("File name changer")
    win.option_add("*Font", "맑은고딕 15")

    label1 = Label(win,
                   text="설정하려는 파일명과 확장자를 입력하세요 \n\n 예) 파일명 : image, 확장자 : jpg 로 설정할 경우 \n   => image1.jpg, image2.jpg, ...  으로 변경됨",
                   padx=20, pady=10)
    label1.pack(padx=20, pady=20)

    label2 = Label(win, text="파일명")
    label2.pack(padx=20, pady=2)
    ent1 = Entry(win, width=400)
    ent1.pack(padx=20, pady=10)

    label3 = Label(win, text="확장자 (예 : jpg, txt, docx, pptx) ")
    label3.pack(padx=20, pady=2)
    ent2 = Entry(win, width=400)
    ent2.pack(padx=20, pady=10)

    text = Text(win, width=800)

    def warning():
        tkinter.messagebox.showerror("오류", "파일 경로를 선택하지 않았거나, 변경하려는 파일명이 기존의 파일명과 동일합니다.")

    def ask():
        global path
        win.dirName = filedialog.askdirectory()
        path = win.dirName

    def get_parameter():
        prefix = ent1.get()
        suffix = ent2.get()

        try:
            do_change(prefix, suffix, path)
        except Exception as e:
            print(e)
            warning()

    btn = Button(win, text="폴더 경로 선택", command=ask, height=2, width=15, bg="gray")
    btn.pack()

    btn = Button(win, text="파일명 변경하기", height=2, width=15, bg="red", fg='white')
    btn.config(command=get_parameter)
    btn.pack()

    win.mainloop()


    """
    -----------------
    """





if __name__ == '__main__':
    main()