class Ex3_10 {
	public static void main(String args[]) {
		long a = 1_000_000 * 1_000_000;
		long b = 1_000_000 * 1_000_000L; // Long 타입으로 변환해야 한다.

		System.out.println("a=" + a);
		System.out.println("b=" + b);
	}
}