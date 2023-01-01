/*Write program to implement a priority queue in C++ using an inorder list to store the items
in the queue. Create a class that includes the data items (which should be template) and the
priority (which should be int). The inorder list should contain these objects, with operator <=
overloaded so that the items with highest priority appear at the start of the list (which will
make it relatively easy to retrieve the highest item.)
      
      OR

Write a C++ program to simulating job queue by using array and linked list.
"""*/

#include<iostream> 
using namespace std; 
#define size 10 
 
class job{ 
    public: 
        int front=-1; 
        int rear=-1; 
        int a[10],i; 
        void ins(){ 
            int val; 
            if(front==-1 && rear==-1){ 
                front=0; 
                cout<<"Enter the ID : "; 
                cin>>val; 
                a[front]=val; 
                rear=1; 
            } 
            else if (front==rear) 
            { 
                cout<<"No Jobs"<<endl; 
            } 
            else{ 
                cout<<"Enter Job Id : "; 
                cin>>val; 
                a[rear]=val; 
                rear=rear+1; 
            } 
        } 
        void del(){ 
            for(i=0;i<rear;i++){ 
                a[i]=a[i+1]; 
            } 
            rear=rear-1; 
        } 
        void display(){ 
            cout<<"Jobs are : "<<"<-- "; 
            for(i=front;i<rear;i++){ 
                cout<<a[i]<<" "; 
            } 
            cout<<" <--"<<endl; 
 
        } 
}; 
int main(){ 
    int k=0; 
    int c; 
    job obj; 
    while(k==0){ 
        cout<<"Press 1 to Insert Job"<<endl; 
        cout<<"Press 2 to Delete Job"<<endl; 
        cout<<"press 3 to exit"<<endl; 
        cin>>c; 
        if(c==1){ 
            obj.ins(); 
            obj.display(); 
        } 
        if(c==2){ 
            obj.del(); 
            obj.display(); 
        } 
        if(c==3){ 
            k=1; 
        } 
    } 
}