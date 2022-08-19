import java.util.*;
import java.text.*;

class practice {
    public static void main(String[] args) {
        Date today = new Date();

        SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
        SimpleDateFormat sdf5, sdf6, sdf7, sdf8, sdf9;

        sdf1 = new SimpleDateFormat("yyyy-MM-dd");
        sdf2 = new SimpleDateFormat("''yy년 MMM dd일 E요일");
        sdf3 = new SimpleDateFormat("yyyy-MM-dd");
        sdf4 = new SimpleDateFormat("yyyy-MM-dd");

        System.out.println(sdf2.format(today));
    }
}