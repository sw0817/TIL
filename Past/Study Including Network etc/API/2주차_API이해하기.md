# 2주차__API_이해하기

[TOC]

## 1. API

> API: Application Programming Interface 
>
> 한 줄로 요약하면, "프로그램(Application) 사이의 커뮤니케이션을 담당하는 것"이라 볼 수 있다.

### #1. API 정의와 개념

![API](http://blog.wishket.com/wp-content/uploads/2019/10/API-%EC%89%BD%EA%B2%8C-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0.png)

간단하게 도식을 살펴보면, API는 손님의 요청을 요리사에게 전달하는 웨이터로 볼 수 있다. 

손님은 아무 요청이나 할 수는 없고, 메뉴판을 보고 해당 요리사가 제공해줄 수 있는 것을 올바른 방법으로 요청하면 요리사는 그에 응답한다.  

---

API라는 단어는 사실 더 넓고 포괄적인 개념이다. 

API는 운영체제에서 제공해주기도 하고 실제로 컴퓨팅 초기부터 API라는 개념은 OS의 라이브러리 개념으로 사용되었다. 실제로 컴퓨터를 초기에 배울 때 windows의 계산기 API를 사용하여 자신만의 윈도우 계산기를 만들어보는 실습을 많이 했다고 한다... 

[Windows API](https://docs.microsoft.com/en-us/windows/win32/apiindex/windows-api-list)

하지만 우리에게 익숙한 API라는 단어는 웹을 통해 데이터가 전달되는 것이다. 이는 정확하게 표현하면 API에 의해 조작되는 리소스가 요청을 보내는 컴퓨터의 외부에 있는 `원격 API`인 것이다.  가장 광범위하게 사용되는 커뮤니케이션 네트워크가 인터넷이기 때문에 대부분의 API는 웹 표준을 기반으로 설계되며, 모든 원격 API가 웹 API인 것은 아니지만 웹 API가 원격이라고 가정할 수 있다.

웹 API는 일반적으로 요청 메시지에 HTTP를 사용하여 응답 메시지 구조의 정의를 제공합니다. 이러한 응답 메시지는 일반적으로 XML 또는 JSON 파일의 형태입니다. 다른 애플리케이션이 쉽게 조작할 수 있는 방식으로 데이터를 표시하므로 XML과 JSON 둘 다 자주 사용됩니다.



아래는 함께 진행했던 `pjt02` 에서 KOBIS의 API를 사용했던 코드의 일부이다. 

```python
class URLMaker:    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    

    def __init__(self, key):
        self.key = key


    def get_url(self, category='people', feature='searchPeopleList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'  
    
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/{category}/{feature}.json?key={09de8ccc5d7---86903*****3b}
```

우리는 위의 기본 url에 category, feature, API key 값 등을 넣어서 요청을 보냈다. 그러면 kobis에서는 해당 요청(REQUEST)이 올바른 방식으로 넘어온다면, 데이터를 요청자에게 보내주는 응답(RESPONSE)을 한다.



### #2. API 유형

1. Private API
   - 사내에서 개발자들끼리 사용하는 경우
2. Partner API
   - 계약을 맺은 파트너 회사들과 API를 통해 데이터를 전송받을 때 사용 
3. Public API
   - 오픈 API
     - API 중에서 플랫폼의 기능 또는 콘텐츠를 외부에서 웹 프로토콜(HTTP)로 호출해 사용할 수 있게 개방(open)한 API를 의미합니다. 네이버 개발자센터에서 제공하고 있는 지도, 검색을 비롯 기계 번역, 캡차, 단축 URL 등 대부분 API는 HTTP로 호출할 수 있는 오픈 API에 해당합니다.
     - (NaverD2) API 중에서 플랫폼의 기능 또는 콘텐츠를 외부에서 웹 프로토콜(HTTP)로 호출해 사용할 수 있게 개방(open)한 API를 의미합니다. 네이버 개발자센터에서 제공하고 있는 지도, 검색을 비롯 기계 번역, 캡차, 단축 URL 등 대부분 API는 HTTP로 호출할 수 있는 오픈 API에 해당합니다.
     - 최근 이 `오픈 API` 라는 용어가 많이 사용되는데, 이는 `대기업`,`IT기업`,`정부 공공기관` 등에서 공익의 목적으로 다양한 사람들이 데이터에 접근하고 활용할 수 있도록 Public으로 개방하고 있기 때문이다. 



### #3. 그러면 웹 프로토콜하고 API하고는 무슨 차이인거지?

- 웹 프로토콜은 좀 더 광범위하게 우리가 웹 브라우저를 통해 소통할 때는 "이러 ~ 저러~한 규칙을 통해서 서로 소통하자."고 약속한 것으로 웹이라는 사회의 '법'과 같은 개념이다. 
- API는 프로그램 간의 소통 규칙이다. 다시 말해 프로그램의 사용설명서와 같이 프로그램을 만드는 회사에서 자신들이 제공하는 프로그램을 어떠한 방식으로 사용하면 되는지 알려주는 것이다.
- 다시 말해서, 우리가 어떤 서비스를 만들 때, 지도 기능이 필요하다면 우리가 직접 만들 수도 있지만 네이버에서 제공하는 지도 API를 사용해서 네이버 지도를 내 서비스 내에 포함시킬 수 있는 것이다. 또 가장 많이 사용하는 기능이 바로 로그인 기능이다. 우리는 어떤 앱을 새롭게 가입할 때 여러 과정을 거치는 것이 귀찮다. 때문에 앱 개발자들은 이 귀찮음을 최소화하여 사용자 경험을 높이려고 하므로, 대부분의 사람들이 가지고 있는 네이버, 구글, 카카오 등의 계정을 활용해서 접속할 수 있도록 해주는 것이다. 
- 따라서, 인터넷에서 HTTP는 모두가 지키기로 한 약속이므로 거의 모든 통신은 http를 통해서 이루어진다. 하지만 API는 프로그램간 소통이기 때문에 서로가 필요할 때에만 규칙을 지켜 활용하면 된다.



## 2. REST API

> REST: Representational State Transfer
>
> **웹에 존재하는 모든 자원(이미지, 동영상, DB 자원)에 고유한 URI를 부여해 활용"**하는 것으로, 자원을 정의하고 자원에 대한 주소를 지정하는 방법론을 의미한다. 
>
> 무슨말인지 전혀 모르겠으니 찬찬히 살펴보자

### #1. REST API와 RESTful

REST는 API를 표현하는 형식이다. 이전에는 SOAP라는 형식을 많이 사용했는데 이 방식이 복잡해서 항상 많은 분량의 API 문서가 필요했다.

REST는 이러한 불편한 점을 개선하고 좀 더 동적인 개발환경을 위해 새롭게 등장한 API형식이다.

REST는 위 정의들을 구현하는 방식에 제약을 두지 않고 권고 하는 것이다. 따라서 구체적인 가이드라인 혹은 규약이 없다.

규약이 없다는 것은 자유롭다는 뜻이지만 곧 혼란스럽다는 이야기와 동일하다. 

때문에 많은 개발자들은 자신들이 생각하는 REST스럽다고 생각하는 것들에 대해 의견을 제시했고 그러한 비공식적인 의견들을 모은 guidelines을 잘 따르는 것을 `RESTful하다 `고 할 수 있다.

이런 비공식적인 개발자들의 의견들을 모아 MS에서 REST API에 대한 가이드라인을 내놓으셨습니다. Official한 '법'은 아니긴 하지만 대부분 잘 지키는 '관습법' 정도로 생각하면 되겠다.  

참고: [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md)



학생(student) 데이터를 관리하는 API를 생각해보자. 아래는 student에 관한 resource 예시 이다.

```json
{
  "id": 1,
  "firstName": "Tyrion",
  "lastName": "Lannister",
  "classes": [
    {"id": 1, "name": "History of Westeros"}, 
    {"id": 2, "name": "Brewing"}, 
    {"id": 3, "name": "High Valyrian 101"}
  ]
}
```

이제 이러한 데이터를 CRUD하는 url routing을 생각해보자

```python
[POST] /students : 새 student를 등록
[GET] /students : 전체 student list를 호출
[GET] /students/1 : 1번 student를 호출
[PUT] /students/1 : 1번 student의 정보를 수정
[DELETE] /students/1 : 1번 student의 정보를 삭제
```

django project할 때 우리는 이렇게 url을 작성하도록 교육받았다. 이것이 REST API의 routing guidlines를 따르는 예시이다.

그렇다면 RESTful 하지 못한 것에는 무엇이 있을까?

- CRUD(생성,조회,수정,삭제)기능을 모두 POST로만 처리하는 [API](https://www.a-mean-blog.com/ko/blog/토막글/_/API)
- Route에 resource, id 외 정보가 들어가는 경우 (예를 들어 [POST] /students/update -> 이 route을 RESTful하게 고치면 [PUT] students/:id )
- URI에 동사가 들어가는 경우 (> _**명사만 권장**)

 ```python
RESTful 하지 못한 예
[POST] /GetStudentList
[POST] /GetStudent/:id
[POST] /CreateStudent
[POST] /UpdateStudent/:id
[POST] /DeleteStudent/:id
 ```



REST의 가장 중요한 특징은

1. **Self-descriptive**:  '스스로 설명 가능하다'. 즉, **요청 URL의 모습 그 자체로 이 요청이 무엇을 요청하는 것인지 추론 가능하다는 것**'이다. 

2. **HATEOAS**: 'Hypermedia As The Engin of Application State'. 하이퍼 미디어 컨트롤. 하이퍼 미디어 어플리케이션의 상태를 관리하기 위한 매커니즘을 말하고REST API에서 서버가 클라이언트에 리소스를 넘겨줄 때 특정 부가적인 리소스의 링크 정보를 넘겨주어 클라이언트가 이를 참고하여 사용 할 수 있도록 한다.

   <요청 REQUEST>

   ```json
   GET /accounts/12345 HTTP/1.1
   Host: bank.example.com
   Accept: application/vnd.acme.account+json
   ```

   <응답 RESPONSE>

   ```json
   [EX 1]
   HTTP/1.1 200 OK
   Content-Type: application/xml
   Content-Length: ...
   
   <?xml version="1.0"?>
   <account>
       <account_number>12345</account_number>
       <balance currency="usd">100.00</balance>
       <link rel="deposit" href="https://bank.example.com/accounts/12345/deposit" />
       <link rel="withdraw" href="https://bank.example.com/accounts/12345/withdraw" /> 
       <link rel="transfer" href="https://bank.example.com/accounts/12345/transfer" />
       <link rel="close" href="https://bank.example.com/accounts/12345/status" />
   </account>
   
   [EX 2]
   HTTP/1.1 200 OK
   Content-Type: application/xml
   Content-Length: ...
   
   <?xml version="1.0"?>
   <account>
       <account_number>12345</account_number>
       <balance currency="usd">-25.00</balance>
       <link rel="deposit" href="https://bank.example.com/accounts/12345/deposit" />
   </account>
   ```
   

위 요청과 응답을 살펴보면, 일단 묻고 있는 계좌(12345)의 남은 잔고와 함께 deposit, withdraw .. 등등을 할 수 있는 links 들을 함께 전송해준다. Client는 이 link들을 받아서 추가적인 action을 다시 할 수 있게 된다. 

Client는 위 URI를 그대로 써도 도지만  link의 rel(relation)만을 활용한다면 URI 주소가 바뀌더라도 충분히 활용할 수 있다.

   또 아래는 잔고가 - 25일 때의 응답 예시인데, 이때는 withdraw, transfer 같은  기능은 불가능하도록 response가 동적으로 변화한다. 이러한 특징들이 `HATEOAS`이다.

​	

이 외에도 REST의 6가지 특성은 다음과 같다. Uniform Interface, Client-Server, Stateless, Cacheable, Layered System, Code on Demand. 이런 것들이 지켜졌을 때 REST하다고 하는데, 워낙 광범위한 내용이다 보니 오늘은 다루지 않고 넘어가겠다. 



### #3. REST API가 최근 각광받는 이유는?

1.  단연 협업에서의 `생산성`을 높이기 때문이다. -> 통일성 & 이름짓는 수고 덜어줌.

   API는 앞에서 언급했듯이 내부 개발자들끼리 혹은 새로운 개발자들이 들어왔을 때, 타 회사의 다른 개발자들과 함께 업무를 할 때, Open  API로 외부의 모든 개발자들과 소통할 일이 상당히 많아졌기 때문이다. 

   django에서 CRUD를 배웠다. 그리고 우리는 자연스럽게 만드는 요청을 보내는 주소로 'CREATE'을 사용했고, 삭제할 때는 'DELETE', 수정할 때는 'UPDATE' 같은 단어로 url을 생성했다. 물론 다른 단어로 변경한다 하더라도 동작에는 전혀 무리가 없다. 하지만, 개발자들은 무의식적으로 자주 쓰는 API 형식과 이름들을 기대하고 있으며 이를 지키지 않는 코드, API 구조 등을 보면 '아 이 XX뭐야... '하고 욕을 박는다. 이는 우리가 HTML5 에서 Semantic Tag 등을 사용하는 이유와 유사하다고 할 수 있다. (** 욕먹지 않는 개발자가 되기 위해서는 개발자들 사이의 convention을 잘 학습하고 사용하도록 하자 ^^)

   또한, 웹 개발 환경이 점점 동적으로 변화하고 있기 때문이기도 하다. 

   20년 전 웹의 모습은 거의 HTML 문서들간의 연결이었다고 봐도 무방하다. 하지만 최근 웹에서는 실시간 LIVE 방송이 진행되기도 하고 실시간으로 게임이 돌아가기도 하는 등 Client와 Server간 통신이 상당히 동적이다. 이런 상황에서 API는 보다 명시적일 필요가 있으며, SERVER side에 변화가 있더라도 Client side에서는 이 변화에 상관없이 동일하게 동작할 수 있도록 하는 상황이 필요해진 것이다.  

2. 윈윈(win-win)이다.
   신규 서비스를 개발하는 입장에서는 '지도, 날씨'와 같은 데이터가 많이 필요하고 만드는데 시간이 오래 걸리는 기능들을 이전에 잘 만들어놓은 다른 기업의 서비스로부터 API를 받아서 쓰면 개발 시간이 확 줄어든다. 

   소프트웨어의 격언 중에는 이런 말이 있다. `Don't reinvent the wheel.` '바퀴가 이미 있는데 또 바퀴를 만들 필요는 없다.'
   
   반대로 제공하는 기업에서는 자신들의 서비스 사용자가 늘어날 수 있는 새로운 기회가 된다. 이미 만들어둔 기능을 최대한 많은 사람들이 많이 많이 써주는게 좋은데, 신규 서비스가 자신들의 소프트웨어 프로그램을 써준다면 돈안쓰고 광고하는 셈이 되는 것이다. 



## 3. (실습) 구글 맵 API 사용

1. [구글맵 문서](https://developers.google.com/maps/documentation/embed/get-started?hl=ko)

2. 사용자 인증 정보 maps embed  API -> 어플리케이션 생성

3. 인증키 받기

4. index.html 생성

5. 예시 iframe 코드 넣기

6. 문서 아래 내용 보면서 커스터마이징 하기 

   예) 지도 초기화면을 파리 에펠탑으로 띄우기 -> 에펠탑 view mode satellite모드로 보기

 

이 두 개는 REST API와 Graphql에 대해 간단하고 재밌게 잘 설명해서 오늘 끝나고 한 번 보는걸 추천합니다.

[얄팍한 코딩사전- REST API가 뭔가요?](https://youtu.be/iOueE9AXDQQ)

[얄팍한 코딩사전- Graphql이 뭔가요?](https://youtu.be/iOueE9AXDQQ)

오늘 수업 중에 URI라는 용어를 계속 사용했는데, URL이 아닌가? 하는 의문이 있었을 수 있습니다. URI와 URL의 개념은 아래 도식과 같으며 구체적인 설명은 아래 링크를 통해 확인해보시면 좋겠습니다.

[URI와 URL]([https://velog.io/@pa324/%EA%B0%9C%EB%B0%9C%EC%83%81%EC%8B%9D-URI-URL-%EC%B0%A8%EC%9D%B4-%EC%A0%95%EB%A6%AC](https://velog.io/@pa324/개발상식-URI-URL-차이-정리))

![img](https://media.vlpt.us/post-images/pa324/43314730-092e-11ea-9e05-cf069c31c421/image.png)



-------

**References**

[API(애플리케이션 프로그래밍 인터페이스): 개념, 기능, 장점](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)

[WIN api를 이용한 계산기 만들기]([https://medium.com/@jckk9082/win-api%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EA%B3%84%EC%82%B0%EA%B8%B0-1-e825f3ccc10a](https://medium.com/@jckk9082/win-api를-활용한-계산기-1-e825f3ccc10a))

[API란?]([https://medium.com/@dydrlaks/api-%EB%9E%80-c0fd6222d34c](https://medium.com/@dydrlaks/api-란-c0fd6222d34c))

[그런 REST API로 괜찮은가](https://slides.com/eungjun/rest#/37)

[REST API 란 ?](https://ijbgo.tistory.com/20)
