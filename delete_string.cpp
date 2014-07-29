#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main()
{
    int num,pos,i;
    char *tmp;
    string str,tmp_str,final_str;

    while(cin>>str)
    {
        int i;
       for(i=0;i<str.size();i++)
       {
           if(str[i]==',')
           {
               break;
           }
       }
       tmp_str=str.substr(i+1,str.size());
       int aa;
       for(int j=0;j<tmp_str.size();j++)
       {
           if(((tmp_str[j]>='0')&&(tmp_str[j]<='9'))|((tmp_str[j]>='a')&&(tmp_str[j]<='z'))|((tmp_str[j]>='A')&&(tmp_str[j]<='Z'))|(tmp_str[j]==' '))
           {
               if(j==0)
               {
                   cout<<tmp_str[j];
                   aa=j;
               }
               else
               {
                   if(tmp_str[j]!=tmp_str[aa])
                   {
                       cout<<tmp_str[j];
                       aa=j;
                   }
               }
           }
       }

    }
    return 0;
}
