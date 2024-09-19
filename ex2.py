import pandas as pd

data = {'이름': ['Kim', 'Park', 'Lee', 'Ho'],
        '국어': [90, 58, 88, 100],
        '영어': [100, 60, 80, 70],
        '수학': [55, 65, 76, 88]}

df = pd.DataFrame(data)

# 1. df 전체 출력
print(df, end="\n\n")

# 2. '이름' 열 출력
sr_name = df['이름']
print(sr_name, end="\n\n")

# 3. 'Park'의 데이터를 loc로 가져오기
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end="\n\n")

# 4. 'Ho'의 수학 점수를 90으로 수정
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end="\n\n")

# 5. 3번째 행을 'Oh'으로 교체
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end="\n\n")

# 6. 'Lee' 행 삭제 (2번째 인덱스)
df = df.drop([2], axis=0)
print(df, end="\n\n")
