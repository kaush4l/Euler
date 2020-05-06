
public class One {
    public static void main(String[] args) {
        int multipleA = 3;
        int multipleB = 5;
        int n = 999;
        System.out.println(one(multipleA, multipleB, n));
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
}