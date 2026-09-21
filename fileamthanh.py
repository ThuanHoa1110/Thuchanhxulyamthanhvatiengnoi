from gtts import gTTS

print("===================================")
print("     CHUYỂN VĂN BẢN THÀNH ÂM THANH")
print("===================================")

text = input("Nhập văn bản: ")

if text.strip() == "":
    print("Bạn chưa nhập văn bản!")
else:
    tts = gTTS(
        text=text,
        lang="vi",
        slow=False
    )

    tts.save("output.mp3")

    print("\nĐã tạo âm thanh thành công!")
    print("File được lưu tại: output.mp3")