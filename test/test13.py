# 효신이는 매년 국회의원 선거 때마다, 성북구에서 집계 도우미 봉사를 하는데요. 작년까지는 표를 손수 세다가, 올해부터는 IT 시대에 더 적합한 솔루션을 개발하려고 합니다.
# 파이썬 리스트 votes에는 성북구민들의 투표 결과가 저장되어 있습니다. 리스트 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하는 것이 목표입니다.


# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자',
         '최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기',
         '강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name in vote_counter:
        vote_counter[name] += 1
    else:
        vote_counter[name] = 1

# 후보별 득표수 출력
print(vote_counter)
