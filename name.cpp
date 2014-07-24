#include <iostream>
#include<map>
#include<set>
#include<vector>
#include<string>
using namespace std;

map<string,string> namemap;

int main()
{
string lady_names[]={"wang fei","zhang man yu","zhang zhi yi","li li","li xiao man","li yu cun","yang ni","xiao tong","li lei","zhang san"};
vector<set<char> >lady_name_sets;
string lady_name;
for(int i=0;i<10;i++)
 {
  lady_name=lady_names[i];
  set<char> sample_set;
  for(int j=0;j<lady_name.size();j++)
  {
   if (lady_name[j]==' ')
       continue;
   else
       sample_set.insert(lady_name[j]);
  }
  lady_name_sets.push_back(sample_set);
 }

set<char>::iterator it;
for (int m=0;m<lady_name_sets.size();m++)
 {
 cout<<m<<":\t"<<lady_names[m]<<"---";
 for(it=lady_name_sets[m].begin();it!=lady_name_sets[m].end();it++)
 {
 cout<<*it<<" ";
 }
cout<<endl;
}
string man_name;
string match_name;
int max_match;
set<char> man_name_set;
while(getline(cin,man_name))
  { man_name_set.clear();
    for(int k=0;k<man_name.size();k++)
     {if(man_name[k]==' ')
           continue;
      else
      man_name_set.insert(man_name[k]);}
 max_match=-1;
 for(int aa=0;aa<lady_name_sets.size();aa++)
  {it= man_name_set.begin();
   int tmp_match=0;
   while(it!=man_name_set.end())
     {if(lady_name_sets[aa].find(*it)!=lady_name_sets[aa].end())
      tmp_match++;
      ++it;}
   if(tmp_match>max_match)
     { max_match=tmp_match;
     match_name=lady_names[aa];}
   }
 cout<<"max_match:"<<max_match<<"---"<<match_name<<endl;
}
 return 0;
}

