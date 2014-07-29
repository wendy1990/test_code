#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;
struct leave
{
    int id;
    int value;
};
bool compare(leave a,leave  b)
{
    if((a.value)>=(b.value))
     {
         return true;
         }
    else
        return false;
}
vector<leave> leaves;
vector<leave>::iterator it;
int main()
{
    int height,vec,id,angle;
    while(1)
    {
        string str;
        int a1,a2;
        leave tmp;
        leaves.clear();
        while((cin>>str)&&(str!="end"))
        {
            string str3,str1,str2;

            for(int i=0;i<str.size();i++)
            {
                if(str[i]==':')
                    {
                        a1=i;
                        //cout<<i<<"11111"<<endl;
                    }
                if(str[i]==',')
                    {
                        a2=i;
                        //cout<<i<<"222222"<<endl;
                    }
            }
            //cout<<a1<<"````````````"<<a2<<endl;
            str1=str.substr(0,a1);
            str2=str.substr(a1+1,a2-(a1+1));
            str3=str.substr(a2+1,str.size()-(a2+1));
            //cout<<str1<<" "<<str2<<" "<<str3<<endl;
            if(str1=="init")
            {
                height=atoi(str2.c_str());
                vec=atoi(str3.c_str());
            }
            if(str1=="leaf")
            {
                id=atoi(str2.c_str());
                angle=atoi(str3.c_str());
                tmp.id=id;
                tmp.value=angle;
                leaves.push_back(tmp);
            }
        }
        if(height==0)
        {
            if(leaves.size()!=0)
            {
                for(it=leaves.begin();it!=leaves.end()-1;it++)
                {
                        cout<<it->id<<",";
                }
             cout<<it->id;
            }
        }
        else
        {
            sort(leaves.begin(),leaves.end(),compare);
            if(leaves.size()!=0)
            {
                for(it=leaves.begin();it!=leaves.end()-1;it++)
                    {
                        cout<<it->id<<",";
                }
                cout<<it->id;
            }
        }
    }

}
