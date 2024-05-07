#include<iostream> 
using namespace std; 
 
string city[10]; 
int d[10][10]; 
int space; 
int val; 
 
void cityname(){ 
    cout<<"Enter the number of cities : "; 
    cin>>space; 
    for(int i=0;i<space;i++){ 
        cout<<"Enter Name city no. "<<i+1<<" : "; 
        cin>>city[i]; 
    } 
} 

void distance(){ 
    for(int i=0;i<space;i++){ 
        for(int j=0;j<space;j++){ 
            if(i!=j && d[i][j]==0){ 
                cout<<"Enter distance between "<<city[i]<<" -> "<<city[j]<<" : "; 
                cin>>val; 
                d[i][j]=val; 
                d[j][i]=val; 
            } 
        } 
    } 
} 
 
void add(){ 
    cout<<"Enter Name of city : "; 
    cin>>city[space]; 
    space++; 
    distance(); 
} 
 
void display(){ 
    for(int i=0;i<space;i++){ 
        cout<<"          "<<city[i]; 
    } 
    cout<<endl; 
    cout<<endl; 
    for(int i=0;i<space;i++){ 
        cout<<city[i]; 
        for(int j=0;j<space;j++){ 
            cout<<"         "<<d[i][j]; 
        } 
        cout<<endl; 
        cout<<endl; 
    } 
} 
 
int main(){ 
    cityname(); 
    distance(); 
    int ch; 
    while(true){ 
        cout<<"1. Add a city "<<endl; 
        cout<<"2. Display weight representation : "<<endl; 
        cout<<"3. Exit"<<endl; 
        cout<<"enter choice : "; 
        cin>>ch; 
        if(ch==1){ 
            add(); 
        } 
        else if(ch==2){ 
            display(); 
        } 
        else if(ch==3){ 
            break; 
        } 
    } 
}