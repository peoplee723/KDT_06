#문자열 원소/요소 변경 체크

#1. 원소/요소 값 변경
msg='python'
#    012345
#msg[1]='y' 
# TypeError: 'str' object does not support item assignment
# -->미지원

#2. 원소/요소 삭제--->명령어 del,del()
# del msg[1]
#TypeError: 'str' object doesn't support item deletion
#->미지원

#명령어 del,del()
"""
del msg
print(msg)
"""
#NameError: name 'msg' is not defined -->변수 삭제됨

