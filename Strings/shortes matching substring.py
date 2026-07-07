class Solution {

    public int shortestMatchingSubstring(String s, String p) {
        String[] parts = p.split("\\*", -1);

        String a = parts[0];
        String b = parts[1];
        String c = parts[2];

        int n = s.length();

        int[] lpsA = buildLPS(a + "#" + s);
        int[] lpsB = buildLPS(b + "#" + s);
        int[] lpsC = buildLPS(c + "#" + s);

        int na = a.length();
        int nb = b.length();
        int nc = c.length();

        int ans = Integer.MAX_VALUE;

        int j = 0, k = 0;

        for (int i = 0; i <= n; i++) {

            while (i < n && na > 0 && lpsA[na + 1 + i] != na)
                i++;

            while (j < n && (j < i + nb || (nb > 0 && lpsB[nb + 1 + j] != nb)))
                j++;

            while (k < n && (k < j + nc || (nc > 0 && lpsC[nc + 1 + k] != nc)))
                k++;

            if (k == n)
                break;

            int start = na == 0 ? i : i;
            int end = nc == 0 ? j : k + 1;

            ans = Math.min(ans, end - start + na);
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private int[] buildLPS(String str) {
        int n = str.length();
        int[] lps = new int[n];

        for (int i = 1; i < n; i++) {
            int j = lps[i - 1];

            while (j > 0 && str.charAt(i) != str.charAt(j))
                j = lps[j - 1];

            if (str.charAt(i) == str.charAt(j))
                j++;

            lps[i] = j;
        }

        return lps;
    }
}