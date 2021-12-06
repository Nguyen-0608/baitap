# Nhập số lượng SV
n=int(input("Nhập vào số lượng sinh viên:"))
#Danh sách các môn học
dscacmon=[" TTHCM"," GTN"," VHH"," QHQT"," TDLT"," TCC"," LLNN"," KTVM"," TA"," ĐRL"]
sotinchi=[   2,      2,      2,     2,      3,      3,     3,      3,       5,   0]

#Tổng điểm các môn
def tongdiem(ds,tinchi):
    d1 = ds[0] * tinchi[0]
    d2 = ds[1] * tinchi[1]
    d3 = ds[2] * tinchi[2]
    d4 = ds[3] * tinchi[3]
    d5 = ds[4] * tinchi[4]
    d6 = ds[5] * tinchi[5]
    d7 = ds[6] * tinchi[6]
    d8 = ds[7] * tinchi[7]
    d9 = ds[8] * tinchi[8]
    d10 = ds[9]* tinchi[9]
    tong=d1+d2+d3+d4+d5+d6+d7+d8+d9+(d10*0.2)
    return(tong)

#Điểm trung bình
def trungbinh(tong,sotinchi):
     tc=0
     for i in range(len(sotinchi)):
         tc+=sotinchi[i]
     dtb=tong/tc
     return dtb

#Hàm nhập điểm cho các bạn sv
def nhapdiem(dsmon):
    ds=[]
    for i in range(1, n + 1):
       print("Nhập điểm của bạn thứ", i)
       for i in range(len(dsmon)):
          print("Nhập môn" + dsmon[i])
          diem=float(input())
          ds.append(diem)
    return(ds)
ds = nhapdiem(dscacmon)
#Output
diem=tongdiem(ds,sotinchi)
tb=trungbinh(diem,sotinchi)
print("Điểm trung bình mỗi bạn là",tb)


