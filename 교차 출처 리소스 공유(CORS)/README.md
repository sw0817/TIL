



# 교차 출처 리소스 공유

# (Cross-Origin Resource Sharing, CORS)

[TOC]

## 1. CORS의 기본적 내용

**CORS는 웹 개발자라면 한 번쯤은 마주하게 될 정책이다.**

- Mozilla 에서는 CORS를 아래와 같이 설명하고 있다.

  `교차 출처 리소스 공유`는 추가 `HTTP 헤더`를 사용하여, 한 `출처`에서 실행 중인 웹 애플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제입니다. 웹 애플리케이션은 리소스가 자신의 출처(도메인, 프로토콜, 포트)와 다를 때 교차 출처 HTTP 요청을 실행합니다.

- 쉽게 말해 교차 출처 자원 공유는 웹 페이지 상의 제한된 리소스를 최초 자원이 서비스된 도메인 밖의 다른 도메인으로부터 요청할 수 있게 허용하는 구조이다. CORS는 교차 출처 요청을 허용하는 것이 안전한지 아닌지를 판별하기 위해 브라우저와 서버가 상호 통신하는 하나의 방법을 정의한다.

---



### 1.1 시작 전 집고 넘어갈 점

- CORS를 직역하니 `Cross-Origin` 을 `교차 출처` 로 해석되었는데 `"다른출처"` 로 생각하는게 이해에 도움이 된다.
- 즉 CORS 는 `다른 출처간의 리소스 공유` 라는 의미 !

---



### 1.2 출처(Origin)


 **서버의 위치를 의미하는 URL은 여러 개의 구성 요소로 이루어져 있다.**

![](README.assets/출처.JPG)

- 출처는 위 그림과 같이 `Protocol` 과 `Host` 등, 그리고 그림에 없는 `:443` 과 같은 포트 번호까지 모두 합친 것을 의미한다. 즉, 서버의 위치를 찾아가기 위해 필요한 가장 기본적인 것들을 합쳐놓은 것.

- 출처 내의 포트 번호는 생략이 가능한데, 이는 각 웹에서 사용하는 `HTTP`, `HTTPS` 프로토콜의 기본 포트 번호가 정해져 있기 때문.
- But, 만약 `https://google.com:443` 과 같이 출처에 포트 번호가 명시적으로 포함된다면, 이 포트 번호까지 모두 일치해야 같은 출처라고 인정된다.
  - 그런데 이 케이스에 대한 명확한 정의가 표준으로 정해진 것은 아니어서, 어떤 경우에는 다른 출처로 판단될 수도 있다고 함,,

---



### 1.3 SOP(Same-Origin Policy) 동일출처 정책



**웹 세계에서 다른 출처로의 리소스 요청을 제한하는 것과 관련된 정책은 두 가지인데, 한 가지는 앞서 소개한 CORS, 나머지 한 가지가 `SOP` 이다.**

**SOP의 의미 : "같은 출처에서만 리소스를 공유할 수 있다"** **즉 이 동일 출처 정책은 한 도메인의 JavaScript 코드를 불러오면 해당 코드 안에서 다른 도메인의 데이터를 요청할 수 없다는 것을 의미한다.**

