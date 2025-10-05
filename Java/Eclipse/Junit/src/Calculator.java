
public class Calculator {
	private int n1, n2;
	
	public Calculator(int _n1, int _n2) {
		n1 = _n1;
		n2 = _n2;
	}
	public int add() {
		return n1 + n2;
	}
	public int multiply() {
		return n1 * n2;
	}
}
