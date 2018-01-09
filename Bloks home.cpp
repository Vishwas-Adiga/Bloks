#include "C:\Python27\include\Python.h"
#include <iostream>
#include <conio.h>
#include <process.h>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include <stdlib.h>


using namespace std;

int main(){
    //system("python home.py");
    FILE *fd = fopen("home.py", "r");
    PyRun_SimpleFileEx(fd, "home.py", 0);
    cout << "Opening pytest";
    getch();

return 0;
}
