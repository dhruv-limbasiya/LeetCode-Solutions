class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        ps = path.split('/')

        for i in ps:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if st:
                    st.pop()
            else:
                st.append(i)

        return '/' + '/'.join(st)