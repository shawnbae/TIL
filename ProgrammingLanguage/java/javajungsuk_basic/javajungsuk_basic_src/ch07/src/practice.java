class practice {
    public static void main(String[] args) {
        Car car = new Car();
        FireEngine fe = new FireEngine();
        FireEngine fe2 = null;

        System.out.println(car instanceof FireEngine);
        // fe.water();
        // fe2 = (FireEngine) car;
        // fe2.water();
    }
}

class Car {
    String color;
    int door;

    void driver() {
        System.out.println(("driver"));
    }

    void stop() {
        System.out.println("stop");
    }
}

class FireEngine extends Car {
    void water() {
        System.out.println("water");
    }
}