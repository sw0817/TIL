## 1. RR 스케줄링

### 라운드 로빈 스케줄링(Round Robin Scheduling, RR)

![](https://t1.daumcdn.net/cfile/tistory/9917AA435C42D5D728))



![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Round_Robin_Schedule_Example.jpg/1024px-Round_Robin_Schedule_Example.jpg)

1. 시분할 시스템을 위해 설계된 선점형 스케줄링
2. 컴퓨터 자원을 사용할 수 있는 기회를 프로그램의 프로세스들에게 공정하게 부여하기 위한 방법
3. 각 프로세스에 일정시간을 할당하고, 할당된 시간이 지나면 그 프로세스는 잠시 보류한 뒤 다른 프로세스에게 기회를 주는 방식
4. 프로세스 사이에 우선 순위가 없음.
5. 문맥 전환의 오버헤드가 큼
   1. 오버헤드 : 어떤 처리를 하기 위해 들어가는 간접적인 처리시간이나 메모리 등
6. 응답시간이 짧다는 장점 덕분에 실시간 시스템에 유리
7. 각 프로세스에 할당되는 시간이 큰 경우에는 비선점 FIFO와 같아짐
8. 반환시간 & 대기시간
   1. 반환 시간 = 작업완료시간 - 도착시간
   2. 대기시간 = 마지막 작업 시작시간 - 이미 처리한 시간 - 도착시간

예제1) 라운드로빈 정책을 사용하여 스케줄링 할 경우 평균 반환시간을 계산한 결과로 옳은 것은? (단, 작업할당 시간은 4시간으로 한다.)

| 프로세스 |  A   |  B   |  C   |
| :------: | :--: | :--: | :--: |
| 실행시간 |  17  |  4   |  5   |

답)

|  A   |  B   |  C   |  A   |  C   |  A   |  A   |  A   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  4   |  8   |  12  |  16  |  17  |  21  |  25  |  26  |

A: 26-0=26 / B: 8-0=8 /C: 17-0=17

평균: (26+8+17)/3 = 17 



예제2) 라운드로빈 정책을 사용하여 스케줄링 할 경우 평균 반환시간을 계산한 결과로 옳은 것은? (단, 작업할당 시간은 4시간으로 한다.)

| 작업  | 제출시간 | 실행시간 |
| :---: | :------: | :------: |
| Task1 |    0     |    8     |
| Task2 |    1     |    4     |
| Task3 |    2     |    9     |
| Task4 |    3     |    5     |



## 2. 다단계 큐 스케줄링(MQ)

### 1. 다단계 큐 스케줄링

1. 정적 우선순위를 사용하는 스케줄링을 구현할 때 적합한 자료구조
2. 동작 원리
   1. 서로 다른 우선순위의 프로세스들을 구별하고 관리하기 위해 우선순위의 개수만큼 큐가 필요함.
   2. 프로세스들은 자신의 우선순위 값에 해당하는 큐에 들어감. 이 때 정적 우선순위 이므로 큐들 간에 프로세스의 이동이 불가능하다.
   3. 프로세스가 특정 그룹의 준비상태 큐에 들어갈 경우 다른 준비상태 큐로 이동할 수 없다.
   4. 하위 준비 상태 큐에 있는 프로세스를 실행하는 도중이라도 상위 준비 상태 큐에 프로세스가 들어오면 상위 프로세스에게 CPU를 뺏기는 선점 방식.



### 2. 다단계 피드백 큐 스케줄링

