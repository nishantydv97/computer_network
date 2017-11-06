//============================================================================
// Name        : try.cpp
// Author      : Nishant
// Version     :
// Copyright   : public
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
#include <stdlib.h>
#include<math.h>
using namespace std;
int main(){
	cout<<"\n enter the 8 bit data : \n";
	int data[12];
	for(int i=0;i<12;i++){
		if(i!=0 && i!=1 && i!=3 && i!=7){
			cin>>data[i];
		}
		else{
			data[i]=99;
		}
	}
	data[0]=data[2]^data[4]^data[6]^data[8]^data[10];
	data[1]=data[2]^data[5]^data[6]^data[9]^data[10];
	data[3]=data[4]^data[5]^data[6]^data[11];
	data[7]=data[8]^data[9]^data[10]^data[11];
	cout<<"\n bit transfer through the channel are : \n";
	for(int i=0;i<12;i++){
		cout<<data[i]<<" ";
	}
	int rcv[12];
	cout<<"\n enter the bit received by the receiver : \n";
	for(int i=0;i<12;i++){
		cin>>rcv[i];
	}
	int p[4];
	if(rcv[0]==(rcv[2]^rcv[4]^rcv[6]^rcv[8]^rcv[10])){
		p[0]=0;
	}else{
		p[0]=1;
	}
	if(rcv[1]==(rcv[2]^rcv[5]^rcv[6]^rcv[9]^rcv[10])){
		p[1]=0;
	}else{
		p[1]=1;
	}
	if(rcv[3]==(rcv[4]^rcv[5]^rcv[6]^rcv[11])){
		p[2]=0;
	}else{
		p[2]=1;
	}
	if(rcv[7]==(rcv[8]^rcv[9]^rcv[10]^rcv[11])){
		p[3]=0;
	}else{
		p[3]=1;
	}
	int sum=0;
	for(int i=0;i<4;i++){
		sum+=p[i]*pow(2,i);
	}
	if(sum==0){
		cout<<"no bit is bad :";
	}else{
		cout<<"bad bit is :"<<sum<<": from left side "<<endl;
	}
	if(rcv[sum-1]==1){
		rcv[sum]=0;
	}else{
		rcv[sum-1]=1;
	}
	cout<<"correct bit or error free bit are as follows \n";
	for(int i=0;i<12;i++){
		cout<<rcv[i]<<" ";
	}
	return 0;
}
/*
 enter the 8 bit data : 
1 1 0 0 0 1 0 0

 bit transfer through the channel are : 
0 0 1 1 1 0 0 1 0 1 0 0 
 enter the bit received by the receiver : 
0 0 1 1 0 0 0 1 0 1 0 0
bad bit is :5: from left side 
correct bit or error free bit are as follows 
0 0 1 1 1 0 0 1 0 1 0 0 
 */

