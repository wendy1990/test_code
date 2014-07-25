#include<iostream>
#include<string>
using namespace std;
int main()
{
    string candystr;
    char candy[5][5];
    int min_candy=-1;
    cin>>candystr;
    for(int i=0;i<candystr.size();i++)
    {
        candy[i/5][i%5]=candystr[i];
    }
    /*for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
            cout<<candy[i][j]<<endl;
    }*/
    for(int i=0;i<5;i++)
    {
        if(min_candy!=-1)
        {
            break;
        }
        for(int j=0;j<5;j++)
        {
            //cout<<"---:"<<i<<"&"<<j<<endl;
            //cout<<candy[i][j];
            //j<==>j+1
            if(j+1<5)
        {
            //cout<<"1"<<endl;
            if(candy[i][j]==candy[i][j+1])
            {
                if((i-1>=0)&&(j-1>=0)&&(candy[i-1][j-1])==candy[i][j])//i-1&j-1
                {
                   // cout<<"11"<<endl;
                 min_candy=(i-1)*5+j;
                 break;
                }
                if((i-1>=0)&&(j+2<5)&&(candy[i-1][j+2])==candy[i][j])//i-1&j+2
                {
                  //  cout<<"13"<<endl;
                 min_candy=(i-1)*5+j+2+1;break;
                }
                if((i+1<5)&&(j-1>=0)&&(candy[i+1][j-1])==candy[i][j])//i+1&j-1
                {
                  //  cout<<"12"<<endl;
                 min_candy=i*5+j;break;
                }
                if((i+1<5)&&(j+2<5)&&(candy[i+1][j+2])==candy[i][j])//i+1&j+2
                {
                  //  cout<<"14"<<endl;
                 min_candy=i*5+j+2+1;break;
                }
            }
        }
        //i<==>i+1
        if (i+1<5)
        {
            //cout<<"2"<<endl;
            if(candy[i][j]==candy[i+1][j])
            {
                if((i-1>=0)&&(j-1>=0)&&(candy[i-1][j-1])==candy[i][j])//i-1&j-1
                {
                    //cout<<"21"<<endl;
                 min_candy=(i-1)*5+j;break;
                }
                if((i-1>=0)&&(j+1<5)&&(candy[i-1][j+1])==candy[i][j])//i-1&j+1
                {
                    //cout<<"22"<<endl;
                 min_candy=(i-1)*5+j+1+1;break;
                }
                if((i+2<5)&&(j-1>=0)&&(candy[i+2][j-1])==candy[i][j])//i+2&j-1
                {
                   // cout<<"23"<<endl;
                 min_candy=(i+2)*5+j;break;
                }
                if((i+2<5)&&(j+1<5)&&(candy[i+2][j+1])==candy[i][j])//i+2&j+1
                {
                   // cout<<"24"<<endl;
                 min_candy=(i+2)*5+j+1;break;
                }
            }
        }
        //i<==>i+2
        if (i+2<5)
        {
            //cout<<"4"<<endl;
            if(candy[i][j]==candy[i+2][j])
            {

                if((i+1<5)&&(j-1>=0)&&(candy[i+1][j-1])==candy[i][j])//i+1&j-1
                {
                   // cout<<"41"<<endl;
                 min_candy=(i+1)*5+j;break;
                }
                if((i+1<5)&&(j+1<5)&&(candy[i+1][j+1])==candy[i][j])//i+1&j+1
                {
                   // cout<<"42"<<endl;
                 min_candy=(i+1)*5+j+1;break;
                }
            }
        }
        //i<==>i+2
        if (j+2<5)
        {
            //cout<<"3"<<endl;
            if(candy[i][j]==candy[i][j+2])
            {
                if((j+1<5)&&(i-1>=0)&&(candy[i-1][j+1])==candy[i][j])//i-1&j+1
                {
                    // cout<<"31"<<endl;
                 min_candy=(i-1)*5+j+1+1;break;
                }
                if((i+1<5)&&(j+1<5)&&(candy[i+1][j+1])==candy[i][j])//i+1&j+1
                {
                    // cout<<"32"<<endl;
                 min_candy=i*5+j+1+1;break;
                }
            }
        }

    }
    }
    if(min_candy==-1)
    {
        cout<<"NO"<<endl;
    }
    else
    {
        cout<<"YES "<<min_candy<<endl;
    }
    return 0;
}
