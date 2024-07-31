# Coding-Test
코딩 테스트 연습 Repository
## Run
```
$ ./run.sh [problem_number] [operation] [input_file] [output_file]
```
## Args
- `problem_number`: 경로와 확장자를 제외한 문제 번호. Problem 디렉토리 내 .py 파일 이름과 일치. (필수)
- `operation`: 수행할 작업, test 또는 end.
  - `test`: 문제 스크립트를 실행하고, 예상 결과와 출력 비교.
  - `end`: 테스트 세션 종료 또는 작업 완료 표시. (필수)
- `input_file`: 테스트 케이스를 포함한 입력 파일 경로. (기본값: "./input.txt")
- `output_file`: 출력 결과를 저장할 파일 경로. (기본값: "./output.txt")
## Description
- 문제 풀이 정보를 기록하여 `./problem_statistics.csv`에 자동 저장
  - `$ ./run.sh 7576 test`
    ```
    Problem Name,Start Solving,End Solving,Trial,Correct
    Problem/baekjoon/BFS/7576,2024-07-31 23:51:05,2024-07-31 23:51:05,1,1
    ```
  - `$ python run.py -p baekjoon/7576 -c`
    ```
    Problem Name,Start Solving,End Solving,Trial,Correct
    Problem/baekjoon/BFS/7576,2024-07-31 23:51:05,2024-07-31 23:51:45,6,1
    ```
- `input.txt`에는 test case를 `-`로 구분해 여러 개 입력 가능 (백준과 유사)
  - `-`만으로 구분하기 때문에 엔터가 들어가도 상관없음   
  ```
  1 2 5
  
  -
  324 42 3
  ```
- `output.txt`에는 `input.txt`에 존재하는 모든 case에 대해 결과를 저장
  ```
  ********* Case 1 *********
  8
  ********* Case 2 *********
  -1
  ```
