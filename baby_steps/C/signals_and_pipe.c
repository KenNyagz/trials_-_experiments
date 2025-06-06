#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

#define BUFFER_SIZE 100

int pipefd[2]; /*Glabal variable to hold the pipe file descriptors*/

/**
*sigint_handler - handles SIGINT signal
*@sig: signal id
*Description: handles signal interupt from user
*Return: nothing
*/

void sigint_handler(int sig)
{
    char buffer[BUFFER_SIZE];
    /*Read data from read end of the pipe*/
    read(pipefd[0], buffer, BUFFER_SIZE);
    printf("Recieved from child: %s\n", buffer);

    exit(0);
}

int main(void)
{
    pid_t pid;
    char message[] = "This is the child process";

    /*Create pipe*/
    if (pipe(pipefd) == -1)
    {
        perror("Pipe creation error");
        exit(EXIT_FAILURE);
    }

    /*Set up SIGINT signal handler*/
    signal(SIGINT, sigint_handler);

    pid = fork(); /*Create a child process*/

    if (pid < 0) {
        perror("Forking error");
        exit(EXIT_FAILURE);
    }
    else if (pid == 0)  /*Inside the child process*/
    {
        close(pipefd[0]); /*Close read end of pipe*/

        /*Write to the pipe*/
        write(pipefd[1], message, strlen(message) + 1);
        close(pipefd[1]);

        /*Send SIGINT to parent process to terminate*/
        kill(getppid(), SIGINT);
        exit(0);
    }
    else
    {
        close(pipefd[1]);

        while (1)
        {
            pause();
        }
    }
    return (0);
}
