def makeXL(filename):
    from faker import Faker
    from openpyxl import Workbook
    
    fake = Faker('ko_KR')
    wb = Workbook()
    ws =wb.active
    ws.append(['이름', '성별', '이메일', '전화번호', '주소'])
    
    for i in range(1000):
        name = fake.name()
        gender = fake.random_element(elements=('남', '여'))
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()
        ws.append([name. gender, email, phone_number, address])
        
        print(filename)
        wb.save(filename)
        
        @app.post("/getexcelfile/")
        async def make_excel_file():
            filename = "sample.xlsx"
            save_file = "static/files/" + filename
            import os
            if os.path.exists(save_file):
                os.remove(save_file)
                
                makeXL(save_file)
                return {"filename": save_file}
                
        
                        
