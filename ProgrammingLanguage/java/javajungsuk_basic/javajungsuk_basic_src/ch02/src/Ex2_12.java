class Ex2_12 {
	public static void main(String args[]) {
		String str = "3";

		System.out.println(str.charAt(0) - '0'); // 숫자를 문자로 변환 (숫자에 '0' 더하기)
		System.out.println('3' - '0' + 1);
		System.out.println(Integer.parseInt("3") + 1);
		System.out.println("3" + 1);
		System.out.println(3 + '0');
	}
}