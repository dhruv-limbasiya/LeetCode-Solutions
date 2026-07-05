class Solution
{
    public:
        bool isSameAfterReversals(int num)
        {
            int n =num;
            int rev = 0;
            if (num == 0)
            {
                return true;
            }
            while (num != 0)
            {
                int d = num % 10;
                rev = rev *10 + d;
                num = num / 10;
            }
            int rev2 = 0;
            while (rev != 0)
            {
                int d2 = rev % 10;
                rev2=rev2*10+d2;
                rev = rev / 10;
            }
            if (rev2 == n)
            {
                return true;
            }
            return false;
        }
};