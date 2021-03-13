#include <charconv>
#include <string>
#include <iostream>


int main(int argc, char** argv)
{
   std::string s("42");
   int value;
   auto result = std::from_chars(&s[0], &s[0] + s.length(), value);

   std::cout << "You got " << value << std::endl;
   return 0;
}
