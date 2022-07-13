class Ex6_14 {
	// 클래스 초기화 블럭
	// --> 클래스 생성 시 한번만 수행
	static {
		System.out.println("static { }");
	}

	// 인스턴스 초기화 블럭
	// --> 인스턴스가 불러질 때마다 수행
	{
		System.out.println("{ }");
	}

	public Ex6_14() {
		System.out.println("생성자");
	}

	public static void main(String args[]) {
		System.out.println("Ex6_14 bt = new Ex6_14(); ");
		Ex6_14 bt = new Ex6_14();

		System.out.println("Ex6_14 bt2 = new Ex6_14(); ");
		Ex6_14 bt2 = new Ex6_14();
	}
}