#!/bin/bash

# Default file paths
INPUT_FILE="input.txt"
OUTPUT_FILE="output.txt"

# Find the problem file in the 'Problem' directory and its subdirectories.
PROBLEM_PATH=$(find Problem -type f -name "$1.py" | head -n 1)

# If the file is not found, print an error message.
if [ -z "$PROBLEM_PATH" ]; then
    echo "Error: Could not find the problem file: $1.py"
    exit 1
fi

# Set custom input and output file paths if provided
if [ ! -z "$3" ]; then
    INPUT_FILE="$3"
fi
if [ ! -z "$4" ]; then
    OUTPUT_FILE="$4"
fi

# Execute different commands based on "test" or "end".
if [ "$2" == "test" ]; then
    python run.py -p "$PROBLEM_PATH" -i "$INPUT_FILE" -o "$OUTPUT_FILE" -c
elif [ "$2" == "end" ]; then
    python run.py -p "$PROBLEM_PATH" -i "$INPUT_FILE" -o "$OUTPUT_FILE"
else
    echo "Usage: ./run_problem.sh problem_number test|end [input_file] [output_file]"
    exit 1
fi
