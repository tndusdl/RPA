import pandas as pd

data = {'이름': ['Kim', 'Park', 'Lee', 'Ho'],
        '국어': [90, 58, 88, 100],
        '영어': [100, 60, 80, 70],
        '수학': [55, 65, 76, 88]}

# 1. data를 데이터 프레임으로 만드시오
df = pd.DataFrame(data)

# 2. 1에서 만든 데이터 프레임을 출력하시오.
print(df, end="\n\n")

# 3. 학생 아름만 추출해서 출력하시오.(열 추출)
sr_name = df['이름']
print(sr_name, end="\n\n")

# 4. 'Park" 성적만 출력하시오.
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end="\n\n")

# 5. 'Ho'학생의 수학 점수를 90점으로 수정하시오.
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end="\n\n")

# 6. 'Oh' 학생의 국어(100), 영어(70), 수학(80) 성적을 새로 추가하시오.
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end="\n\n")

# 7. 'Lee' 학생의 성적을 삭제하시오.
df = df.drop([2], axis=0)
print(df, end="\n\n")
