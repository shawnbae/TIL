abstract class Unit {
    int x, y;

    abstract void move(int x, int y);

    void stop() {
        System.out.println("추상클래스의 stop method");
    }
}

interface Fightable {
    void move(int x, int y);

    void attack(Fightable f);
}

class Fighter extends Unit implements Fightable {
    public void move(int x, int y) {
        System.out.println("move");
    }

    public void attack(Fightable f) {
        System.out.println("attack");
    }
}

public class practice {
    public static void main(String[] args) {
        Fightable f = new Fighter();

        f.move(100, 200);
        f.attack(f);

        Fighter f2 = new Fighter();
        f2.stop();
    }
}