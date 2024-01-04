import cv2

"""
    到 https://github.com/opencv/opencv/tree/master/data/haarcascades
    下載 haarcascade_frontalface_default.xml
"""

# 載入分類器
Face_Cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 讀取圖片
Img = cv2.imread('tw.jpg')

# 將 圖片 轉成 灰階圖片(加快檢測速度)
Gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)

# 偵測臉部
Faces = Face_Cascade.detectMultiScale(
        Gray,
        scaleFactor = 1.08, # 每次搜尋方塊漸少的比例
        minNeighbors = 20,   # 每個目標至少檢測 10次以上
        minSize = (30, 30)) # 設定數據搜尋的最小尺寸

# 繪製人臉的方框
# (0, 255, 0) 欄位可以變更方框顏色 (Blue, Green, Red)
for (x, y, w, h) in Faces:
    cv2.rectangle(Img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
# 顯示成果
cv2.namedWindow('Img', cv2.WINDOW_NORMAL)  # 正常視窗大小
cv2.imshow('Img', Img)                     # 顯示圖片
cv2.imwrite("tw_AI.jpg", Img )            # 保存圖片
cv2.waitKey(0)                             # 等待按下任一按鍵
cv2.destroyAllWindows()                    # 關閉視窗