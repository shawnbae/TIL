import java.util.Scanner;

class Ex2_10 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); // Scanner클래스의 객체를 생성

		System.out.print("두자리 정수를 하나 입력해주세요.>");
		String input = scanner.nextLine(); // 입력받은 내용을 input에 저장
		int num = Integer.parseInt(input); // 입력받은 내용을 Int타입의 값으로 변환

		System.out.println("입력내용 :" + input);
		System.out.printf("num=%d%n", num);
	}
}