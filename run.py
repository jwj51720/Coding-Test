import argparse
import subprocess
import pandas as pd
from datetime import datetime
import pytz
import os
import sys


def get_current_time():
    kst = pytz.timezone("Asia/Seoul")
    return datetime.now(kst).strftime("%Y-%m-%d %H:%M:%S")


def update_csv(problem_file, end_time, correct, update_only_correct):
    filename = "problem_statistics.csv"
    problem_name, _ = os.path.splitext(problem_file)
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=["Problem Name", "Start Solving", "End Solving", "Trial", "Correct"]
        )

    if problem_name in df["Problem Name"].values:
        if update_only_correct:
            df.loc[df["Problem Name"] == problem_name, "Correct"] = 1
        else:
            df.loc[df["Problem Name"] == problem_name, "End Solving"] = end_time
            df.loc[df["Problem Name"] == problem_name, "Trial"] += 1
    else:
        start_time = get_current_time()
        end_time = start_time
        new_row = pd.DataFrame(
            {
                "Problem Name": [problem_name],
                "Start Solving": [start_time],
                "End Solving": [end_time],
                "Trial": [1],
                "Correct": int(correct),
            }
        )
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(filename, index=False)


def run_script(problem_file, input_data, correct, update_only_correct):
    process = subprocess.Popen(
        ["python", problem_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = process.communicate(input_data)
    end_time = get_current_time() if not update_only_correct else None

    if stderr:
        print("Error:", stderr)

    update_csv(problem_file, end_time, correct, update_only_correct)

    return stdout


def process_cases(problem_file, input_file, output_file, correct, update_only_correct):
    with open(input_file, "r") as file:
        content = file.read().strip()
        cases = [case.strip() for case in content.split("-\n") if case.strip()]

    with open(output_file, "w") as file:
        for i, case in enumerate(cases):
            case_header = f"********* Case {i+1} *********"
            file.write(case_header + "\n")
            output = run_script(problem_file, case, correct, update_only_correct)
            file.write(output)


def validate_files(problem_file, input_file):
    missing_files = []
    if not os.path.exists(problem_file):
        missing_files.append(f"Problem '{problem_file}'")
    if not os.path.exists(input_file):
        missing_files.append(f"Input '{input_file}'")

    if missing_files:
        missing_files_str = ", ".join(missing_files)
        print(f"Error: {missing_files_str}를 찾을 수 없습니다.")
        sys.exit(1)


def main(args):
    validate_files(args.problem, args.input)
    process_cases(args.problem, args.input, args.output, args.correct, args.correct)
    print("Done.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Coding Test Run")
    parser.add_argument("-p", "--problem", default="./test.py", help="실행할 문제 파일")
    parser.add_argument("-i", "--input", default="./input.txt", help="input.txt 파일")
    parser.add_argument("-o", "--output", default="./output.txt", help="output.txt 파일")
    parser.add_argument("-c", "--correct", action="store_true", help="정답인 경우")
    args = parser.parse_args()
    main(args)
