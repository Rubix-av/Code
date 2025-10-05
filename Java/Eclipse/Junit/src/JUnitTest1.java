import static org.junit.Assert.*;

import org.junit.Test;

public class JUnitTest1 {

	@Test
	public void test() {
		Calculator c = new Calculator(10, 20);
		assertEquals(31, c.add());
	}

}
