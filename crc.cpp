//============================================================================
// Name        : crc.cpp
// Author      : Nishant
// Version     :
// Copyright   : public
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout<<"sender side :"<<endl;
	string msg,gen;
	int gen_len,msg_len;
	cout<<"enter the messages in the form of string : \n";
	cin>>msg;
	cout<<"enter the generator in the form of string :\n";
	cin>>gen;
	gen_len=gen.length();
	msg_len=msg.length();
	cout<<"no of 0s appended are"<<gen_len-1<<endl;
	for(int i=0;i<(gen_len-1);i++){
		msg+='0';
	}
	cout<<"messages after appending 0s are :"<<msg<<endl;
	string m=msg;
	int j=gen_len;
	while(1){
		int i=0;
		while(msg[i]=='0'){
			i++;
		}
		if(i+gen_len-1<msg_len+gen_len-1){
			for(int k=0;k<(gen_len);k++,i++){
				if(msg[i]==gen[k]){
					msg[i]='0';
				}
				else{
					msg[i]='1';
				}
			}
		}
		else{
			break;
		}
		j=i;
	}
	cout<<"crc remainder  are"<<msg<<endl;
	for(int i=msg.length(),j=0;j<gen_len-1;i--,j++){
		m[i]=msg[i];
	}
	cout<<"message transfer through the channel are "<<m<<endl;
	cout<<"Receivers  side"<<endl;
	j=gen.length();
	while(1){
		int i=0;
		while(m[i]=='0'){
			i++;
		}
		if(i+gen_len-1<msg_len+gen_len-1){
			for(int k=0;k<(gen_len);k++,i++){
				if(m[i]==gen[k]){
					m[i]='0';
				}
				else{
					m[i]='1';
				}
			}
		}
		else{
			break;
		}
		j=i;
	}
	cout<<"Remainder are :"<<m<<endl;
	bool flag;
	for(int i=0;i<m.length();i++){
		if(m[i]!='0'){
			flag=1;
		}
	}
	if(flag==1){
		cout<<"as remainder are not 0 hence "<<endl;
		cout<<"error in the code "<<endl;

	}
	else{
		cout<<"as reminder of are all 0 hence "<<endl;
		cout<<"no error in the code "<<endl;
	}
	return 0;
}
/*
 * sender side :
enter the messages in the form of string :
1011011
enter the generator in the form of string :
1101
no of 0s appended are3
messages after appending 0s are :1011011000
crc remainder  are0000000001
message transfer through the channel are 1011011001
Receivers  side
Remainder are :0000000000
as reminder of are all 0 hence
no error in the code
 *
 */

