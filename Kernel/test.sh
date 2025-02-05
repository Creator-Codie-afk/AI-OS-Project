#!/bin/bash

# Compile the main.c file
gcc main.c -o kernel

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Running the kernel..."
    # Run the compiled kernel
    ./kernel
else
    echo "Compilation failed."
fi
