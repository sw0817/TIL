# 정규표현식 part2. 메서드와 컴파일옵션

## 1. methods

| Methods    | 목적                                                         |
| ---------- | ------------------------------------------------------------ |
| match()    | 문자열의 처음부터 정규식과 매치되는지 조사한다.              |
| search()   | 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.         |
| findall()  | 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다. |
| finditer() | 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다. |

#### 01. match()

```python
import re
p = re.compile('[a-z]+')
## 만약 숫자에 관한 매칭 체크를 하고 싶다면, p=re.compile('[0-9]') 이런식으로 해주면 된다.

# ex.1
m = p.match('python')
print(m)
>>> <re.Match object; span=(0, 6), match='python'>

# ex.2
n = p.match("3 python")
print(n)
>>> None - 3으로 시작하기 때문에 match되지 않으므로 None 반환

# ex.3
l = p.match("python 3")
print(l)
>>> <re.Match object; span=(0, 6), match='python'> - 3이 뒤에 있는거는 괜찮음
```

##### match() 의 메소드

| method  | 목적                                                   |
| :------ | :----------------------------------------------------- |
| group() | 매치된 문자열을 돌려준다.                              |
| start() | 매치된 문자열의 시작 위치를 돌려준다.                  |
| end()   | 매치된 문자열의 끝 위치를 돌려준다.                    |
| span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |

```python
m = p.match("python")
m.group()
>>> 'python'
m.start()
>>> 0
m.end()
>>> 6
m.span()
>>> (0, 6)
```



#### 02. search()

```python
# ex.1
m = p.search("python")
print(m)
>>> <re.Match object; span=(0, 6), match='python'>

# ex.2
l = p.search("3 python")
print(l)
>>> <re.Match object; span=(2, 8), match='python'> 
# 문자열 슬라이싱 2:8 영역에 match되는 python이 있다고 알려줌
```



#### 03. findall()

```python
result = p.findall("life is too short 33 AA")
print(result)

>>> ['life', 'is', 'too', 'short']
# compile을 [a-z]로 소문자 영역만 했다. 따라서 대문자인 AA도 누락, integer인 33도 누락된다. 
```



#### 04. finditer()

> finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다. 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

```python
result = p.finditer("life is too short")
print(result)
>>> <callable_iterator object at 0x01F5E390>

for r in result: 
    print(r)
    
>>> <re.Match object; span=(0, 4), match='life'>
>>> <re.Match object; span=(5, 7), match='is'>
>>> <re.Match object; span=(8, 11), match='too'>
>>> <re.Match object; span=(12, 17), match='short'>
```



## 2. 컴파일 옵션

| method         | 목적                                                         |
| :------------- | :----------------------------------------------------------- |
| DOTALL (S)     | `.` 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다. |
| IGNORECASE (I) | 대소문자에 관계없이 매치할 수 있도록 한다.                   |
| MULTILINE (M)  | 여러줄과 매치할 수 있도록 한다. (`^`, `$` 메타문자의 사용과 관계가 있는 옵션이다) |
| VERBOSE (X)    | verbose 모드를 사용할 수 있도록 한다.-  (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.) |



```python
# ex 1 DOTALL
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
>>> None
# '.'은 메타문자 (예: \n, *, + 등)와 매치되지 않기 때문에 math 결과는 None이 된다.

# ex 1 - 메타문자 포함시키는 방법
p = re.compile('a.b', re.DOTALL) || p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)
>>> <_sre.SRE_Match object at 0x01FCF3D8>
# compile을 할 때 re.DOTALL 옵션을 뒤에 작성하면 메타문자도 match에 포함시킨다. re.DOTALL은 re.S로 사용해도 동일하다


# ex 2 IGNORECASE
p = re.compile('[a-z]')
m = p.match('python')
print(m)
>>> None

# ex 2 - 대소문자 구분 상관없이 하는 방법
p = re.compile('[a-z]', re.IGNORECASE) || p = re.compile('[a-z]', re.I)
m = p.match('python')
l = p.match('Python')
n = p.match('PYTHON')
print(m, l, n)
>>> <re.Match object; span=(0, 6), match='python'>
>>> <re.Match object; span=(0, 6), match='Python'>
>>> <re.Match object; span=(0, 6), match='PYTHON'>

# ex 3. MULTILINE
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
>>> ['python one']

# ex 3 여러줄도 포함하는 방법
p = re.compile("^python\s\w+", re.MULTILINE )

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
>>> ['python one', 'python two', 'python three']
```

