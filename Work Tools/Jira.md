# Jira

> 애자일 소프트웨어 개발을 위한 이슈 추적 시스템으로 버그 추적, 이슈 추적, 프로젝트 관리 기능을 제공한다.



**애자일 모델**

기존의 폭포수 모델은 프로젝트 규모가 커지면 요구사항 변화에 대한 유연한 대처가 어려웠는데, 이러한 한계점을 극복하기 위해 애자일 모델이 등장하게 되었다.

- 애자일 방법론을 도와주는 대표적인 소프트웨어 툴
  - `Jira`
  - `Trello`
  - `Redmine`



**스크럼**

스크럼은 익스트림 프로그래밍, 칸반(Kanban) 등 애자일 모델의 여러가지 방법론 중 하나이다.

- Scrum의 특성
  - 솔루션에 포함할 기능 / 개선점에 대한 우선 순위를 부여한다.
  - 개발 주기는 30일 정도로 조절하고 개발 주기마다 실제 동작할 수 있는 결과를 제공하라.
  - 개발 주기마다 적용할 기능이나 개선에 대한 목록을 제공하라.
  - 날마다 15분 정도 회의를 가져라.
  - 항상 팀 단위로 생각하라.
  - 원활한 의사소통을 위하여, 구분 없는 열린 공간을 유지하라.
  
  

**DevOps**

소프트웨어의 개발(Development)과 운영(Operations)의 합성어로서, 소프트웨어 개발자와 정보기술 전문가 간의 소통, 협업 및 통합을 강조하는 개발 환경이나 문화

- DevOps를 잘 수행하기 위해 필요한 조건
  - tool을 이용한 반복적인 작업의 자동화
  - 팀원 모두가 알고 있는 하나의 공유된 지표 필요
  - 장애/이슈 발생 시 팀원들과 공유 필요

이러한 맥락에서 등장한 tool 중 하나가 `Jira`이다.



### JIRA

 **KEYWORD**

 - 스프린트(Sprint) : 일정한 주기를 바탕으로 반복되는 개발 주기
 - 이슈(Issues) : 제품에 관해 회사에서 대화의 대상이 되는 거의 모든 것
- 이슈의 3가지 카테고리: `Task`, `Bug`, `Story`

| Issue Type | 설명                                                         | 예시                                                    |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| Epic       | 최상위 수준의 기능/작업 단위 (프로젝트 전반 또는 여러 Sprint에 걸쳐 진행할 정도의 범위) | 회원 관리, 로그인 관리                                  |
| Story      | epic에 대한 하위 Level 수준의 기능/작업 단위                 | 회원 가입, 회원 정보 수정, 회원 탈퇴, 로그인, 비번 찾기 |
| Bug        | 프로젝트 개발/검증 중 발견도니 버그                          | 상품 검색 시 특정 상품이 조회되지 않는 문제             |
| Task       | 개발에 직접 해당되지는 않으나 Sprint 안에 포함하여 해야 할 일 | ERD 작성, 테스트케이스 작성                             |
| Sub-task   | 위 Issue들과 관련하여 세부 단위 작업 등이 필요할 때 등록     |                                                         |



#### 사용법

- 스프린트 만들기
  - 프로젝트를 시작하고 스프린트를 설정한다.
  - `Backlog` 메뉴에서 `스프린트 만들기`를 클릭한다.



- 스프린트에 이슈 등록

  - 스프린트에서 이슈를 등록한다.
  - `summary`와 `description`을 잘 작성하도록 한다.

  

- 스프린트 시작
  - 스프린트에 이슈가 1개 이상 있으면 스프린트를 시작할 수 있다.
  - 중요
    - 스프린트 주기
    - 시작날짜
    - 종료날짜
    - 스프린트 목표



- 백로그에 이슈 등록
  - 스프린트를 시작한 이후 이슈를 등록해야하는 경우, 백로그에서 이슈를 생성하여 등록할 수 있다.
  - 백로그에만 이슈를 등록하면 활성 스프린트 보드에는 표시가 안된다.

    - 이런 경우, 해당 이슈를 등록할 때 스프린트에 현재 스프린트를 선택해준다!



## JQL(Jira Query Language)

Jira Issue를 구조적으로 **검색**하기 위해 제공하는 언어

- SQL(Standard Query Language)와 비슷한 문법
- Jira의 각 필드들에 맞는 특수한 예약어 제공
- 쌓인 Issue들을 재가공해 유의미한 데이터를 도출해 내는데 활용 (Gadget, Agile Board 등)



1. JQL Operators

   - =, !=, >, >=
   - in, not in
   - ~ (contains), !~ (not contains)
   - is empty, is not empty, is null, is not null
   - was, was in, was not in
   - changed (from xxx to xxx)

   

2. Relatvie Dates

   - 상대적 날짜값을 사용할 수도 있다.

     - 1d, 2d, 3d
     - -1d, -2d, -3d
     - 1w, 2w
     - -1w, -2w

     

3. JQL Keywords

   - AND
   - OR
   - NOT
   - EMPTY
   - NULL
   - ORDER BY (DESC, ASC)

   

4. JQL Funcionts

   - endOfDay(), startOfDay()
     - 오늘 24시, 오늘 00시
   - endOfWeek(), startOfWeek()

     - Saturday, Sunday

   - endOfMonth(), startOfMonth(), endOfYear(), startOfYear()

   - currentLogin()

   - currnetUser()

   - updatedBy(user, dateFrom(optional), dateTo(optional))