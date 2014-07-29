#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
   int a[10];
   vector<int> ji,ou;
   vector<int>::iterator it;

    while(1)
    {
        ji.clear();
        ou.clear();
        for(int i=0;i<10;i++)
        {
            cin>>a[i];
        }
        for(int j=0;j<10;j++)
        {
            if(a[j]%2==0)
            {
                ou.push_back(a[j]);
            }
            else
            {
                ji.push_back(a[j]);
            }
            sort(ji.begin(),ji.end());
            sort(ou.begin(),ou.end());
        }
         //cout<<ou.size()<<"ou"<<endl;
         //cout<<ji.size()<<"ji"<<endl;

        if(ji.size()>ou.size())
        {
            int k;
            for(k=0;k<ji.size();k++)
            {
                if(k==ji.size()-1)
                {
                    cout<<ji[k];
                }
                else
                {
                cout<<ji[k]<<" ";
                //cout<<ji[k]<<"==========";
                if(k<(ou.size()))
                {
                    cout<<ou[k]<<" ";
                }
                else
                {
                    cout<<"0 ";
                }
                }
            }
            //cout<<ji[k]<<" ";
        }
        if(ji.size()==ou.size())
        {
            int k;
            for(k=0;k<ji.size();k++)
            {
                if(k==ji.size()-1)
                {
                    cout<<ji[k]<<" ";
                    cout<<ou[k];
                }
                else
                {
                cout<<ji[k]<<" ";
                cout<<ou[k]<<" ";
                }
            }
            //cout<<ji[k]<<" ";
        }
        if(ji.size()<ou.size())
        {
            int k;
            for(k=0;k<ou.size();k++)
            {
                if(k<(ji.size()))
                {
                    cout<<ji[k]<<" ";
                }
                else
                {
                    cout<<"0 ";
                }
                if(k==(ou.size()-1))
                 {cout<<ou[k];}
                 else
                    {cout<<ou[k]<<" ";}
            }

            //cout<<ou[k]<<" ";
        }
    }

    return 0;
}
