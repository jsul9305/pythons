import urllib.request
import json

def get_country_code(ip):
    # ip 정보 조회 API 호출
    url = f"https://apis.data.go.kr/B551505/whois/ipas_country_code?serviceKey=SWwAuuSGB0LldPNTE4TGN5jovAA9%2BtTAxHf9XPUE5X4%2BdaUCT6oky%2FMRvZdeeTyY9BDYDZErBnoPeUD7I3nLiQ%3D%3D&query={ip}&answer=json"
    try:
        with urllib.request.urlopen(url) as response:
            # 응답을 JSON으로 읽기
            data = json.load(response)
            # countryCode 추출
            return data.get("response", {}).get("whois", {}).get("countryCode", "Unknown")
    except urllib.error.URLError:
        return "Error"  # 네트워크 오류 등의 경우 "Error" 반환
    
def add_country_code_to_ips(input_file, output_file):
    with open(input_file, 'r') as f:
        ips = f.readlines() # ip 목록읽기
    
    with open(output_file, 'w') as f:
        for ip in ips:
            ip = ip.strip()  # IP에서 불필요한 공백 제거
            country_code = get_country_code(ip)  # API 호출하여 국가 코드 얻기
            f.write(f"{ip} - {country_code}\n")  # 결과를 IP 옆에 기록
            print(f"{ip} - {country_code}")  # 진행 상황 출력

# 입력 파일과 출력 파일 결정
input_file = "ips.txt"
output_file = "ipscountries.txt"

# 함수 호출
add_country_code_to_ips(input_file, output_file)