**대표적으로 `XMLHttpRequest`와 [Fetch API](https://developer.mozilla.org/ko/docs/Web/API/Fetch_API)는 [동일 출처 정책](https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy) 을 따른다.**

**여기서 `XMLHttpRequest` 는 비동기 웹 기술에 관련된 객체이고(대표적으로 ajax 요청),`fetch`란 쉽게 말해 웹 리소스를 가져오는 고수준 api를 뜻한다. html의 img태그나 scipt 태그, javascript,css 의 리소스 접근에 관한 일부 api도 Fetch의 구현체다.**

**하지만 최근에는 웹이라는 오픈된 환경에서 ajax가 대중화되고, OPEN API 등 다른 출처에 있는 리소스를 가져와 활용하는 일은 매우 흔한 일로 무작정 막을 수는 없음. 그래서 몇 가지 예외 조항을 두고 이 조항에 해당하는 리소스 요청은 다른 출처라도 허용하기로 했는데, 그 중 하나가 `CORS 정책을 지킨 리소스 요청` 이다.**



- 왜 이러한 정책이 만들어 졌을까 ?

출처가 다른 두 개의 어플리케이션이 제약없이 소통할 수 있는 환경이 위험하기 때문이다. 특히 웹 어플리케이션의 경우 브라우저의 개발자 도구만 열어도 어떤 서버와 통신하는지, 리소스의 출처는 어디인지와 같은 각종 정보들을 아무런 제재없이 열람할 수 있다. 

(최근에는 자바스크립트 소스 코드를 난독화해 읽기 어렵다고는 한다. But 난독화는 암호화가 아니므로, 소스 코드를 직접 볼 수 있다는 것 자체가 보안적으로 상당히 취약하다.)

이런 환경에서 아무런 제약이 존재하지 않는다면, 악의를 가진 사용자가 소스 코드를 쓱 구경한 후 [CSRF(Cross-Site Request Forgery)](https://ko.wikipedia.org/wiki/사이트_간_요청_위조)나 [XSS(Cross-Site Scripting)](https://ko.wikipedia.org/wiki/사이트_간_스크립팅)와 같은 방법을 사용하여 사용자의 어플리케이션에서 코드가 실행된 것처럼 꾸며서 사용자의 정보를 탈취하기가 너무나도 쉬워진다.



- 즉, 우리가 다른 출처로 리소스를 요청하면 SOP 정책을 위반하는 것이고, SOP의 예외 조항인 CORS 정책까지 위반한다면 아예 다른 출처의 리소스를 사용할 수 없게 되는 것이다.

**결론적으로, 다른 출처로 리소스를 요청하기 위해서는 SOP에서 정의된 예외 조항과 CORS를 사용할 수 있는 케이스를 따라야 한다는 것이다.**

---



### 1.4 같은 출처와 다른 출처의 구분

결론부터 말하자면, 두 URL의 구성 요소 중 `Scheme`, `Host`, `Port` 이 3가지만 동일하면 두 개의 출처가 서로 같다.

`https://mensan-sanghun.github.io:80` 이라는 출처로 예를 들자면 `https://` 이라는 스킴에 `mensan-sanghun.github.io` 호스트를 가지고 `:80` 번 포트를 사용하고 있다는 것만 같다면, 나머지는 전부 다르더라도 같은 출처로 판단된다는 것이다.



- 예시(출처가 https://mensan-sanghun.github.io 일 때)

| URL                                            | 같은 출처 여부 | 이유                        |
| ---------------------------------------------- | -------------- | --------------------------- |
| https://mensan-sanghun.github.io/about         | O              | 스킴, 호스트, 포트가 동일   |
| https://mensan-sanghun.github.io/about?q=상훈  | O              | 스킴, 호스트, 포트가 동일   |
| https://user:password@mensan-sanghun.github.io | O              | 스킴, 호스트, 포트가 동일   |
| http://mensan-sanghun.github.io                | X              | 스킴이 다름                 |
| https://api.github.io                          | X              | 호스트가 다름               |
| https://mensan-sanghun.naver.com               | X              | 호스트가 다름               |
| https://mensan-sanghun.github.io:8000          | ?              | 브라우저의 구현에 따라 다름 |

맨 마지막 케이스의 경우, 만약 출처에 `https://mensan-sanghun.github.io:80` 처럼 포트 번호가 명시되어 있다면 다른 출처이지만, 예시로 든 출처의 경우 포트 번호가 포함되지 않아 판단하기 애매하다.

이런 경우에는 각 브라우저들의 독자적인 출처 비교 로직을 따라간다.

**여기서 중요한 점은, 이렇게 출처를 비교하는 로직이 서버에 구현된게 아니라 브라우저에 구현되어 있는 점이다.**

**그렇기 때문에, 우리가 CORS 정책을 위반하는 리소스 요청을 해도, 해당 서버가 같은 출처에서 보낸 요청만 받는 로직을 가진 경우가 아니라면, 서버는 정상적으로 응답을 하고 이후 브라우저에서는 이 응답을 분석해 CORS 정책 위반이라고 판단하고 그 응답을 사용하지 않고 버린다.**

**즉, CORS는 브라우저의 구현 스펙에 포함되는 정책이기 때문에, 브라우저를 통하지 않고 서버 간 통신을 할 때는 이 정책이 적용되지 않는다. 또한 CORS 정책을 위반하는 리소스 요청 에러가 발생해도, 서버 쪽 로그에는 정상적으로 응답을 했다는 로그가 남아 혼란을 야기할 수 있다.**

---





## 2. CORS의 동작

기본적으로 웹 클라이언트 어플리케이션이 다른 출처의 리소스를 요청할 때는 HTTP 프로토콜을 사용하여 요청을 보내게 되는데, 이때 브라우저는 요청 헤더에 `Origin` 이라는 필드에 요청을 보내는 출처를 함께 담는다,

```http
# http
Origin: https://mensan-sanghun.github.io
```

이후 서버가 이 요청에 대한 응답을 할 때 응답 헤더의 `Access-Control-Allow-Origin`이라는 값에 “이 리소스를 접근하는 것이 허용된 출처”를 내려주고, 이후 응답을 받은 브라우저는 자신이 보냈던 요청의 `Origin`과 서버가 보내준 응답의 `Access-Control-Allow-Origin`을 비교해본 후 이 응답이 유효한 응답인지 아닌지를 결정한다.

기본적 흐름은 이와 같고, CORS가 동작하는 방식은 세 가지의 시나리오가 있다.

---



### 2.1 CORS의 시나리오

###### 1. simple request, 2. preflight request, 3. credentialed request



#### Simple Request 시나리오를 들어가기 전에

이 시나리오 케이스에 대한 정식 명칭은 없지만, MDN의 CORS 문서에서는 이 시나리오를 [Simple Request](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS#접근_제어_시나리오_예제)라고 부르고 있다.

Simple Request의 정의에 앞서 CORS Preflight 에 대해 먼저 집고 넘어가는게 이해하기에 좋다. 

---

#### Preflight Request(예비 요청 시나리오)

`프리플라이트(Preflight)` 방식은 일반적으로 우리가 웹 어플리케이션을 개발할 때 가장 마주치는 시나리오이다. 이 시나리오에 해당하는 상황일 때 브라우저는 요청을 한번에 보내지 않고 예비 요청과 본 요청으로 나누어서 서버로 전송한다.

이때 브라우저가 본 요청을 보내기 전에 보내는 예비 요청을 Preflight라고 부르는 것이며, 이 예비 요청에는 HTTP 메소드 중 `OPTIONS` 메소드가 사용된다. 예비 요청의 역할은 본 요청을 보내기 전에 브라우저 스스로 이 요청을 보내는 것이 안전한지 확인하는 것이다.

자바스크립트를 예를 들어 이 과정을 간단한 플로우 차트로 나타내보면 다음과 같다.

![](README.assets/Preflight.JPG)

> 브라우저는 본 요청을 보내기 전 예비 요청을 먼저 보내고, 요청의 유효성을 검사한다.

자바스크립트의 `fetch API`를 사용하여 브라우저에게 리소스를 받아오라는 명령을 내리면 브라우저는 서버에 예비 요청을 먼저 보내고, 서버는 이 예비 요청에 대한 응답으로 현재 자신이 어떤 것들을 허용하고, 어떤 것들을 금지하고 있는지에 대한 정보를 응답 헤더에 담아 브라우저에게 다시 보내주게 된다.

이후 브라우저는 자신이 보낸 예비 요청과 서버가 응답에 담아준 허용 정책을 비교한 후, 이 요청을 보내는 것이 안전하다고 판단되면 같은 엔드포인트로 다시 본 요청을 보내게 된다. 이후 서버가 이 본 요청에 대한 응답을 하면 브라우저는 최종적으로 이 응답 데이터를 자바스크립트에게 넘겨준다.



> 이 플로우는 브라우저의 개발자 도구 콘솔에서도 재현해볼 수 있는데, 아직 JS 사용에 대한 이해도가 떨어져 다른 개발자가 재현한 예제를 통해 공부해보았다.

---

- 예제

개발자의 블로그 환경에서 개발자의 티스토리 블로그의 RSS 파일 리소스에 요청을 보내면 브라우저가 본 요청을 보내기 전에 `OPTIONS` 메소드를 사용하여 예비 요청을 보내는 것을 확인할 수 있다.

![](README.assets/Preflight_1.JPG)

실제로 브라우저가 보낸 요청을 보면, 단순히 `Origin`에 대한 정보 뿐만 아니라 자신이 예비 요청 이후에 보낼 본 요청에 대한 다른 정보들도 함께 포함되어 있는 것을 볼 수 있다.

위 예비 요청에서 브라우저는 `Access-Control-Request-Headers`를 사용하여 자신이 본 요청에서 `Content-Type` 헤더를 사용할 것을 알려주거나, `Access-Control-Request-Method`를 사용하여 이후 `GET` 메소드를 사용할 것을 서버에게 미리 알려주고 있는 것이다.

이후, 티스토리 서버는 예비 요청에 대한 응답을 보내준다.

![](README.assets/Preflight_2.JPG)

여기서 중요하게 볼 것은 `Access-Control-Allow-Origin: https://evanmoon.tistory.com`라는 값이다.

티스토리 서버는 이 리소스에 접근이 가능한 출처는 오직 `https://evanmoon.tistory.com` 뿐이라고 브라우저에게 이야기해준 것이고, 개발자가 이 요청을 보낸 출처는 `https://evan-moon.github.io`이므로 서버가 허용해준 출처와는 다른 출처이다.

결국 브라우저는 이 요청이 CORS 정책을 위반했다고 판단하고 다음과 같은 에러를 뱉는다.

![](README.assets/Preflight_3.JPG)

위 예비 요청에 대한 응답에서 에러가 발생하지 않고 `200` 이 정상적으로 응답되었는데, 콘솔 창에서는 에러가 표시되는 부분이 많은 개발자를 헷갈리게 한다. 결론부터 말하자면 CORS 정책 위반으로 인한 에러는 예비 요청의 성공 여부와 별 상관이 없다. 브라우저가 CORS 정책 위반 여부를 판단하는 시점은 예비 요청에 대한 응답을 받은 이후이기 때문이다.

중요한 것은 예비 요청의 성공/실패 여부가 아니라 “응답 헤더에 유효한 `Access-Control-Allow-Origin` 값이 존재하는가”이다. 만약 예비 요청이 실패해서 `200`이 아닌 상태 코드가 내려오더라도 헤더에 저 값이 제대로 들어가있다면 CORS 정책 위반이 아니라는 의미이다.

---

#### Simple Request(단순 요청 시나리오)

대부분의 경우 Preflight Request 방식을 사용해 예비 요청과 본 여청을 나누어 보내지만, 예비 요청없이 본 요청만으로 CORS 정책 위반 여부를 검사하기도 한다.

이 시나리오는 Preflight Request 시나리오와 전반적인 로직 자체는 같되, 예비 요청의 존재 유무만 다르다.

예비 요청을 보내지 않고 바로 서버에게 본 요청을 보낸 후, 서버가 이에 대한 응답의 헤더에 `Access-Control-Allow-Origin`과 같은 값을 보내주면 그때 브라우저가 CORS 정책 위반 여부를 검사하는 방식이다.

![](README.assets/simple.JPG)

> 단순 요청은 예비 요청없이 바로 본 요청을 보낸다.

다만 단순 요청은 특정 조건을 만족하는 경우에만 가능하고, 이 조건은 까다로운 편이라 거의 경험하기 힘든 편이다.

1. 요청의 메소드는 `GET`, `HEAD`, `POST` 중 하나여야 한다.
2. `Accept`, `Accept-Language`, `Content-Language`, `Content-Type`, `DPR`, `Downlink`, `Save-Data`, `Viewport-Width`, `Width`를 제외한 헤더를 사용하면 안된다.
3. 만약 `Content-Type`를 사용하는 경우에는 `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`만 허용된다.

2번 조건에 명시된 헤더는 매우 기본적인 헤더들이고, `Authorization` 헤더 조차 저 조건에는 포함되지 않는다. 또한, 대부분의 HTTP API는 `text/xml`이나 `application/json` 컨텐츠 타입을 가지도록 설계되기 때문에 3번 조건을 만족시키기도 매우 어렵다.

---

#### Credentialed Request(인증된 요청 시나리오)

이번 시나리오는 CORS의 기본적 방식이라기 보다 다른 출처 간 통신에서 보안을 좀 더 강화하고 싶을 때 사용하는 방법이다.

기본적으로 브라우저가 제공하는 비동기 리소스 요청 API인 `XMLHttpRequest` 객체나 `fetch API`는 별도의 옵션 없이 브라우저의 쿠키 정보나 인증과 관련된 헤더를 함부로 요청에 담지 않는다. 이때 요청에 인증과 관련된 정보를 담을 수 있게 해주는 옵션이 바로 `credentials` 옵션이다.

이 옵션에 사용할 수 있는 값과 의미는 다음과 같다.

| 옵션 값              | 설명                                            |
| -------------------- | ----------------------------------------------- |
| same-origin (기본값) | 같은 출처 간 요청에만 인증 정보를 담을 수 있다. |
| include              | 모든 요청에 인증 정보를 담을 수 있다.           |
| omit                 | 모든 요청에 인증 정보를 담지 않는다.            |

만약 `same-origin`이나 `include`와 같은 옵션을 사용하여 리소스 요청에 인증 정보가 포함된다면, 브라우저는 다른 출처의 리소스를 요청할 때 단순히 `Access-Control-Allow-Origin`만 확인하는 것이 아니라 좀 더 빡빡한 검사 조건을 추가하게 된다.

---

- 예제

앞선 예제의 개발자의 로컬환경과 블로그를 호스팅하고 있는 Github 서버와의 통신을 통해, 어떤 제약이 추가되었는지 보여주는 예제이다.



개발자의 블로그는 `Allow-Control-Allow-Origin` 값으로 모든 출처를 허용한다는 의미인 `*`가 설정되어있기 때문에, 다른 출처에서 개발자의 블로그로 리소스를 요청할 때 CORS 정책 위반으로 인한 제약을 받지 않는다.

그래서 `http://localhost:8000`과 같은 로컬의 개발 환경에서도 `fetch API`를 사용하여 마음대로 리소스를 요청하고, 또 받아올 수 있다.

![](README.assets/Credentialed_1.JPG)

구글 크롬 브라우저의 `credentials` 기본 값은 같은 출처 내에서만 인증 정보를 사용하겠다는 `same-origin`이기 때문에, 로컬 환경에서 `https://evan-moon.github.io`로 보내는 리소스 요청에는 당연히 브라우저의 쿠키와 같은 인증 정보가 포함되어 있지 않다.

그렇기 때문에 브라우저는 단순히 `Access-Control-Allow-Origin: *`이라는 값을 보고 “이 요청은 안전하다”라는 결론을 내리는 것이다. 그러나 `credentials` 옵션을 모든 요청에 인증 정보를 포함하겠다는 의미를 가진 `include`로 변경하고 같은 요청을 보내면 이번에는 상황이 조금 달라진다.

![](README.assets/Credentialed_2.JPG)

블로그를 호스팅하고 있는 Github 서버는 이번에도 동일한 응답을 보내주었지만, 브라우저의 반응은 다르다.

![](README.assets/Credentialed_3.JPG)

브라우저는 인증 모드가 `include`일 경우, 모든 요청을 허용한다는 의미의 `*`를 `Access-Control-Allow-Origin` 헤더에 사용하면 안된다고 이야기하고 있다.

이처럼 요청에 인증 정보가 담겨있는 상태에서 다른 출처의 리소스를 요청하게 되면 브라우저는 CORS 정책 위반 여부를 검사하는 룰에 다음 두 가지를 추가하게 된다.

> 1. `Access-Control-Allow-Origin`에는 `*`를 사용할 수 없으며, 명시적인 URL이어야한다.
> 2. 응답 헤더에는 반드시 `Allow-Control-Allow-Credentials: true`가 존재해야한다.

---



## 3. CORS를 해결할 수 있는 방법

그렇다면 이 복잡한 정책 CORS를 위반하지 않으려면 어떻게 해야하는건가 ?



### 3.1 Access-Control-Allow-Origin 세팅하기

CORS 정책 위반으로 인한 문제를 해결하는 가장 대표적이고 정석적인 방법은, 그냥 서버에서 `Access-Control-Allow-Origin` 헤더에 알맞은 값을 세팅해주는 것이다. (인터넷을 찾아보면 리버스 프록싱 등 몇 가지 꼼수가 있지만 로컬환경과 실제 서버 환경이 다른 경우 에러가 나기 쉽다. 그러므로 정석대로 하자)

이때 와일드카드인 `*`을 사용하여 이 헤더를 세팅하게 되면 모든 출처에서 오는 요청을 허용한다는 의미이므로 보안적으로 심각한 이슈가 발생할 수도 있다.

그러므로 `Access-Control-Allow-Origin: https://evan.github.io`와 같이 출처를 명시해주도록 한다.

Spring, Express, Django와 같이 이름있는 백엔드 프레임워크의 경우에는 모두 CORS 관련 설정을 위한 세팅이나 미들웨어 라이브러리를 제공하고 있으니 세팅 자체가 어렵지는 않을 것이다.



#### EX)장고에서 적용하기

먼저 장고 패키지를 설치한다.

```bash
>>> pip install django-cors-headers
```

설치가 완료되면, `settings.py`의 `INSTALLED_APP`과 `MIDDLEWARE`에 코드를 입력한다.

```django
INSTALLED_APPS = [
	'corsheaders',
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
]
```

마지막으로 `settings.py`에 아래와 같은 코드를 입력하면 된다. 아래 설정에서 CORS_ORIGIN_ALLOW_ALL=False를 하고 CORS_ORIGIN_WHITELIST를 지운다면 모든 요청을 허용하는 환경(테스트환경으로나 가능)

```django
##CORS
CORS_ORIGIN_ALLOW_ALL=False
CORS_ORIGIN_WHITELIST = [
	'google.com',
	'localhost:8000',
	'127.0.0.1:9000',
	'hostname.example.com',
]
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
```

---



CORS 정책 위반은 브라우저의 구현에서 발생하기 때문에, 프론트엔드 개발자가 이로 인한 문제를 겪는다. 하지만 문제 해결을 위해서는 백엔드 개발자가 서버 어플리케이션의 응답 헤더에 올바른 `Acccess-Control-Allow-Origin`이 내려올 수 있도록 세팅해줘야 한다.

그러므로 프론트엔드 개발자로서든, 백엔드 개발자로서든 이 정책위반 문제해결에 대한 지식을 가지고, 경험해볼 필요가 있다고 생각한다.

---

#### References

[교차 출처 리소스 공유 MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)

[Fetch API](https://developer.mozilla.org/ko/docs/Web/API/Fetch_API)

[CORS는 왜 이렇게 우리를 힘들게 하는걸까?](https://evan-moon.github.io/2020/05/21/about-cors/)

[Django-내 로컬 서버에서 외부접속 허용하기](https://velog.io/@devmin/Django-CORS-Setting-basic)

[Django CORS 설정과 API 연동](https://blog.thereis.xyz/41)

[교차 출처 리소스 공유 위키피디아](https://ko.wikipedia.org/wiki/%EA%B5%90%EC%B0%A8_%EC%B6%9C%EC%B2%98_%EB%A6%AC%EC%86%8C%EC%8A%A4_%EA%B3%B5%EC%9C%A0#cite_note-6)