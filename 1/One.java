
public class One {
    // If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    // The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    public static void main(String[] args) {
        int multipleA = 3;
        int multipleB = 5;
        int n = 999; // Since 1000 is not incluided. Can reduce in method but this seemed easy
        System.out.println(one(multipleA, multipleB, n));
        System.out.println(oneJ8(multipleA, multipleB, n));
    }

    public static int one(int a, int b, int n) {
        int maxAMultiple = n / a;
        int maxBMultiple = n / b;
        int maxCommon = n / (a * b);
        int aCount = (maxAMultiple * (maxAMultiple + 1)) / 2;
        int bCount = (maxBMultiple * (maxBMultiple + 1)) / 2;
        int comm = (maxCommon * (maxCommon + 1)) / 2;
        return (aCount * a) + (bCount * b) - (comm * (a * b));
    }

    public static int oneJ8(int a, int b, int n) {
        Operation divisor = (p, q) -> p / q;
        Count count = p -> ((p * (p + 1)) / 2);
        Operation multiple = (p , q) -> p * q;
        return multiple.of(a, count.induction(divisor.of(n, a))) 
            + multiple.of(b, count.induction(divisor.of(n, b)))
            -multiple.of((a * b), count.induction(divisor.of(n, (a * b))));
    }
}

interface Count {
    int induction(int n);    
}

interface Operation {
    int of (int n, int d);
}
