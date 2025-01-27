import subprocess

# 'pip freeze' 명령어를 실행하여 설치된 패키지 목록을 가져옵니다.
# subprocess.check_output은 명령어의 실행 결과를 바이트 문자열로 반환합니다.
# 이를 디코딩하여 일반 문자열로 변환합니다.
installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8')

# 'requirements.txt' 파일을 쓰기 모드로 열고, 패키지 목록을 저장합니다.
with open('requirements.txt', 'w') as f:
    f.write(installed_packages)

print("requirements.txt 파일이 성공적으로 생성되었습니다.")
