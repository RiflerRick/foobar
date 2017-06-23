/*
This program will be used to test certain parts of the third party solution. The package we will test here is the java.util package as that package has widely been used inside the third party solution of running with bunnies
 */
import java.util.*;
import java.io.*;
class testJava
{
    public static void main(String args[])throws IOException
    {
        // int len=50;
        int max=5;
        LinkedList<LinkedList<Integer>> subsets = new LinkedList<LinkedList<Integer>>();
        // as is clear from the line above it is a linked list of linked lists.
        int maxLen = Integer.toBinaryString(max).length();
        int a=Integer.MAX_VALUE;
        int b=45;
        String str=Integer.toString(b);
        System.out.println(str+',');

    }
}