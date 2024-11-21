import qrcode 

name = input("이름을 입력하세요: ")
stdtnum = input("학번을 입력하세요: ")
major = input("전공을 입력하세요: ")

qr_data = [name, stdtnum, major]
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)