/*Pizza parlor accepting maximum M orders. Orders are served in first come first served basis.
Order once placed cannot be cancelled. Write C++ program to simulate the system using
circular queue using array*/

#include<iostream>
#define size 10
using namespace std;

class queue
{
	private:
		int front=-1;
		int rear= -1;
	public:
		string arr[size];
		void enqueue();
		void dequeue();
		void display();
		

};
void queue::enqueue()
{
	string Name;
	if(front==-1 && rear==-1)
	{
		cout<<"Enter Name: "<<endl;
		cin>>Name;
		
		front=0;
		arr[front]=Name;
		rear=1;
	}
	else if(rear==front)
	{
		cout<<"\t\t Sorry , Currently Unavailable :) "<<endl;

	}
	else
	{
		cout<<"Enter Name: "<<endl;
		cin>>Name;
		arr[rear]=Name;
		rear=(rear+1)%size;
	}
}
void queue::dequeue()
{
	cout<<"Order of"<<arr[front]<<" is served ..."<<endl;
	do
	{
		arr[front]=arr[front+1];
		front=front+1;
		
	}while(front<rear);
	front=0;
	rear-rear-1;
	
}
void queue :: display()
{
	int i;
	cout<<"List of orders is: "<<endl;
	for(i=front;i<rear;i++)
	{
		cout<<"LIST: \t"<<arr[i]<<endl;
	}
}

int main()
{
	int ch;
	queue obj;
	
	do
	{
		cout<<"Press 1 for ORDER "<<endl;
		cout<<"Press 2 to  Get ORDER"<<endl;
		cout<<"Press 3 to display list of ORDERS"<<endl;
		cout<<"4. EXIT"<<endl;
		
		cout<<"ENTER YOUR CHOICE: ";
		cin>>ch;
		
		switch (ch)
		{
			case 1:
				obj.enqueue();
				break;
			case 2:
				obj.dequeue();
				break;
			case 3:
				obj.display();
				break;
			case 4:
				exit(0);
				break;
		}
	}while(ch!=4);
	return 0;
}