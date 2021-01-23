# 정규표현식



## greedy and non-greedy match

| method  | 목적                                                   |
| ------- | ------------------------------------------------------ |
| group() | 매치된 문자열을 돌려준다.                              |
| start() | 매치된 문자열의 시작 위치를 돌려준다.                  |
| end()   | 매치된 문자열의 끝 위치를 돌려준다.                    |
| span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다. |



정규식에서 Greedy란 어떤 의미일까 ??

예를 하나 들어보겠습니다. 



```python
import re # Regular expression

text = '<html><head><title>Title</title>'
print(len(text))
# 32
print(re.match('<.*>', text).span())
# (0, 32)
print(re.match('<.*>', text).group())
# <html><head><title>Title</title>
print(re.match('<.*?>', text).group())
# <html>
print(re.match('<.*?>', text).end())
# 6
```



수량표현식 ( * + { } ) 은 욕심이 많은(greedy) 연산자이기 때문에, 제공된 데이터에서 최대한 많이 매칭하려고 합니다.

| 표현식  | 의미                                                         |
| ------- | ------------------------------------------------------------ |
| x?      | 존재여부 표현. x 문자가 존재할 수도, 아닐 수도 있음          |
| .x      | 임의의 한 문자의 자리수, 문자열이 x로 끝남                   |
| x*      | 반복여부. 문자가 0번 또는 그 이상 반복됨을 의미              |
| x+      | 반복을 표현. x 문자가 한 번 이상 반복됨                      |
| x{n, m} | 반복을 표현. x 문자가 최소 n번 이상 최대 m 번 이하로 반복됨을 의미 |

'<.*>' 라면 <와 > 사이 반복되는 임의의 문자가 존재하는 문자열을 의미할텐데, 이 때 최대한 많은 매칭을 이루는 `<html><head><title>Title</title>` 를  매칭하게 되는 것입니다.

반면 non-greedy 표현식을 사용해 수량표현식의 탐욕을 제한할 수 있습니다.

```python
import re # Regular expression

text = '<html><head><title>Title</title>'
print(re.match('<.*?>', s).group())
# <html>
```

`*?`, `+?`, `??`, `{m, n}?` 과 같이 사용이 가능합니다.

non-greedy 표현식은 가능한 한 가장 최소한의 반복을 수행하도록 합니다.



- 즉 greedy match 는 최대 일치, non greedy match 는 최소 일치라고 생각하면 되겠습니다.

또한 `.`과 같은 연산자를 사용하지 않고, 좀 더 엄격한 정규식을 사용하는 방법이 좋겠습니다.