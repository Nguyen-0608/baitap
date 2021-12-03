# Nhập số lượng SV
n=int(input("Nhập vào số lượng sinh viên:"))

#Danh sách các môn học
dsmon=["TTHCM","GTN","VHH","QHQT","TDLT","TCC","LLNN","KTVM","TA","ĐRL"]
sotinchi=[  "2",   "2",  "2",  "2",    "3",   "3",  "3",  "3",   "5", "0"]

#Hàm nhập điểm cho các bạn sv
ds=[]
for i in range(1, n + 1):
    print("Nhập điểm của bạn thứ", i)
    for i in range(len(dsmon)):
      print("Nhập môn" +dsmon[i])
      diem=float(input())
      ds.append(diem)
      tong = ((ds[0] + ds[1] + ds[2] + ds[3]) * 2) + ((ds[4] + ds[5] + ds[6] + ds[7]) * 3) + ds[8] * 5 + ds[9] * 0.2
      dtb= tong/25
      print(dtb)




#Điểm trung bình


