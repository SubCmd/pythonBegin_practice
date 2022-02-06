# 자료형(3)

## - 문자열 포매팅(Formatting)

    : 문자열 안에 있는 특정한 값을 변경해야 하는 경우, 이것을 가능하게 해주는 것.

    - 포매팅 하는 방법들

    1. 숫자 바로 대입하기
    -> "I eat %d apples."% 3
    'I eat 3 apples'

    : 여기 있는 %d를 포맷 코드라 칭한다.

    2. 문자열 바로 대입
    -> "I eat %s apples." % "five"
    'I eat five apples.'

    여기서 숫자를 넣을 때는 %d를 사용하고 문자열을 넣기 위해서는 %s를 사용해야 한다.

    3. 숫자 값을 나타내는 변수로 대입하기
    -> number = 3
    -> "I eat %d apples." % number
    'I eat 3 apples.'

    4. 두 개 이상의 값 넣기
    -> number = 10
    -> day = "three"
    -> "I ate %d apples. so I was sick for %s days." % (number, day)
    'I ate 10 apples. so I was sick for three days.'

---
|코드|설명|
|---|:---:|
|%s|문자열(String)|
|%c|문자 1개(Character)|
|%d|정수(Integer)|
|%f|부동 소수(Floating-point)|
|%o|8진수|
|%x|16진수|
|%%|Literal%(문자'%'자체)|
|---|:---:|

예시)
-> "I have %s apples." % 3
'I have 3 apples.
-> "rate is %s" % 3.234
'rate is 3.234

---

### 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.

    -> "Error is %d%." % 98

    Traceback (most recent call last):
        File "<stdin>", line 1 in <module>
    Value Error : incomplete format

    -> "Error is %d%%." % 98
    'Error is 98%'


- 포맷 코드와 숫자 함께 사용하기

1. 정렬과 공백
    -> "%10s" % "hi"
    '            hi'
        : hi가 오른쪽 정렬된다. 
        : 전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 나머지는 공백을 남긴다.

    -> "%-10jane" % 'hi'
    'hi          jane'
        : 전체 길이가 10인 문자열 공간에 hi를 대입하여 왼쪽 정렬하고, 그 이후 자리에 jane이라는 문자열을 추가한다.

2.  소수점 표현하기
    -> "%0.4f" % 3.42134234
    '3.4213'
        : 여기서는 소수점 네 번째 자리를 의미하는 자료이다.
    
    -> "10.4f" % 3.42134234
    '    3.4213'
        : 전체 길이가 10인 문자열 공간에 3.4213을 대입하여 오른쪽 정렬한다.


- format 함수를 사용한 포매팅

    - 숫자 바로 대입하기
        -> "I eat {0} apples.".format(3)
        'I eat 3 apples.'
    
    - 문자열 바로 대입하기
        -> 'I eat {0} apples.".format("five")
        'I eat five apples.'
    
    - 숫자 값을 가진 변수로 대입하기
        -> number = 3
        -> 'I eat {0} apples.'.format(number)
        'I eat 3 apples.'
    
    - 2개 이상의 값 넣기
        -> number = 10
        -> day = "three"
        -> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
        'I ate 10 apples. so I was sick for three days.'
    
        => 위와 같이 보이는 {0}, {1} 등의 인덱스 대신 {name} 형태를 사용해도 된다.
    
    - 인덱스와 이름을 혼용해서 넣기
        -> "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
        'I ate 10 apples. so I was sick for 3 days.'
                : name=value와 혼용해서 사용 가능하다.

    - 왼쪽 정렬 (:<)
        -> "{0:<10}".format("hi")
        'hi        '
    
    - 오른쪽 정렬 (:>)
        -> "{0:>10}".format("hi")
        '         hi'
    
    - 가운데 정렬
        -> "{0:^10}".format("hi")
        '    hi    '

    - 공백 채우기
        -> "{0:=^10}".format("hi")
        '====hi===='
        -> "{0:!<10}".format("hi")
        'hi!!!!!!!!'
    
    - 소수점 표현하기
        -> y = 3.42134234
        -> "{0:0.4f}".format(y)
        '3.4213'

        -> "{0:10.4f"}.format(y)
        '    3.4213'
    
    - {또는} 문자 표현하기
        -> :{{ and }}".format()
        '{ and }'
            : 2개를 연속해서 사용하면 중괄호(brace)를 표현할 수 있다.

- f 문자열 포매팅
    : 파이썬 3.6버전부터 사용가능한 기능
    : f 접두사를 사용하면 f 문자열 포매팅이 가능하다.

    -> name = '홍길동'
    -> age = 30
    -> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
    '나의 이름은 홍길동입니다. 나이는 30입니다.'

    -> age = 30
    -> f'나는 내년이면 {age+1}살이 된다.'
    '나는 내년이면 31살이 된다.'

    - 딕셔너리의 경우,
        -> d = {'name':'홍길동', 'age':30}
        -> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
        '나의 이름은 홍길동입니다. 나이는 30입니다.'
    
    - 정렬의 경우,
        -> f'{"hi":<10}' : 왼쪽 정렬
        'hi        '
        -> f'{"hi":>10}' : 오른쪽 정렬
        '        hi'
        -> f'{"hi":^10}' : 가운데 정렬
        '    hi    '
    
    - 공백 채우기의 경우,
        -> f'{"hi":=^10}' : 가운데 정렬 + =로 공백채우기
        '====hi===='
        -> f'{"hi":!<10}' : 오른쪽 정렬 + !로 공백채우기
        'hi!!!!!!!!'

    - 소수점 표현하기
        -> y = 3.42134234
        -> f'{y:0.4f}' : 소수점 4점자리까지만 표현
        '3.4213'
        -> f'{y:10.4f}' : 소수점 4점자리까지 표현하고 총 자릿수를 10으로 맞춤
        '    3.4213'

    - f문자열에서 {}를 문자로 표현하기
        -> f'{{ and }}'
        '{ and }'













