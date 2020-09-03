# GET & POST

> 서버로 데이터를 전달하기 위해 사용한다는 기능적 측면에서는 같다.

![GET&POST](https://t1.daumcdn.net/cfile/tistory/99D83C395BCB27A001?download])

- GET과 POST 방식의 보안, 전달형식, 전달할 수 있는 데이터의 양에 따라 차이점이 발생!!



## 1. HTTP 패킷

- 클라이언트가 서버로 요청을 했을 때 보내는 데이터
- 헤더와 바디로 구성
- 헤더에서는 메서드 방식 / 클라이언트의 정보 / 브라우저 정보 / URL 등의 정보를 포함
- 바디는 보통 비어있음



## 2. GET

> 어떠한 정보를 가져와서 조회하기 위한 방식



### <특징>

```html
<FORM NAME="form1" ACTION="index.jsp" METHOD="GET"></FORM>
```

- DB에 추가로 정보를 처리하지 않고, 저장된 데이터를 단순 요청하는 정도로 사용
- URL에 변수를 포함시켜 요청한다.
  - /create/?title=안녕하세요&content=반갑습니다&my-site=파이팅
  - url에 그대로 query의 이름과 값이 각각 key와 value로 연결되어 표현된다.
    - query : 웹 서버에 특정한 정보를 보여달라는 웹 클라이언트의 요청에 의한 처리
- 전송하는 길이에 제한이 있다.
  - URL포함 255자까지 전송 가능
  - HTTP/1.1 에서는 2048자까지 가능
  - 초과 데이터는 절단됨.
- HTTP 패킷의 헤더에 포함. / 바디는 비어있다.
- URL에 데이터가 노출되어 보안에 취약하다.
  - URL형태로 데이터를 나타내기 때문에 특정 페이지를 타인이 접속 가능하다.
- POST 방식에 비해 빠른 이유 : Caching
  - Caching : 한 번 접근한 데이터에 대해 재요청 시 빠르게 접근하기 위해 레지스터에 데이터를 저장시켜 놓는 방식



## 3. POST

> 데이터를 서버로 제출하여 추가나 수정하기 위한 방식



### <특징>

```html
<FORM NAME="form1" ACTION="index.jsp" METHOD="POST"></FORM>
```

- DB에 서버에서 갱신 작업을 하거나 정보가 가공되어 응답하는 경우에 사용
- URL에 변수(데이터)를 노출하지 않고 요청한다.
  - HTTP 패킷의 바디에 데이터를 넣어서 보낸다.
  - 헤더 영역에는 바디의 데이터를 설명하는 Content-Type라는 헤더 필드와 데이터 타입을 명시한다. 이를 통해 요청이 전송된다.
  - https://gist.github.com/jays1204/703297eb0da1facdc454

```text
1. application/x-www-form-urlencoded

2. text/plain

3. multipart/form-data
```

```
HEADER 영역  

Content-Type:application/json; charset=UTF-8

.....

BODY 영역

{
	"param1":"value1",
	"param2":"value2"
}
```



- URL에 데이터가 노출되지 않아서 기본 보안은 되어있다.
  - URL에 데이터가 표시되지 않을 뿐 보안이 강력하다란 의미는 아님.
- 전송하는 길이나 데이터의 양은 제한이 없다.



## 4. 추가로

- Google의 "Accelerator"사건
  - GET, POST의 개념이 없이 개발하면서 발생한 문제
  - CRUD에서 GET은 READ를 호출하는 경우에 사용하고 나머지는 POST를 사용하는게 정석
  - 그러나 Accelerator가 URL을 가져오는 경우 GET으로 가져오는데 Delete를 GET으로 개발한 부분과 충돌해 링크의 메일이나 게시글이 지워지는 문제가 발생
- 자주 사용하는 메서드
  - PUT : 전체 수정 요청
  - PATCH : 부분 수정 요청
  - DELETE : 제거 요청
- 자주 사용하지는 않는 메서드(참고만)
  - OPTION : 서버가 어떤 메서드를 지원하는지 알아볼 때
  - HEAD : 요청에서 헤더만 가져올 때
  - CONNECT : 양방향 통신을 할 때
  - TRACE 



https://interconnection.tistory.com/72

https://www.zerocho.com/category/HTTP/post/5b3723477b58fc001b8f6385

