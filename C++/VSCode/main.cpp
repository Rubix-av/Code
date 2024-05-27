#include <iostream>

int main()
{
    //declaration of variables
    int age;
    std::string name;

    std::cout<<"What's your full name? ";

    //we cannot give our full name this way, hence we need to do something else
    // std::cin>>name;

    //This will let us enter a string with spaces
    std::getline(std::cin, name);

    std::cout << "What's your age? ";
    std::cin >> age;



    std::cout << "Hello "<< name <<'\n';
    std::cout << "You are "<< age <<" years old";

    return 0;
}