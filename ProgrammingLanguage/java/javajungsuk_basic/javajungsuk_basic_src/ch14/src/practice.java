import java.util.*;
import java.util.stream.*;

class practice {
    public static void main(String[] args) {
        Stream<String[]> Streamtest = Stream.of(
                new String[] { "abc", "def", "jkl" },
                new String[] { "abc", "def", "jkl" });

        // Streamtest.map(System.out::println);
        Streamtest.flatMap(System.out::println);
    }
}