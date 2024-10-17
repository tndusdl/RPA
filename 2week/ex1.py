import pandas as pd

# 초기 데이터 생성
col_names = ['과목번호', '과목명', '강의실', '시간수']
list1 = [
    ['C1','인공지능개론', 'R1', 3],
    ['C2', '웃음치료', 'R2', 2],
    ['C3', '경영학', 'R3', 3],
    ['C4', '3D디자인', 'R4', 4],
    ['C5', '스포츠경영', 'R2', 2],
    ['C6', '예술의 세계', 'R3', 1]
]

df = pd.DataFrame(list1, columns=col_names)
print(df, end='\n\n')

# 데이터 딕셔너리로 다시 생성
data = {
    '과목번호' : ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명' : ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의 세계'],
    '강의실' : ['R1', 'R2', 'R3', 'R4', 'R4', 'R2'],  # 수정: 6개의 값으로 조정
    '시간수' : [3, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df, end='\n\n')

# 과목명 시리즈 출력
sr_name = df['과목명']
print(sr_name, end='\n\n')

# 세 번째 행 전체 출력
sr_no = df.loc[2]
print(sr_no, end='\n\n')

# 세 번째 행의 과목명 출력
cell_name = df.loc[2]['과목명']
print(cell_name, end='\n\n')

# CSV 파일로 저장
df.to_csv('file.csv', index=False)

print("###################################################")

# 교수 정보 추가
df['담당교수'] = ['홍길동', '김철수', '이영희', '박영수', '최영희', '김영수']
print(df, end='\n\n')

# 새 행 추가
df.loc[6] = ['C7', '통계학', 'R7', 3, '이철수'] 
print(df, end='\n\n')

# '강의실' 열 삭제
df1 = df.drop(['강의실'], axis=1)
print(df1, end='\n\n')

# 6번째(인덱스 5) 행 삭제
df2 = df.drop([5], axis=0)
print(df2, end='\n\n')

print("###################################################")

#범위 찾기
#행 찾기
print(df.loc[0:2], end='\n\n')
print(df.iloc[0:2], end='\n\n')
#열 찾기
print(df[['과목명', '담당교수']], end='\n\n')
print(df.loc[:'강의실': '담당교수'], end='\n\n')
