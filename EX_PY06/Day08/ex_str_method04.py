# 문자열에서 원소/요소 변경해주는 메서드: replace()
msg='python'
# str ->인덱싱 미지원(불변의 시퀀스 타입)
# ->전용 메서드로 변경 가능
m1= msg.replace('y', 'i')
  #결과를 저장해야 변경 적용 가능!!
print(f'msg = {msg},\nm1= {m1}')

msg="Good Happy"
# o를 대문자로 변경
print(msg.replace('o', 'O')) #기본->모든 원소에 적용

# o를 1개만 대문자로 변경
print(msg.replace('o', 'O',1)) #1개 원소에 적용(정방향)

