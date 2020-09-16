# 0914 Django - FORM / STATIC MEDIA



## Django Form



> Form

- Form은 django 프로젝트의 주요 유효성 검사 도구들 중 하나이며, 공격 및 우연한 데이터 손상에 대한 중요한 방어수단
- django는 Form에 관련된 작업의 아래 세 부분을 처리해줌
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



> Form Class

- django Form 관리 시스템의 핵심
- form내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러메세지를 결정
- django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여 줌



> ModelForm Class

- model을 통해 Form Class를 만들 수 있는 Helper
- 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능
- Meta Class
  - Model의 정보를 작성하는 곳
  - 해당 model에 정의한 field 정보를 Form에 적용하기 위함



> Form & ModelForm

- Form
  - 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성(cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출)
  - model에 연관되지 않은 데이터를 받을 때 사용
- ModelForm
  - django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
  - 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능



> View decorators

- decorator (데코레이터)
  - 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 '연장'하게 해주는 함수
  - django는 다양한 기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공
- Allowed HTTP methods
  - 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
  - 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed을 return
  - require_http_methods(), require_GET(), require_POST(), require_safe()   (GET보다는 safe)



## Static

> 정적 파일 (static files)

- 웹 사이트의 구성 요소 중에서 image, css, js 파일과 같이 해당 내용이 고정되어, 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 즉, 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 응답하면 되는 파일
- 기본 static 경로
  - app_name/static/





## Media

> 미디어 파일 (media files)

- 사용자가 웹에서 업로드하는 정적 파일
  - image, pdf, video 등



사진 올리려면 pip install PILLOW

pip install pilkit

pip install django-imagekit