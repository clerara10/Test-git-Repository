import tkinter as tk
from tkinter import messagebox
import threading
import time
import webbrowser
import os
import platform
import subprocess

class DeepFaceUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepFace 감정 분석 UI")
        self.root.geometry("400x300")
        self.running = False
        self.class_name = None

        # 학번 입력 UI
        self.id_label = tk.Label(root, text="학번을 입력하세요:")
        self.id_label.pack(pady=10)

        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.check_button = tk.Button(root, text="확인", command=self.verify_student)
        self.check_button.pack(pady=10)

        self.attend_button = tk.Button(root, text="수업 듣기", command=self.select_class, font=("Arial", 12))
        self.focus_button = tk.Button(root, text="집중도 분석 확인", command=self.show_focus_result, font=("Arial", 12))

    def verify_student(self):
        self.student_id = self.id_entry.get().strip()
        if not self.student_id:
            messagebox.showwarning("입력 오류", "학번을 입력하세요.")
            return

        result = self.compare_face(self.student_id)
        if result:
            messagebox.showinfo("인식 성공", f"{self.student_id} 학생 확인 완료")
            self.show_action_buttons()
        else:
            messagebox.showerror("인식 실패", "학생 사진과 일치하지 않습니다.")

    def compare_face(self, student_id):
        print(f"학번 {student_id}에 대해 얼굴 비교 중...")
        time.sleep(1)
        return True

    def show_action_buttons(self):
        self.id_label.pack_forget()
        self.id_entry.pack_forget()
        self.check_button.pack_forget()
        self.attend_button.pack(pady=20)
        self.focus_button.pack(pady=10)

    def select_class(self):
        popup = tk.Toplevel(self.root)
        popup.title("수업 선택")
        popup.geometry("300x150")
        tk.Label(popup, text="수업을 선택하세요:", font=("Arial", 12)).pack(pady=10)

        tk.Button(popup, text="1강", command=lambda: self.start_class("1강", popup)).pack(pady=5)
        tk.Button(popup, text="2강", command=lambda: self.start_class("2강", popup)).pack(pady=5)
        tk.Button(popup, text="3강", command=lambda: self.start_class("3강", popup)).pack(pady=5)

    def start_class(self, class_name, popup):
        self.class_name = class_name
        popup.destroy()

        # 각 강의에 해당하는 유튜브 링크
        youtube_links = {
            "1강": "https://www.youtube.com/watch?v=jPs3n9Vou9c",
            "2강": "https://www.youtube.com/watch?v=jPs3n9Vou9c",
            "3강": "https://www.youtube.com/watch?v=jPs3n9Vou9c"
        }

        url = youtube_links.get(class_name)
        if url:
            webbrowser.open(url)
        else:
            messagebox.showerror("오류", "링크가 없습니다.")

        self.start_deepface()

    def start_deepface(self):
        if self.running:
            return
        self.running = True
        threading.Thread(target=self.run_deepface_logic, daemon=True).start()

        self.root.withdraw()
        self.show_stop_button()

    def run_deepface_logic(self):
        print(f"{self.class_name} 감정 분석 시작")
        while self.running:
            print(f"{self.class_name} 감정 분석 중...")
            time.sleep(5)
        print(f"{self.class_name} 감정 분석 종료")

    def stop_deepface(self):
        self.running = False
        self.stop_window.destroy()
        self.root.deiconify()

    def show_stop_button(self):
        self.stop_window = tk.Toplevel()
        self.stop_window.overrideredirect(True)
        self.stop_window.attributes("-topmost", True)

        screen_width = self.stop_window.winfo_screenwidth()
        self.stop_window.geometry(f"40x30+{screen_width - 50}+10")

        stop_button = tk.Button(self.stop_window, text="⏸", command=self.stop_deepface, width=3)
        stop_button.pack()

    def show_focus_result(self):
        csv_path = "emotion_summary.csv"  # 저장한 감정 분석 CSV 파일 경로

        if not os.path.isfile(csv_path):
            messagebox.showerror("파일 없음", f"{csv_path} 파일이 존재하지 않습니다.")
            return

        try:
            if platform.system() == "Windows":
                os.startfile(csv_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.call(["open", csv_path])
            else:  # Linux
                subprocess.call(["xdg-open", csv_path])
        except Exception as e:
            messagebox.showerror("실패", f"CSV 파일을 열 수 없습니다:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeepFaceUI(root)
    root.mainloop()
