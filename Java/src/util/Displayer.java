package util;

/**
 * Created by zhaoyan on 8/1/17.
 */
public class Displayer {
    public static void ListDisplay(ListNode head){
        while (head != null){
            System.out.print(head.val);
            head = head.next;
        }
    }
}
