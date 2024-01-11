str='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''

def khoangcach(str) :
    str=str.split("-")
    while '' in str: 
        str.remove("")
    return " ".join(str)

def xuongdong(str):
    str=str.split("\n")
    for i in str:
        print(khoangcach(i))
xuongdong(str)