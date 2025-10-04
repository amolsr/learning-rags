/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

class A implements Runnable {
	public void run(){
		for(int i = 0 ; i < 1000 ; i++){
			System.out.println(i);
		}
	}
}

/* Name of the class has to be "Main" only if the class is public. */
public class RunnableExample
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Thread t1 = new Thread(new A());
		Thread t2 = new Thread(new A());
		t1.start();
		t2.start();
	}
}
