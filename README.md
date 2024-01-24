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
- 문제 풀이 시에 풀이 정보를 기록하여 `./problem_statistics.csv`에 자동 저장
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
