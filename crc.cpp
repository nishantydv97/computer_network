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
	string msg,gen;
	int gen_len,msg_len;
	cout<<"enter the messages in the form of string : \n";
	cin>>msg;
	cout<<"enter the generator in the form of string :\n";
	cin>>gen;
	gen_len=gen.length();
	msg_len=msg.length();
	for(int i=0;i<(gen_len-1);i++){
		msg+='0';
	}
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
	for(int i=msg.length(),j=0;j<gen_len-1;i--,j++){
		m[i]=msg[i];
	}
	cout<<"message transfer through the channel are "<<m<<endl;
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
	cout<<"Remainder are "<<m<<endl;
	bool flag;
	for(int i=0;i<m.length();i++){
		if(m[i]!='0'){
			flag=1;
		}
	}
	if(flag==1){
		cout<<"error in the code "<<endl;
	}
	else{
		cout<<"no error in the code "<<endl;
	}
	return 0;
}
/*
 * enter the messages in the form of string :
1011011
enter the generator in the form of string :
1101
message transfer through the channel are 1011011001
Remainder are 0000000000
no error in the code
 */
