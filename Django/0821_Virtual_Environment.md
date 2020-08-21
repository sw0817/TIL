# 0821 가상환경

### Virtual Environment

- 파이썬 인터프리터, 라이브러리 및 스크립트가 **"시스템 파이썬(글로벌 환경)"**(즉, 운영 체제 일부로 설치되어있는 것)에 설치된 모든 라이브러리와 격리 되어있는 파이썬 환경
- 각 가상 환경은 **고유한 파이썬 환경**을 가지며 **독립적**으로 격리되어 설치된 패키지 집합을 가짐
- 대표적인 가상 환경 지원 시스템
  - **venv**, virtualenv, conda, pyenv(mac OS)
  - 파이썬 3.3 부터 venv가 기본 모듈로 내장

- 사용하는 이유
  - pip로 설치한 패키지들은 Lib/site-packages안에 저장되는데 이는 모든 파이썬 스크립트에서 사용할 수 있다.
  - 그런데 여러 프로젝트를 진행하게 되면 프로젝트 마다 다른 버전의 라이브러리가 필요할 수도 있는데 파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능하다.
  - 더불어 각 라이브러리나 모듈은 서로에 대한 의존성(dependency)이 다르기 때문에 알 수 없는 충돌이 발생하거나 다른 여러 문제를 일으킬 수 있게 된다.

---

### 가상 환경 명령어

- 가상 환경 만들기
  - python -m venv 가상환경이름(venv)        - python 3.7.2 이상에서 사용 가능
- 활성화
  - Windows(git bash) : 가상환경이름\Scripts\activate       - 앞에 사실 소스가 붙어야 함
  - macOS : 가상환경이름/bin/activate
- 비활성화
  - deactivate

---

### 패키지 관리

- pip freeze
  - 현재 환경에 설치된 패키지를 requirements format으로 출력
  - 각 패키지들은 대소문자를 구분하지 않는 순서로 나열
- 패키지 요구사항 파일 생성 (1)
  - pip freeze > requirements.txt                > : redirect
- 패키지 요구사항 설치 (2) - 받는 입장
  - pip install -re requirements.txt

---

### fixture

- Django가 데이터베이스로 import 할 수 있는 데이터 모음
- 앱을 처음 설정할 때 데이터베이스를 미리 채워야 하는 상황이 존재하는데 이러한 초기 데이터(initial data)를 제공하는 방법 중 하나

####  fixture 출력 및 로드

- dumpdata
  - 특정 앱의 관련된 데이터베이스의 모든 데이터를 출력
- loaddata
  - dumpdata를 통해 만들어진 fixtures 파일을 데이터베이스에 import
  - fixtures 파일은 반드시 app 디렉토리 안에 fixtures 디렉토리에 위치

#### dumpdata usage

- 명령어
  - python manage.py dumpdata app_name.ModelName [--options]
- 사용 예시
  - python manage.py dumpdata articles.Article --indent 4 > articles.json

#### loaddata usage

- 명령어

  - python manage.py loaddata fixtures_path

- 사용 예시

  - python manage.py loaddata articles/articles.json    

     - 클론 받고, 서버켜서 db를 만들고 마이그레이션까지는 미리 해야함