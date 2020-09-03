# DNS, Round robin DNS



# 1. 도메인 기본

1. 도메인이란?
   - 인터넷에 연결된 컴퓨터를 사람이 쉽게 기억하고 입력할 수 있도록 문자(영문, 한글 등)로 만든 인터넷주소



## 2. DNS(Domain Name System)

1. 정의
   - 네트워크 상에서 컴퓨터들은 IP 주소를 이용하여 서로를 구별하고 통신한다.
   - 그래서 사용자들이 네트워크를 통해 원격의 컴퓨터에 접속하기 위해서는 IP주소를 이용해야 함.
   - 그러나 IP주소를 일일이 외울 수 없기 때문에 쉽게 기억할 수 있는 DNS가 만들어짐
   - **DNS는 도메인 이름의 수직적인 체계를 말함**
2. 체계도
   - 도메인 관리자는 해당 도메인이 포함하는 영역을 관리할 수 있다.

![DNS](https://한국인터넷정보센터.한국/images/domain/imgDomainSys02.gif)

3. 도메인 이름 형성
   - 이름 형성의 규칙은 [RFC 1035](https://tools.ietf.org/html/rfc1035), [RFC 1123](https://tools.ietf.org/html/rfc1123), RFC 2181에 정의되어 있다.
   - 도메인 이름은 한 개 이상의 부분(레이블)으로 이루어지고, 점으로 구분하여 붙여쓴다.
   - `www.example.com`
     - 도메인의 계층 구조는 오른쪽부터 왼쪽으로 내려간다.
     - 가장 오른쪽 레이블인 `com`은 **최상위 도메인**을 의미
     - 레이블 `example`은 `com`의 서브 도메인
     - `www`은 `example.com`의 서브 도메인
     - 서브 도메인은 127단계까지 가능
     - 각 레이블은 최대 63개 문자를, 전체는 253개 문자를 사용할 수 있다.
     - 사용 가능한 문자는 영어 대소문자, 숫자, 하이픈(-)이다.  단, 하이픈으로 시작하거나 끝낼 수 없다.
       - 이 규칙을 LDH규칙이라고 한다.(letter(문자), digit(숫자), hyphen(하이픈))
4. DNS 서버
   - 역할 : 도메인에 속해 있는 컴퓨터들의 이름을 관리하고, 외부에 해당 컴퓨터의 IP주소를 알려줌.

| 호스트명 |             운영기관             |   위치    | IPv4/IPv6 지원 |
| :------: | :------------------------------: | :-------: | :------------: |
| b.dns.kr |                KT                | 서울 혜화 |      IPv4      |
| c.dns.kr |              LG U+               | 경기 안양 |      IPv4      |
| d.dns.kr | ISC(Internet Systems Consortium) |   미국    |      IPv4      |
|          |               KINX               | 서울 도곡 |   IPv4/IPv6    |
|          |             드림라인             | 서울 삼성 |      IPv4      |
|          |                KT                | 경기 성남 |      IPv4      |
| e.dns.kr |  한국과학기술정보연구원(KISTI)   |   대전    |   IPv4/IPv6    |
|          |              CNNIC               |   중국    |      IPv4      |
|          |           Registro.br            |  브라질   |   IPv4/IPv6    |
|          |            세종텔레콤            | 서울 역삼 |      IPv4      |
| f.dns.kr |           SK브로드밴드           | 서울 동작 |      IPv4      |
| g.dns.kr |      한국인터넷진흥원(KISA)      | 서울 서초 |   IPv4/IPv6    |
|          |              DENIC               |   독일    |   IPv4/IPv6    |
|          |      한국인터넷진흥원(KISA)      | 서울 서초 |      IPv4      |



## 3. Round Robin DNS

> round robin : 모든 순서가 차례대로 계속되고 다시 첫 번째 것이 기회를 갖게 됨. 즉, 분류된 모든 큐에 각각 기회를 차례로 주어 공정하게 기회를 갖게 하는 방식



### 1. 로드 밸런싱

![Round robin DNS](https://t1.daumcdn.net/cfile/tistory/2413C14E590B4F8A3A)

1. 탄생 배경
   1. 웹 사이트에 많은 사람들이 접속하면서 1대의 서버가 트래픽을 감당할 수 없게됨.
   2. 처음에는 DB 서버를 분리했으나 그마저도 서버의 부하를 감당할 수 없게됨
2. 로드 밸런싱의 기능
   1. 다수의 사용자가 사용
   2. 로드 밸런싱을 통해 다수의 서버가 부하(load)를 나눠가지게 됨.
3. 로드 밸런싱의 방법
   1. Round robin DNS
   2. L4를 이용한 로드밸런싱 : https://medium.com/@pakss328/%EB%A1%9C%EB%93%9C%EB%B0%B8%EB%9F%B0%EC%84%9C%EB%9E%80-l4-l7-501fd904cf05

위키백과 : https://ko.wikipedia.org/wiki/%EB%B6%80%ED%95%98%EB%B6%84%EC%82%B0



### 2. Round robin DNS 정의

![](https://t1.daumcdn.net/cfile/tistory/26667D4E590B5F5E32)

- 별도의 소프트웨어나 하드웨어 로드밸런싱 장비를 사용하지 않고 DNS만을 이용하여 도메인 레코드 정보를 조회할 때 트래픽을 분산하는 기법이다.
- 클라이언트의 웹서버의 IP를 요청을 받을 때마다 동일하게 설정한 웹서버를 번갈아가면서 서비스를 실시하는 방식
- 단순한 도메인에 IP 리스트만 돌리며 분산 접속시키는 방식이다.
- 장점
  - 비용 절감
  - 별도의 장비가 필요없음
- 단점
  - 1대의 서버가 문제가 생겨도 부하를 분산하기 때문에 원인을 찾기 힘들다.
  - 부하의 분산이 고르지 않음
- 구축 방법 : https://www.youtube.com/watch?v=7eV9T_NkCz0



위키백과 : https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C

한국 인터넷 정보 센터 : https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/jsp/resources/domainInfo/domainInfo.jsp

Round robin DNS : https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/

https://en.wikipedia.org/wiki/Round-robin_DNS