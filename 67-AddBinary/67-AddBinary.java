// Last updated: 8/16/2026, 9:53:00 PM
class Solution {
    public String addBinary(String a, String b) {
        char[] aChars = a.toCharArray();
        char[] bChars = b.toCharArray();
        StringBuilder res = new StringBuilder();

        int i = a.length() - 1, j = b.length() - 1;
        int carry = 0;
        while( i >= 0 || j >= 0) {
            int sum = carry;
            if(i >= 0) sum += aChars[i --] - '0';
            if(j >= 0) sum += bChars[j --] - '0';
            
            // if(sum < 2) {
            //     res.append(sum);
            //     carry = 0;
            // } else {
            //     res.append(sum - 2);
            //     carry = 1;
            // }

            // OR use the binary feature, relation of 2
            res.append( sum % 2 );
            carry = sum / 2;
        }
        if(carry > 0) res.append(carry);

        return res.reverse().toString();

    }
}