temp_string= '1;2,3:456/789'


#split()--> 하나의 구분자만 구별 가능
print(temp_string.split(';,'))
print(temp_string.split(','))

city= '대구광역시 북구 산격3동(123456789)'
print(city.split('('))

