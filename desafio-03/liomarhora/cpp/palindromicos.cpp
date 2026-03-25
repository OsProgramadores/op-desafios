#include <iostream>
#include <string>
#include <cstring>


int main()
{
	std::string converter, numero_inverso;
	
	for(int i = 9; i <= 100000;  i++)
	{
		converter = std::to_string(i);
				
		if(!converter.empty())
		{
			size_t convertSize = converter.length();
			int j = static_cast<int>(convertSize);
			
			for(int x = j-1; x >= 0; x--)
			{
				if(numero_inverso.empty())
				{
					numero_inverso = converter[x];
				} else {
					numero_inverso += converter[x];
				}				
			}
						
			if(converter == numero_inverso)
			{
				std::cout << "Os numeros palindromicos sao: " << converter << '\n';
			}
		}
		
		numero_inverso.erase();
		converter.erase();
	}
}
