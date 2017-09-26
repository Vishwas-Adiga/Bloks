#include <iostream>
#include <conio.h>
#include <process.h>

using namespace std;

int main(){
    system("/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Thiru/Downloads/pytest.py");
    system("/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Thiru/Downloads/pytest.py");
    cout << "Opening pytest";
    
    
    return 0;
}

/*I had to do this cause i have 3 python interpreters.. this is different on Unix like os and windows right????? But we will being doing it for Windows (i know). Just so that you know that we might need to specify the path of the interpreter. i have read that it's not need in windows.... but idk if it will work in our school*/