![](https://t1.daumcdn.net/cfile/tistory/2562294456EA1BBE0C)

1. 다단계 큐 스케줄링에서 CPU를 포함한 전체 자원들의 활용도를 높여 시스템의 성능을 높일 수 있는 기법, 짧은 작업에 유리
2. 짧은 연산 후 입출력을 발생하면 CPU는 다른 프로세스가 선점하게 되고 이때부터 입출력 작업과 CPU 연산이 병행하면서 진행됨.
4. 동작 원리
   1. 우선순위 개수만큼 여러 단계의 큐가 있고 각 단계마다 서로 다른 CPU 시간 할당량을 가짐.
   2. 여기서 우선순위가 높은 큐일수록 시간 할당량이 작음.
   3. 새로운 프로세스는 최상위 단계의 준비 큐에 들어간 후 FCFS의 순서로 CPU를 할당받아 실행됨.
   4. 시간 할당량이 끝나면 한 단계 아래의 준비 큐에 들어감. (우선순위가 한 단계 낮아짐.)
   5. 마지막 단계에서는 더 내려갈 단계가 없으므로 라운드 로빈 방식으로 실행된다.





## 3. 프로세스의 생성과 소멸

review) 프로세스 : 메인 메모리에서 실행 중인 프로그램!

![](https://gmlwjd9405.github.io/images/os-process-and-thread/process.png)

- 프로세스는 실행될 때 각각 독립된 메모리 영역(code, Data, Stack, Heap)을 할당받음

![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTZfMjgw/MDAxNTYwNjcyOTMwODAw.Uy5UuxOwdRO-d9BMy2h0G-erqsih5gM9Sk1TE7P48WUg.x2OtIO9H0no2ardUIxqrI4yN6OHB1jSXcW6drZF3srwg.PNG.jwyoon25/image.png?type=w800)

- 프로세스 스케줄러
  - 둘 이상의 프로세스가 적절히 실행되도록 컨트롤하는 요소



![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTZfNzUg/MDAxNTYwNjc1MjY4MDg0.oHOI_VKm1L3LmIRrDfL_1atq_e86LFfDZ_i9OxywRXQg.1Py3vJ2_7rgxWsj9BqchrmFvmUAn-L21E3hE5bd8juMg.PNG.jwyoon25/image.png?type=w800)

1. S와 E는 각각 Start, End를 의미
2. Running 상태
   1. CPU에 의해 현재 실행중인 상태
3. Ready 상태
   1. 실행을 위한 준비를 끝낸 상태
   2. 스케쥴러의 선택을 기다린다는 의미
4. Blocked 상태
   1. I/O연산중인 프로세스
   2. 연산이 끝나면 Ready 상태로 변경됨.
   3. I/O연산 : 사칙 연산이나 프로그램의 실행 등의 일반적인 연산은 CPU에 의존적이나 I/O연산은 상대적으로 의존도가 낮음 -> 다른 연산과 병행될 수 있음. -> I/O연산 중 만약 Ready 상태이면 스케쥴러에 의해 선택되고 Context Switching 낭비가 됨 -> Blocked상태를 사용하여 이를 해결

- Context Switching : A, B프로세스가 있다고 가정, B프로세스가 실행 중일 때 A를 실행시키려면 B 실행 중 register set에 담긴 정보를 별도의 DB로 옮겨 놓고 B를 ready 상태로 만든다. 그 후 A의 정보를 resister set에 복원 후 A를 running 상태로 만드는 작업.

### 1. 생성

1. 바탕화면에서 실행파일을 더블클릭
2. 프로그램 상에서 프로그래밍을 통해 프로세스를 실행



1. 프로세스 생성 함수

```c++
BOOL CreateProcess(
    LPCTSTR lpApplicationName,    // 생성될 프로세스의 이름
    LPTSTR lpCommandLine,         // 생성될 프로세스에 인자 전달
    LPSECURITY_ATTRIBUTES lpProcessAttributes, // 프로세스의 보안 속성 지정
    LPSECURITY_ATTRIBUTES lpThreadAttributes,   // 쓰레드의 보안 속성 지정
    BOOL bInheritHandles,	// TRUE : 부모 프로세스가 소유하는 상속 가능한 핸들을 상속한다.
    DWORD dwCreationFlags,	// 생성하는 프로세스의 특성을 결정짓는 옵션(우선순위)
    LPVOID lpEnvironment,	// 생성하는 프로세스의 Environment Block 지정
                            // NULL : 부모 프로세스의 환경 블록 복사
    LPCTSTR lpCurrentDirectory,	// 생성하는 프로세스의 현재 디렉터리 설정
                                // NULL : 부모 프로세스의 현재 디렉터리
    LPSTARTUPINFO lpStartupInfo,	// STARTUPINFO 구조체 변수 초기화한 후
                                	// 변수의 포인터를 인자로 전달
    LPPROCESS_INFORMATION lpProcessInformation	//생성하는 프로세스의 정보를 얻기 위한 인자
						 //PROCESS_INFORMATION 구조체 변수의 주소값을 인자로 전달
);
```

1. CreateProcess 함수를 호출하기 위해서는 LPSTARTUPINFO와 LPPROCESS_INFORMATION 구조체를 선언해야 한다.
2. LPSTARTUPINFO에 실행하고자 하는 프로세스의 특성 정보를 담아서 매개변수로 넘겨주면 CreateProcess 함수는 요구사항에 맞게 프로세스를 생성해준다.
3. 생성된 프로세스에 대한 정보를 리턴해주는면 이를 LPPROCESS_INFORMATION를 선언하고 매개변수로 넘겨서 받아야한다.
4. 프로세스를 생성하는 프로세스가 부모 프로세스이고, 이 부모 프로세스에 의해 생성된 프로세스를 자식 프로세스라고 한다.
5. LPCTSTR은 실행파일의 이름, LPTSTR은 main함수의 매개변수

https://m.blog.naver.com/PostView.nhn?blogId=jwyoon25&logNo=221563629786&proxyReferer=https:%2F%2Fwww.google.com%2F

![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTdfMTA0/MDAxNTYwNjk4MTA5MTMz.PyV2_cvK2aHDxIDqrOr0Ee5nQoCxw_6uevuKfWaemqQg.alOJaftbBC73cztLhj6wHJO4M91qfrM5IiggGePx7Ykg.JPEG.jwyoon25/47.JPG?type=w800)

```c++
// AdderProcess.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
// 메인함수의 전달인자를 뎃셈하는 프로그램

int _tmain(int argc, TCHAR* argv[])
{
DWORD val1, val2;
val1 = _ttoi(argv[1]);
val2 = _ttoi(argv[2]);

_tprintf(_T("%d + %d = %d \n"), val1, val2, val1 + val2);

_gettchar();
return 0;
}
```



```c++
// CreateProcess.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다. 
// 

#define DIR_LEN MAX_PATH+1 

int _tmain(int argc, TCHAR* argv[]) 
{ 

STARTUPINFO si = { 0, };  // 구조체 변수 선언 및 초기화
PROCESS_INFORMATION pi;  

si.cb = sizeof(si); // 구조체 변수의 크기를 나타내는 멤버변수 cb초기화 
si.dwFlags = STARTF_USEPOSITION | STARTF_USESIZE;  // Flag지정 (내가 지정한 값만 참고하여 설정할 수 있도록 하는 것. ) 즉, 바로 밑 4줄인 x,y좌표와 프로세스 윈도우 가로,세로 길이값 참고를 위해 사용하는 Flag.
si.dwX = 100;  // 프로세스 x좌표
si.dwY = 200;  // 프로세스 y좌표
si.dwXSize = 300;  // 프로세스 윈도우의 가로 길이
si.dwYSize = 200;  // 프로세스 윈도우의 세로 길이 
si.lpTitle = _T("I am a boy!");  


TCHAR command[] = _T("AdderProcess.exe 10 20");  // 실행파일 명과 매개변수를 선언한 것. 실행파일 명은 위에서 만든것과 이름이 같아야 한다. 
TCHAR cDir[DIR_LEN]; 
BOOL state; 

GetCurrentDirectory(DIR_LEN, cDir);  // 현재 디렉터리 확인 
_fputts(cDir, stdout); 
_fputts(_T("\n"), stdout); 

SetCurrentDirectory(_T("C:\\WinSystem"));  // 현재 디렉터리를 c:\\WinSystem으로 변경하는 코드 

GetCurrentDirectory(DIR_LEN, cDir);  // 현재 디렉터리 확인
_fputts(cDir, stdout); 
_fputts(_T("\n"), stdout); 

state = CreateProcess(  // 프로세스 생성
NULL, 
command, // 메인함수에 전달될 문자열 
NULL, NULL, TRUE, 
CREATE_NEW_CONSOLE, 
NULL, NULL, &si, &pi 
); 

if (state != 0) 
_fputts(_T("Creation OK! \n"), stdout); 
else 
_fputts(_T("Creation Error! \n"), stdout); 

return 0; 
} 
```

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdluXAL%2Fbtquc2WhjdB%2F9EGatfAqRwTPS53qYjA3Pk%2Fimg.png)

