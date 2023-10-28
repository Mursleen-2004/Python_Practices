# zip(): ye aik built-in function hai..iska kaam 1 sy zyda lists ko iterate/repeat krna  hai.

a = [10,20,30,40,50];
b = [5,15,25,35,45,55,66];
                                 #agar aik list mein dosri sy zyda elements hain..to zip osy ignore kr dega.
for c,d in zip(a,b):
 print(c,d)