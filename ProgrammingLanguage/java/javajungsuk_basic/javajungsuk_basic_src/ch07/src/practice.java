class Time {
    int hour;
    int minute;
    int second;
}

public class TimeTest {
    public static void main(String[] args) {
        Time t = new Time();
        t.hour = 100;
        System.out.println(t.hour);
    }
}