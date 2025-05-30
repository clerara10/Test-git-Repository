import tkinter as tk
from tkinter import messagebox
import threading
import time

class DeepFaceUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepFace 감정 분석 UI")
        self.root.geometry("400x300")
        self.running = False

        # 학번 입력 UI
        self.id_label = tk.Label(root, text="학번을 입력하세요:")
        self.id_label.pack(pady=10)

        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.check_button = tk.Button(root, text="확인", command=self.verify_student)
        self.check_button.pack(pady=10)

        # 수업 듣기 / 집중도 분석 버튼 (초기에는 숨김)
        self.attend_button = tk.Button(root, text="수업 듣기", command=self.start_deepface, font=("Arial", 12))
        self.focus_button = tk.Button(root, text="집중도 분석 확인", command=self.show_focus_result, font=("Arial", 12))

    def verify_student(self):
        student_id = self.id_entry.get().strip()
        if not student_id:
            messagebox.showwarning("입력 오류", "학번을 입력하세요.")
            return

        result = self.compare_face(student_id)
        if result:
            messagebox.showinfo("인식 성공", f"{student_id} 학생 확인 완료")
            self.show_action_buttons()
        else:
            messagebox.showerror("인식 실패", "학생 사진과 일치하지 않습니다.")

    def compare_face(self, student_id):
        # 실제 DeepFace 비교 기능 대체 예정
        print(f"학번 {student_id}에 대해 얼굴 비교 중...")
        time.sleep(1)
        return True

    def show_action_buttons(self):
        self.id_label.pack_forget()
        self.id_entry.pack_forget()
        self.check_button.pack_forget()
        self.attend_button.pack(pady=20)
        self.focus_button.pack(pady=10)

    def start_deepface(self):
        if self.running:
            return
        self.running = True
        threading.Thread(target=self.run_deepface_logic, daemon=True).start()

        # 👉 기존 창 숨기고 멈춤 버튼만 띄움
        self.root.withdraw()
        self.show_stop_button()

    def run_deepface_logic(self):
        print("DeepFace 감정 분석 시작")
        while self.running:
            print("감정 분석 중...")
            time.sleep(1)
        print("DeepFace 감정 분석 종료")

    def stop_deepface(self):
        self.running = False
        self.stop_window.destroy()
        self.root.deiconify()  # 기존 창 다시 보이기 (원하면)

    def show_stop_button(self):
        self.stop_window = tk.Toplevel()
        self.stop_window.overrideredirect(True)
        self.stop_window.attributes("-topmost", True)

        screen_width = self.stop_window.winfo_screenwidth()
        self.stop_window.geometry(f"40x30+{screen_width - 50}+10")

        stop_button = tk.Button(self.stop_window, text="⏸", command=self.stop_deepface, width=3)
        stop_button.pack()

    def show_focus_result(self):
        messagebox.showinfo("집중도 분석", "집중도 분석 결과는 85%입니다.")  # 예시

if __name__ == "__main__":
    root = tk.Tk()
    app = DeepFaceUI(root)
    root.mainloop()