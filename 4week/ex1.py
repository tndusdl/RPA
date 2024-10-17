import pandas as pd

data = {'이름': ['Kim', 'Park', 'Lee', 'Ho'],
        '국어': [90, 58, 88, 100],
        '영어': [100, 60, 80, 70],
        '수학': [55, 65, 76, 88]}

# 1. data를 데이터 프레임으로 만들기
df = pd.DataFrame(data)

# 2. 1에서 만든 데이터 프레임을 출력하기
print(df, end="\n\n")

# 3. 학생 아름만 추출해서 출력하기.(열 추출)
sr_name = df['이름']
print(sr_name, end="\n\n")

# 4. 'Park" 성적만 출력하기
park_data = df.loc[df['이름'] == 'Park']
print(park_data, end="\n\n")

# 5. 'Ho'학생의 수학 점수를 90점으로 수정하기
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end="\n\n")

# 6. 'Oh' 학생의 국어(100), 영어(70), 수학(80) 성적을 새로 추가하기
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end="\n\n")

# 7. 'Lee' 학생의 성적을 삭제하기 
df = df.drop([2], axis=0)
print(df, end="\n\n")


print("1>-------------------------")
print("국어 평균 : ", df['국어'].mean(), end="\n\n")
print("국어 중간 : ", df['국어'].median(), end="\n\n")
print("국어 최소 : ", df['국어'].min(), end="\n\n")
print("국어 최대 : ", df['국어'].max(), end="\n\n")

print("2>-------------------------")
print("Kim 총점 : ", df.iloc[0, 1:4].sum(), end="\n\n")
print("Kim 평균 : ", df.iloc[0, 1:4].mean(), end="\n\n")

print("3>-------------------------")
print("수학 4분위 \n : ", df['수학'].quantile([0.25,0.5,0.75]), end="\n\n")
print("수학 분산 : ", df['수학'].var(), end="\n\n")
print("수학 표준편차 : ", df['수학'].std(), end="\n\n")
