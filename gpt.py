import cv2

# 사진 로드
photo = cv2.imread('image.jpg')

# 그레이 스케일 변환
gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

# 가우시안 블러 필터 적용
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Canny 에지 검출 알고리즘 적용
edges = cv2.Canny(gray, 100, 200)

# 경계를 통해 채색된 결과 이미지 생성
cartoon = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
cartoon = cv2.bitwise_and(cartoon, cartoon, mask=edges)

# 결과 이미지 저장
cv2.imwrite('cartoon.jpg', cartoon)
