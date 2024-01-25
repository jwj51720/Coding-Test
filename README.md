# Coding-Test
코딩 테스트 연습 Repository
## Run
```
$ python run.py
```
## Args
-  `--problem`, `-p`: 풀이 py 파일의 경로 (Default: "./test.py") 
-  `--input`, `-i`: 문제의 입력 예시를 넣을 txt 파일의 경로 (Default: "./input.txt")
-  `--output`, `-o`: 문제의 출력을 저장할 txt 파일의 경로 (Default: "./output.txt")
-  `--correct`, `-c`: 문제를 맞은 것으로 표시하기
## Description
- 문제 풀이 정보를 기록하여 `./problem_statistics.csv`에 자동 저장
  - `$ python run.py -p baekjoon/7576`
    ```
    Problem Name,Start Solving,End Solving,Trial,Correct
    baekjoon/7576,2024-01-25 00:21:09,2024-01-25 00:41:39,41,0
    ```
  - `$ python run.py -p baekjoon/7576 -c`
    ```
    Problem Name,Start Solving,End Solving,Trial,Correct
    baekjoon/7576,2024-01-25 00:21:09,2024-01-25 00:41:39,41,1
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