### 2. 소멸

1. exit() system call : 해당 프로세스가 가졌던 모든 자원은 OS에게 반환(메모리, 파일, 입출력장치 등)

## 4. 쓰레드(Thread)

> 프로그램 내부의 흐름, 맥

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiTxyb%2Fbtqw7dgmVR5%2F6MOlKMNKS4zM0KwUAcCSl1%2Fimg.jpg)

1. Tread : 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말한다. 일반적으로 한 프로그램은 하나의 쓰레드를 가지고 있지만, 프로그램 환경에 따라 둘 이상의 쓰레드를 동시에 실행할 수 있다.

2. Multi Tread

   1. 하나의 프로그램에 맥이 2개 이상 있는 것
   5. 위의 그림에서 각 쓰레드는 코드와 데이터를 공유하고 스택은 공유하지 않는다
   3. 장점
      1. 사용자 응답성 증가
      2. 프로세스 자원과 메모리 공유 가능
      3. 경제성이 좋음(프로세스 context switching보다 Thread context switching이 오버헤드가 더 적다.)
         - IPC(Inter Process Communication) : 프로세스들 사이에 서로 데이터를 주고받는 행위 또는 그에 대한 방법이나 경로
      4. 다중 처리로 성능과 효율 향상
         - 멀티 프로세스는 프로세스 간의 context switching 시 단순히 CPU 레지스터 교체 뿐만 아니라 RAM과 CPU 사이의 캐시 메모리에 대한 데이터까지 초기화되므로 오버헤드가 크기 때문
         - 쓰레드는 프로세스 내의 메모리를 공유하기 때문에 독립적인 프로세스와 달리 데이터를 주고받는 것이 간단해지고 시스템 자원 소모가 줄어든다.
         - 멀티 쓰레드는 context switching 시 stack영역만 처리하기 때문에 전환 속도가 빠름.
   4. 단점
      1. 쓰레드를 많이 생성하면, context switching이 많이 일어나서 성능 저하
      2. 쓰레드 중 한 스레드만 문제가 있어도, 전체 프로세스가 영향 받음

   

   **멀티 태스킹 vs 멀티 프로세싱 vs 멀티 쓰레드**

   - 멀티 태스킹

     \- cpu가 하나 있는데, 하나의 cpu가 수시로 프로세스를 변경하면서 프로그램을 실행하는 것 이다. (결과적으로 사람의 눈에는 모든 프로세스가 동시에 실행되는 것 처럼 보임)

     - 하나의 cpu가 여러 프로세스를 번갈아 가면서 실행

   - 멀티 프로세싱

     \- 하나의 프로세스를 여러개의 cpu를 사용해서 실행 시키는 행위

     - 여러 cpu여러 프로세스를 병랭실행해서 속도를 높인다.

   - 멀티 쓰레드

     \- 쓰레드를 여러 개 만들어, 멀티 코어를 통해 활용도를 높임

     - 실행속도 향상에 도움이 된다.