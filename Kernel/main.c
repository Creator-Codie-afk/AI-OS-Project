#include <stdio.h>
#include <stdlib.h>

#define MAX_PROCESSES 10

// Process structure
struct Process {
    int pid;
    int state; // 0: ready, 1: running, 2: terminated
};

// Process table
struct Process process_table[MAX_PROCESSES];

// Function to create a new process
void create_process(int pid) {
    if (pid < 0 || pid >= MAX_PROCESSES) {
        printf("Invalid PID.\n");
        return;
    }
    process_table[pid].pid = pid;
    process_table[pid].state = 0; // ready
    printf("Process %d created.\n", pid);
}

// Function to schedule a process
void schedule_process(int pid) {
    if (pid < 0 || pid >= MAX_PROCESSES || process_table[pid].state == 2) {
        printf("Invalid PID or process terminated.\n");
        return;
    }
    process_table[pid].state = 1; // running
    printf("Process %d scheduled.\n", pid);
}

// Function to terminate a process
void terminate_process(int pid) {
    if (pid < 0 || pid >= MAX_PROCESSES || process_table[pid].state == 2) {
        printf("Invalid PID or process already terminated.\n");
        return;
    }
    process_table[pid].state = 2; // terminated
    printf("Process %d terminated.\n", pid);
}

int main() {
    // Initialize process table
    for (int i = 0; i < MAX_PROCESSES; i++) {
        process_table[i].pid = -1;
        process_table[i].state = 2; // terminated
    }

    // Create and schedule processes
    create_process(0);
    create_process(1);
    schedule_process(0);
    schedule_process(1);
    terminate_process(0);
    terminate_process(1);

    return 0;
}
