# 주어진 데이터를 바탕으로 계산을 진행합니다.

# 기존 대회 데이터
prev_distance = 47.25  # km
prev_flat_distance = 3  # km (평지 구간)
prev_elevation_gain = 3155  # m
prev_total_time = 8*3600 + 31*60 + 26  # 초 (8시간 31분 26초)
prev_flat_time = 18*60 + 95  # 초 (18분 95초)

# 새로운 대회 데이터
new_distance = 107  # km
new_flat_distance = 2  # km (평지 구간)
new_elevation_gain = 4252  # m

# 1. 평지 구간의 페이스 계산 (기존 대회)
prev_flat_pace = prev_flat_time / prev_flat_distance  # 초/km

# 2. 고도 구간 시간 계산 및 고도 구간 페이스 계산
prev_elevation_time = prev_total_time - prev_flat_time  # 고도 구간에서 사용된 시간
prev_elevation_distance = prev_distance - prev_flat_distance  # 고도 구간 거리
prev_elevation_pace = prev_elevation_time / prev_elevation_distance  # 고도 구간 페이스 (초/km)
print("prev_elevation_pace", prev_elevation_pace)

# 3. 고도 증가에 따른 시간 보정 (100m당 시간)
prev_elevation_time_per_100m = prev_elevation_time / (prev_elevation_gain / 100)  # 고도 100m당 시간

# 4. 새로운 대회의 예상 시간 계산
# 평지 구간 예상 시간
new_flat_time = new_flat_distance * prev_flat_pace  # 초

# 고도 구간 예상 시간
new_elevation_distance = new_distance - new_flat_distance  # 고도 구간 거리
new_elevation_time = (new_elevation_distance * prev_elevation_pace) # 초
print("new_elevation_time", new_elevation_time)

# 최종 예상 시간
new_total_time = new_flat_time + new_elevation_time  # 초

# 시간을 시, 분, 초로 변환
new_hours = int(new_total_time // 3600)
new_minutes = int((new_total_time % 3600) // 60)
new_seconds = int(new_total_time % 60)

print(new_hours, ":", new_minutes, ":", new_seconds)