/**
 * Created by zhaoyan on 7/31/17.
 */
import util.Constructor;
import util.Displayer;
import util.ListNode;
public class Launcher {
    int[] array = {1,2,2,0,0};

    public static void main(String args[]){
        Launcher lan = new Launcher();
        lan.runSolution();
    }
    public void runSolution(){
        Solution_75 sl = new Solution_75();

        sl.sortColors(array);
        Displayer.ArrayDisplay(array);

        //ListNode head = Constructor.listConstructor(array);
        //ListNode new_head = sl.sortColors(head);
        //Displayer.ListDisplay(new_head);
    }
}