지금껏 알아본 정규식은 매우 간단하지만 정규식 전문가들이 만든 정규식을 보면 거의 암호수준이다. 

정규식을 이해하려면 하나하나 조심스럽게 뜯어보아야만 한다. 

이렇게 이해하기 어려운 정규식을 주석 또는 줄 단위로 구분할 수 있다면 얼마나 보기 좋고 이해하기 쉬울까? 방법이 있다. 바로 `re.VERBOSE` 또는 `re.X` 옵션을 사용하면 된다.

```python
# ex 4 VERBOSE
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
---
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

첫 번째와 두 번째 예를 비교해 보면 컴파일된 패턴 객체인 charref는 모두 동일한 역할을 한다. 

하지만 정규식이 복잡할 경우 두 번째처럼 주석을 적고 여러 줄로 표현하는 것이 훨씬 가독성이 좋다는 것을 알 수 있다.



## 3. 백슬래시 문제

정규 표현식을 파이썬에서 사용할 때 혼란을 주는 요소가 한 가지 있는데, 바로 백슬래시(`\`)이다.

예를 들어 어떤 파일 안에 있는 `"\section"` 문자열을 찾기 위한 정규식을 만든다고 가정해 보자.

```
\section
```

이 정규식은 `\s` 문자가 whitespace로 해석되어 의도한 대로 매치가 이루어지지 않는다.

위 표현은 다음과 동일한 의미이다.

```
[ \t\n\r\f\v]ection
```

의도한 대로 매치하고 싶다면 다음과 같이 변경해야 한다.

```
\\section
```

즉 위 정규식에서 사용한 `\` 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.

따라서 위 정규식을 컴파일하려면 다음과 같이 작성해야 한다.

```
>>> p = re.compile('\\section')
```

그런데 여기에서 또 하나의 문제가 발견된다. 위처럼 정규식을 만들어서 컴파일하면 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 `\\`이 `\`로 변경되어 `\section`이 전달된다.

> ※ 이 문제는 위와 같은 정규식을 파이썬에서 사용할 때만 발생한다(파이썬의 리터럴 규칙). 유닉스의 grep, vi 등에서는 이러한 문제가 없다.

결국 정규식 엔진에 `\\` 문자를 전달하려면 파이썬은 `\\\\`처럼 백슬래시를 4개나 사용해야 한다.

> ※ 정규식 엔진은 정규식을 해석하고 수행하는 모듈이다.

```
>>> p = re.compile('\\\\section')
```

이렇게 해야만 원하는 결과를 얻을 수 있다. 하지만 너무 복잡하지 않은가?

만약 위와 같이 `\`를 사용한 표현이 계속 반복되는 정규식이라면 너무 복잡해서 이해하기 쉽지않을 것이다. 이러한 문제로 인해 파이썬 정규식에는 Raw String 규칙이 생겨나게 되었다. 즉 컴파일해야 하는 정규식이 Raw String임을 알려 줄 수 있도록 파이썬 문법을 만든 것이다. 그 방법은 다음과 같다.

```
>>> p = re.compile(r'\\section')
```

위와 같이 정규식 문자열 앞에 r 문자를 삽입하면 이 정규식은 Raw String 규칙에 의하여 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 된다.



---

**references**

[점프 투 파이썬](https://wikidocs.net/4308)

[youtube: 조코딩 Jocoding](https://youtu.be/dTDoTR0MXjU)