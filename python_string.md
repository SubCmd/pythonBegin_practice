# 자료형(2)

> 1. 문자열 자료형

## - 문자열(string)

문자, 단어 등으로 구성된 문자들의 집합

"Life is too short, You need Python." etc

문자열은 ""에 둘러싸여 있다.

### - 문자열을 만드는 방법

1. 큰따옴표("")로 양쪽 둘러싸기
    "Hello"

2. 작은따옴표('')로 양쪽 둘러싸기
    'Hello'

3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
    """Life is too short, You need python."""

4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
    '''Life is too short, You need python.'''

***

= 문자열에 작은따옴표(')를 포함시키고 싶은 경우,

1. 문자열에 작은따옴표(') 포함시키기
    Python's favorite food is perl
    -> food = "Python's favorite food is perl."

    SyntaxError : invalid syntax

    -> 만약 food = 'Python's favorite food is perl.'로 작성시, 구문오류(syntax error)가 발생한다.

2. 문자열에 큰따옴표(") 포함시키기
    "Python is very easy." he says
    -> say = '"Python is very easy." he says'

3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
    -> food = 'Python\'s favorite food is perl.'
    -> say = "\"Python is very easy.\" he says."

    : 백슬래시(\) 직후에 작은따옴표나 큰따옴표를 사용하면 된다.

***

= 여러 줄인 문자열을 변수에 대입하고 싶을 경우,

    Life is too short
    You need python

1. 줄을 바꾸는 이스케이프 코드 '\n' 삽입하기
    -> multiline = "Life is too short\nYou need python"

2. 연속된 작은따옴표 3개(''') 또는 큰따옴표(""") 사용하기
    -> multiline = """
    ... Life is too short
    ... You need python
    ..."""

    -> multiline = '''
    ... Life is too short
    ... You need python
    ...'''

***

= 이스케이프 코드 예시

| 코드 | 설명 |
|---|:---:|
'\n'|문자열 안에서 줄을 바꿀 때 사용|
'\t'|문자열 사이에 탭 간격을 줄 때 사용|
'\\'|문자 \를 그대로 표현할 때 사용|
'\''|작은따옴표를 그대로 표현할 때 사용|
'\"'|큰따옴표를 그대로 표현할 때 사용|
'\r'|캐리지 리턴(줄바꿈 문자, 현재 커서를 가장 앞으로 이동)|
'\f'|폼 피드(줄바꿈 문자, 현재 커서를 다음 줄로 이동)|
'\a'|벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)|
'\b'|백스페이스|
'\000'|널 문자|

***

= 문자열 연산하기
: 문자열을 더하거나 곱할 수 있다. (파이썬만의 특징)

1. 문자열 더해서 연결하기(Concatenation)
    -> head = "Python"
    -> tail = "is fun!"
    -> head + tail
    'Python is fun!'

2. 문자열 곱하기
    -> a = "python"
    -> a * 2
    'pythonpython

3. 문자열 곱하기 응용
    -> print("=" * 50)
    -> print("My Program")
    -> print("=" * 50)

    #the result of 'multistring.py'
    ==================================================
    My Program
    ==================================================

4. 문자열 길이 구하기
    len 함수
    -> a = "Life is too short"
    -> len(a)
    17

***

= 문자열 인덱싱과 슬라이싱
- 인덱싱(indexing) : 가리킨다.
- 슬라이싱(slicing) : 잘라낸다.

Q : 문자열 인덱싱이란?
-> a = "Life is too short. You need Python"
        0         1         2         3
        0123456789012345678901234567890123

    -> a = "Life is too short. You need Python"
    -> a[3]
    'e'

### "파이썬은 0부터 센다"


    a[0] : 'L'
    a[1] : 'i'

- 문자열 인덱싱 활용하기
    -> a = "Life is too short. You need Python"
    -> a[0]
    'L'
    a[12]
    's'
    a[-1]   # 마지막 문자 'n'
    'n'
    : 마이너스는 문장의 뒤에서 시작해 앞으로 나아간다. 
      즉, 마이너스는 '뒤에서 몇번째'가 된다.

Q : 문자열 슬라이싱이란?
-> 문자열에서 단순히 한 문자만 추출한다.
    -> a = "Life is too short. You need Python"
    -> b = a[0] + a[1] + a[2] + a[3]
    -> b
    'Life'

    -> a[0:4]
    'Life

    -> a[0:3]   # 즉, 0 <= a < 3 이라는 등호가 성립한다.
    'Lif'

    [시작 번호:끝 번호]

- 문자열을 슬라이싱하는 방법
    -> a[0:5]
    'Life'

    -> a[12:17]
    'short'

    -> a[19:]
    'You need Python'

    -> a[:17]
    'Life is too short'

    -> a[:]
    'Life is too short. You need Python'

    -> a[19:-7]
    'You need'

- 슬라이싱으로 문자열 나누기
    -> a = '2001033Rainy"
    -> date = a[:8]
    -> weather = a[8:]
    -> date
    '2001033'
    -> weather
    'Rainy'

    -> year = a[:4]
    -> day = a[4:8]
    -> weather = [8:]
    -> year
    '2001'
    -> day
    '1033'
    -> weather
    'Rainy'

### 파이썬은 immutable한 자료이다. 
    즉, 문자열 자료형은 그 요솟값을 변경할 수 없다.

Q : Pithon이라는 문자를 Python이라는 문자로 변경하고 싶으면?
    -> a = "Pithon"
    -> a[1]
    'i'
    -> a[1] = 'y'
     
    Type Error가 발생한다! -> 문자열 자료형의 요솟값은 변경할 수 없기 때문이다!

    그렇기에
    -> a = "Pithon"
    -> a[:1]
    'P'
    -> a[2:]
    'thon'
    -> a[:1] + 'y' + a[2:]
    'Python'