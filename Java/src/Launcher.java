/**
 * Created by zhaoyan on 7/31/17.
 */
import util.Constructor;
import util.Displayer;
import util.ListNode;
import util.Solution;
public class Launcher {
    int[] array = {1,2,2,3,5};

    public static void main(String args[]){
        Launcher lan = new Launcher();
        lan.runSolution();
    }
    public void runSolution(){
        ListNode head = Constructor.listConstructor(array);
        Solution_83 sl = new Solution_83();
        sl.deleteDuplicate_recursive(head);
        Displayer.ListDisplay(head);
    }
}
