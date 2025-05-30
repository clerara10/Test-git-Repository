import pandas as pd
import os

def save_emotion_to_sheet(student_id, class_name, minute, emotion, filepath="emotion_summary.csv"):
    column_name = f"{minute}분 감정"

    # 기존 파일 불러오기 또는 새로 생성
    if os.path.isfile(filepath):
        df = pd.read_csv(filepath)
    else:
        df = pd.DataFrame(columns=["학번", "수업명"])

    # 기존 행 존재 여부 확인
    match = (df["학번"] == student_id) & (df["수업명"] == class_name)
    
    if match.any():
        row_idx = df[match].index[0]
        df.loc[row_idx, column_name] = emotion
    else:
        new_row = {"학번": student_id, "수업명": class_name, column_name: emotion}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # 저장
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    print(f"[✔] 감정 저장 완료 → {minute}분: {emotion}")


# ✅ 테스트 데이터
save_emotion_to_sheet(student_id=1, class_name="3강", minute=0, emotion="중립")
save_emotion_to_sheet(student_id=1, class_name="3강", minute=5, emotion="화남")
save_emotion_to_sheet(student_id=1, class_name="3강", minute=15, emotion="행복")

save_emotion_to_sheet(student_id=2, class_name="3강", minute=0, emotion="놀람")
save_emotion_to_sheet(student_id=2, class_name="3강", minute=5, emotion="중립")