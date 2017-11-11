/**
 * Created by zhaoyan on 7/31/17.
 */
import util.Constructor;
import util.Displayer;
import util.ListNode;
import util.Solution;
public class Launcher {
    int[] array = {1};

    public static void main(String args[]){
        Launcher lan = new Launcher();
        lan.runSolution();
    }
    public void runSolution(){
        Solution sl = new Solution_109();
        sl = (Solution_109) sl;
        

//        sl.sortColors(array);
//        Displayer.ArrayDisplay(array);

//        ListNode head = Constructor.listConstructor(array);
//        ListNode new_head = sl.findMid(head);
//        Displayer.ListDisplay(head);
//        Displayer.ListDisplay(new_head);
    }
}
