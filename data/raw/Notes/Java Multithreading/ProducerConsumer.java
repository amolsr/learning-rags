/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

class Producer extends Thread {
	List<Integer> l;
	
	public Producer(List<Integer> l){
		this.l = l;
	}
	public void run(){
		for(int i = 0 ; i < 1000 ; i++){
			l.add(i);
			System.out.println("Added item" + i);
		}
	}
}

class Consumer extends Thread {
	List<Integer> l;
	
	public Consumer(List<Integer> l){
		this.l = l;
	}
	public void run(){
		while(l != null && !l.isEmpty()){
			System.out.println("Consuming" + l.get(l.size() - 1));
		    l.remove(l.size() - 1);
		}
	}
}

/* Name of the class has to be "Main" only if the class is public. */
class ProducerConsumer
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		List<Integer> l = Collections.synchronizedList(new ArrayList<>());
		Thread t1 = new Producer(l);
		Thread t2 = new Consumer(l);
		t1.start();
		t2.start();
	}
}
